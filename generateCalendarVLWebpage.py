#!/usr/bin/python -tt

from VLebretCalendar import VLebretCalendar
from datetime import date, timedelta


def vl_days_calculation(year):
    vl_days = []
    stard_date = date(year=year, month=1, day=1)
    end_date = date(year=year, month=12, day=31)

    change_year = date(year=2023, month=9, day=18)

    holiday = [
        (date(year=2023, month=2, day=10), date(year=2023, month=2, day=19), "jg"),
        (date(year=2023, month=2, day=19), date(year=2023, month=2, day=25), "vl"),
        (date(year=2023, month=4, day=14), date(year=2023, month=4, day=22), "jg"),
        (date(year=2023, month=4, day=22), date(year=2023, month=4, day=29), "vl"),
        (date(year=2023, month=7, day=8), date(year=2023, month=7, day=15), "vl"),
        (date(year=2023, month=7, day=15), date(year=2023, month=7, day=22), "jg"),
        (date(year=2023, month=7, day=22), date(year=2023, month=7, day=29), "vl"),
        (date(year=2023, month=7, day=29), date(year=2023, month=8, day=5), "jg"),
        (date(year=2023, month=8, day=5), date(year=2023, month=8, day=12), "vl"),
        (date(year=2023, month=8, day=12), date(year=2023, month=8, day=19), "jg"),
        (date(year=2023, month=8, day=19), date(year=2023, month=8, day=26), "vl"),
        (date(year=2023, month=8, day=26), date(year=2023, month=9, day=2), "jg"),
        (date(year=2023, month=10, day=21), date(year=2023, month=10, day=28), "jg"),
        (date(year=2023, month=10, day=28), date(year=2023, month=11, day=4), "vl"),
        (date(year=2023, month=12, day=22), date(year=2023, month=12, day=30), "vl"),
        (date(year=2023, month=12, day=30), date(year=2024, month=1, day=6), "jg"),
        (date(year=2024, month=2, day=24), date(year=2024, month=3, day=1), "jg"),
        (date(year=2024, month=3, day=1), date(year=2024, month=3, day=9), "vl"),
        (date(year=2024, month=4, day=12), date(year=2024, month=4, day=19), "vl"),
        (date(year=2024, month=4, day=19), date(year=2024, month=4, day=27), "jg")
    ]

    curr_date = stard_date
    while curr_date != end_date:
        is_holiday = False
        idx = "vl"
        for start_h, end_h, idx in holiday:
            if curr_date >= start_h and curr_date < end_h:
                is_holiday = True
                break
        if is_holiday:
            if idx == "vl":
                vl_days.append((curr_date.month, curr_date.day))
        elif curr_date >= change_year:
            if curr_date.isocalendar()[1] % 2:
                if curr_date.isoweekday() in [1, 4, 5, 6, 7]:
                    vl_days.append((curr_date.month, curr_date.day))
            else:
                if curr_date.isoweekday() in [2, 3, 4]:
                    vl_days.append((curr_date.month, curr_date.day))
        else:
            if curr_date.isocalendar()[1] % 2:
                if curr_date.isoweekday() in [1, 2, 4, 5]:
                    vl_days.append((curr_date.month, curr_date.day))
            else:
                if curr_date.isoweekday() in [3, 6, 7]:
                    vl_days.append((curr_date.month, curr_date.day))
        curr_date += timedelta(days=1)

    return vl_days


def main():
    for idx in range(2):
        current_year = date.today().year - 1 + idx  # get from today, the current year
        vl_days = vl_days_calculation(current_year)
        c = VLebretCalendar(vl_days).formatyearpage(current_year, 4)
        print(c)


if __name__ == '__main__':
    main()
