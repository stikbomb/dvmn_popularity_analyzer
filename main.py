import os
from datetime import datetime, timedelta

import requests
import dotenv
import plotly.graph_objects as go


class APIError(Exception):
    pass


def get_timestamps(number_of_days):
    current_time = datetime.today()

    hours = 0
    minutes = 0

    day = datetime(current_time.year, current_time.month, current_time.day, hours, minutes)

    result = []

    for _ in range(number_of_days):

        day_timestamp = datetime.timestamp(day)
        previous_day = day - timedelta(hours=24)
        previous_day_timestamp = datetime.timestamp(previous_day)

        result.append((datetime.date(day), day_timestamp, previous_day_timestamp))

        day = previous_day

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

    timestamps = get_timestamps(7)

    stats_by_period = get_stats_by_period(vk_data, query, timestamps)

    get_chart(stats_by_period)
