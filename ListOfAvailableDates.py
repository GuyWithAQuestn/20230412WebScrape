from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime

# Given pagesource HTML, will scour page source for buttons and return list of available dates (active buttons)
#   When checked, should check sources for current month, next month, and month after that to get a more complete picture (so
#   this should be called at least 3x in a row
def check_what_dates_are_available(list_of_webpage_content_to_check):
    list_of_dates_available = []


    for each_pagesource in list_of_webpage_content_to_check:
        soup_of_page_source_for_url_for_current_date = BeautifulSoup(each_pagesource, 'lxml')

        button_list = soup_of_page_source_for_url_for_current_date.find_all('button', {
            'class': 'ember-power-calendar-day ember-power-calendar-day--interactive ember-power-calendar-day--current-month'})

        for button in button_list:
            # ... and if it's present, make sure it's not disabled
            if button.has_attr("disabled"):
                do = "nothing"
            else:
                active_buttons_data_date = button.get("data-date")
                list_of_dates_available.append(active_buttons_data_date)

    return list_of_dates_available


def mainBody(list_of_stored_up_webpage_code):

    list_of_dates_available = check_what_dates_are_available(list_of_stored_up_webpage_code)
    #    print("List of available dates")
    #    print(list_of_dates_available)

    return list_of_dates_available

