import os
from datetime import datetime, timedelta

import requests
import dotenv
import plotly.graph_objects as go


class APIError(Exception):
    pass


class IntervalError(Exception):
    pass


def get_hours_of_interval(interval_type):
    if interval_type == 'day':
        return 24
    elif interval_type == 'week':
        return 168
    elif interval_type == 'month':
        return 5040
    else:
        raise IndexError(f'Interval type "{interval_type}" doesn\'t exist')


def get_timestamps(number_of_intervals, interval_type):
    current_time = datetime.today()

    hours = 0
    minutes = 0

    interval = datetime(current_time.year, current_time.month, current_time.day, hours, minutes)

    result = []

    hours = get_hours_of_interval(interval_type)

    for _ in range(number_of_intervals):

        interval_timestamp = datetime.timestamp(interval)
        previous_interval = interval - timedelta(hours=hours)
        previous_interval_timestamp = datetime.timestamp(previous_interval)

        result.append((datetime.date(interval), interval_timestamp, previous_interval_timestamp))

        interval = previous_interval

    return result


def check_error_in_response(decoded_response):
    try:
        if decoded_response['error']:
            error_code = decoded_response['error']['error_code']
            error_msg = decoded_response['error']['error_msg']
            raise APIError(f'Error {error_code} - {error_msg}')
    except KeyError:
        pass


def get_number_of_references_by_interval(vk_data, query, start_timestamp, end_timestamp):
    url = 'https://api.vk.com/method/newsfeed.search'

    token, api_version = vk_data

    payload = {
        'q': query,
        'access_token': token,
        'v': api_version,
        'start_time': start_timestamp,
        'end_time': end_timestamp
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    decoded_response = response.json()
    check_error_in_response(decoded_response)

    number_of_references = decoded_response['response']['total_count']

    return number_of_references


def get_stats_by_period(vk_data, query, period):
    result = []
    for interval in period:
        day_date, end_timestamp, start_timestamp = interval
        day_result = get_number_of_references_by_interval(vk_data, query, start_timestamp, end_timestamp)
        result.append((day_date, day_result))
    return result


def get_chart(stats_by_period):
    dates = []
    counts = []
    for item in stats_by_period:
        dates.append(item[0])
        counts.append(item[1])

    fig = go.Figure([go.Bar(x=dates, y=counts)])
    fig.show()


if __name__ == '__main__':

    dotenv.load_dotenv()
    vk_access_token = os.getenv('VK_ACCESS_TOKEN')
    vk_api_version = os.getenv('VK_API_VERSION')

    vk_data = [vk_access_token, vk_api_version]

    query = 'Coca-cola'
    number_of_intervals = 7
    interval_type = 'week'

    timestamps = get_timestamps(number_of_intervals, interval_type)

    stats_by_period = get_stats_by_period(vk_data, query, timestamps)

    get_chart(stats_by_period)
