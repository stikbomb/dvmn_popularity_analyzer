from datetime import datetime, timedelta


class IntervalError(Exception):
    pass


def get_days_of_interval(interval_type):
    if interval_type == 'day':
        return 1
    elif interval_type == 'week':
        return 7
    elif interval_type == 'month':
        return 30
    else:
        raise IntervalError(f'Interval type "{interval_type}" doesn\'t exist')


def get_interval_dates(number_of_intervals, interval_type):

    interval_date = datetime.today().date()
    days = get_days_of_interval(interval_type)
    interval_dates = [(interval_date - timedelta(days=days) * i) for i in range(number_of_intervals)]
    return interval_dates


def get_today_datetime():
    today = datetime.today()
    hours = 0
    days = 0
    return datetime(today.year, today.month, today.day, hours, days)


def get_timestamps(number_of_intervals, interval_type):

    end_interval_date = get_today_datetime()

    result = []

    days = get_days_of_interval(interval_type)

    for _ in range(number_of_intervals):

        end_timestamp = datetime.timestamp(end_interval_date)
        start_interval_date = end_interval_date - timedelta(days=days)
        start_timestamp = datetime.timestamp(start_interval_date)

        result.append((datetime.date(end_interval_date), end_timestamp, start_timestamp))

        end_interval_date = start_interval_date

    return result
