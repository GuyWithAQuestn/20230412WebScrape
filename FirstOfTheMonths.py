# Notes:
# BeautifulSoup alone won't work as the page is loaded through javascript (??). So need the reading of the HTML
# to be delayed until js has finished loading (hence using selenium instead with a 10 secon delay)
# Then BeautifulSoup is used to parse through the available page and extract the page source
# Then determine if appropriate days/ times are available
# Send an alert when days time are available/ or if they have been missed
# Then use selenium to "click" through and complete the booking (Maybe this last part if I can figure it out)

# Tutorial series how to use Selenium with python:
# https://www.youtube.com/watch?v=b5jt2bhSeXs
# https://www.youtube.com/watch?v=U6gbGk5WPws
# https://www.youtube.com/watch?v=OISEEL5eBqg

# PACKAGES TO INSTALL
# datetime
# calendar
# time

from datetime import date, timedelta, datetime
import calendar
import time


# Get the date of the first of the month (month_offset: 0=current month, 1=next month, 2=2 months, etc)
def get_first_of_month(date, month_offset=0):
    list_of_dates = []

    # zero based indexing of month to make math work
    month_count = date.month - 1 + month_offset
    return date.replace(
        day=1, month=month_count % 12 + 1, year=date.year + (month_count // 12)
    )


def mainBody():
    today = date.today()
    list_of_dates = []

    first_of_this_month = get_first_of_month(today, 0)
    first_of_next_month = get_first_of_month(today, 1)
    first_of_2_months_out = get_first_of_month(today, 2)

    first_of_this_month_str = first_of_this_month.strftime("%Y-%m-%d")
    first_of_next_month_str = first_of_next_month.strftime("%Y-%m-%d")
    first_of_2_months_out_str = first_of_2_months_out.strftime("%Y-%m-%d")


    # list_of_dates.append(first_of_this_month)
    # list_of_dates.append(first_of_next_month)
    # list_of_dates.append(first_of_2_months_out)

    return first_of_this_month_str, first_of_next_month_str, first_of_2_months_out_str