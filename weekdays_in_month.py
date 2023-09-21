import calendar


def weekdays_in_month(
    year, month, week_day
):  # week_day -> 0: Monday, 1: Tuesday, ..., 6: Sunday
    all_days_in_month = calendar.Calendar().itermonthdays(year, month)

    day_count = 0

    for day in all_days_in_month:
        if day != 0 and calendar.weekday(year, month, day) == week_day:
            day_count += 1

    return day_count


def weekdays_in_month_2(year, month, week_day):
    weeks_list = calendar.monthcalendar(year, month)
    # monthcalendar returns an array of week lists
    # ex. Aug 2022
    # [
    #     [1, 1, 1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 1, 1, 1],
    #     [1, 1, 1, 0, 0, 0, 0],
    # ]

    day_count = 0

    for week in weeks_list:
        if week[week_day] != 0:
            day_count += 1
    return day_count


print(weekdays_in_month(2022, 8, 2))
print(weekdays_in_month_2(2022, 8, 2))
