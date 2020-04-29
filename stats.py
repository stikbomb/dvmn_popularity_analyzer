import time
from api_tools import get_number_of_references_by_interval


def get_stats_by_period(vk_data, query, period):
    result = []
    for interval in period:
        day_date, end_timestamp, start_timestamp = interval
        day_result = get_number_of_references_by_interval(vk_data, query, start_timestamp, end_timestamp)
        result.append((day_result))
        time.sleep(3)
    return result


def get_stats_for_queries(vk_data, queries, period):
    result = []
    for query in queries:
        query_result = get_stats_by_period(vk_data, query, period)
        result.append(query_result)
        time.sleep(5)
    return result

