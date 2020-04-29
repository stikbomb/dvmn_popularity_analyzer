import requests


class APIError(Exception):
    pass


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
