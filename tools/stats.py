import time

import pandas as pd

from tools.api import get_number_of_references_by_interval


def get_stats_by_period(vk_data, query, period):
    result = []
    for interval in period:
        day_date, end_timestamp, start_timestamp = interval
        day_result = get_number_of_references_by_interval(vk_data, query, start_timestamp, end_timestamp)
        result.append(day_result)
        time.sleep(1)
    return result


def get_dataframe(vk_data, queries, dates, period):
    df = pd.DataFrame(data=dates)
    for query in queries:
        query_result = get_stats_by_period(vk_data, query, period)
        df[query] = query_result
    return df
