# Notes:
# BeautifulSoup alone won't work as the page is loaded through javascript (??). So need the reading of the HTML
# to be delayed until js has finished loading (hence using selenium instead with a 10 secon delay)
# Then BeautifulSoup is used to parse through the available page and extract the page source
# Then determine if appropriate days/ times are available
# Send an alert when days time are available/ or if they have been missed
# Then use selenium to "click" through and complete the booking (Maybe this last part if I can figure it out)

from datetime import date, timedelta, datetime
import calendar
import time

# input the variables to check and date to build URL to check
# NOTE: Was called build_ONE_url_to_check
def build_booker_url_to_check(input_date, location_service_provider):
    url_to_check_pt1 = 'https://go.booker.com/location/'
    url_to_check_pt2 = '/service/'
    url_to_check_pt3 = '/Short%20Cut%20/availability/'
    url_to_check_pt4 = '/provider/'

    # date_in_question = datetime.strptime(input_date, '%Y-%m-%d').date()
    if type(input_date) != str:  # if it's already in string format, leave it as str. If not, make it str
        input_date = str(input_date)

    location_service_provider_as_list = location_service_provider.split(",")
    location = location_service_provider_as_list[0]
    service = location_service_provider_as_list[1]
    provider = location_service_provider_as_list[2]

    # check URL with userinput date
    concatenated_url = url_to_check_pt1 + location + url_to_check_pt2 + service + url_to_check_pt3 + input_date + url_to_check_pt4 + provider

    return concatenated_url


# def get_list_of_urls(variables_for_url):
#     list_of_urls = []
#
#         global today  # don't need to keep asking today's date, get it once, be done
#         first_of_next_month = get_first_of_month(today, 1)
#         first_of_2_months_out = get_first_of_month(today, 2)
#
#     for each_set_of_variables in variables_for_url:
#         # Get 3 URLS (based on current date, next month, month after that)
#         url_for_current_date = build_booker_url_to_check(each_set_of_variables, today)
#         list_of_urls.append(url_for_current_date)
#         url_for_next_month = build_booker_url_to_check(each_set_of_variables, first_of_next_month)
#         list_of_urls.append(url_for_next_month)
#         url_for_next_two_month = build_booker_url_to_check(each_set_of_variables, first_of_2_months_out)
#         list_of_urls.append(url_for_next_two_month)
#
#     return list_of_urls
#
#
# def create_date_specific_url_because_I_did_a_poor_job_coding(date):
#     url_to_check_pt1 = 'https://go.booker.com/location/'
#     url_to_check_pt2 = '/service/'
#     url_to_check_pt3 = '/Short%20Cut%20/availability/'
#     url_to_check_pt4 = '/provider/'
#
#     # date_in_question = datetime.strptime(input_date, '%Y-%m-%d').date()
#     if type(date) != str:  # if it's already in string format, leave it as str. If not, make it str
#         date = str(date)
#
#     url_for_current_date = build_booker_url_to_check(providers_info_to_search_for, date)
#
#     return url_for_current_date
#
#
# def get_dates_specifically_to_search_for(dates_and_times_to_search):
#     list_of_specific_dates = []
#
#     list_of_dates_and_times = dates_and_times_to_search.split("|")
#
#     for each_date in list_of_dates_and_times:
#         list_of_specific_dates = each_date[0]
#
#     #    for each_specific_date in dates_and_times_to_search:
#
#     #    list_of_specific_dates_and_times = collected_data_as_string[0].split("|")
#
#     #    for each_date in dates_and_times_to_search:
#     #        specific_dates.append(***)
#
#     return list_of_specific_dates
#

# Main Body
def mainBody(input_date, location_service_provider):

    print("URL types of input: ")
    print(type(input_date))
    print(input_date)
    print(type(location_service_provider))
    print(location_service_provider)

    generated_url = build_booker_url_to_check(input_date, location_service_provider)

    return generated_url
