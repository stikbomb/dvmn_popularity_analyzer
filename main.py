import os

import dotenv

from args_parser import parse_args
from time_tools import get_interval_dates, get_timestamps
from stats import get_stats_for_queries
from plot_tools import get_group_chart


if __name__ == '__main__':

    dotenv.load_dotenv()

    vk_access_token = os.getenv('VK_ACCESS_TOKEN')
    vk_api_version = os.getenv('VK_API_VERSION')

    vk_data = [vk_access_token, vk_api_version]

    args = parse_args()

    queries = args.queries
    number = args.number
    interval_type = args.interval

    dates = get_interval_dates(number, interval_type)
    period = get_timestamps(number, interval_type)
    queries_stats = get_stats_for_queries(vk_data, queries, period)

    get_group_chart(dates, queries_stats)
