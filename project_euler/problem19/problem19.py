import datetime as datetime


def how_many_sundays_on_first_of_month(start_date: str, end_date: str):
    count = 0
    # convert the dates to integers
    start_date = [int(x) for x in start_date.split("/")]
    end_date = [int(x) for x in end_date.split("/")]
    for year in range(start_date[2], end_date[2] + 1):
        for month in range(start_date[1], end_date[1] + 1):
            if datetime.date(year, month, 1).weekday() == 6:
                count += 1
    return count


print(how_many_sundays_on_first_of_month("1/1/1901", "31/12/2000"))
