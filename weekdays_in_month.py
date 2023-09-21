import calendar


def weekdays_in_month(
    year, month, week_day
):  # week_day -> 0: Monday, 1: Tuesday, ..., 6: Sunday
    all_days_in_month = calendar.Calendar().itermonthdays(year, month)

    count_days = 0

    for day in all_days_in_month:
        if day != 0 and calendar.weekday(year, month, day) == week_day:
            count_days += 1

    return count_days
