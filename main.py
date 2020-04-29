import os

import dotenv

from tools.parser import parse_args
from tools.time import get_interval_dates, get_timestamps
from tools.stats import get_dataframe
from tools.plot import get_chart


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

    df = get_dataframe(vk_data, queries, dates, period)

    get_chart(df)
