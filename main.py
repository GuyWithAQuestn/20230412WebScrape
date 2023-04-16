import ReadInParametersFile
import FirstOfTheMonths
import GenerateHaircutURL
import ScrapeWebPage
import ListOfAvailableDates
import AttemptToMatchDate
import SearchForSurroundingDates
import SearchForDatesAfterLastWanted
import AttemptToBookAppointment


# File Read In Parameters: [Wanted Days, Times];[Provider Details];email;password
dates_and_times_to_search_list, location_service_provider_list, email_address, email_password = ReadInParametersFile.mainBody()

first_of_this_month, first_of_next_month, first_of_2_months_out = FirstOfTheMonths.mainBody()


list_of_generated_urls = []
list_of_page_sources = []
# Create URLs for 1st of month, 1st of next month, 1st of next-next month
# GenerateHaircutURL.mainBody(date, location_service_provider)
# For loop in case there are multiple location_service_provider

for each_location_service_provider in location_service_provider_list:
    url_for_this_month = GenerateHaircutURL.mainBody(first_of_this_month, each_location_service_provider)
    list_of_generated_urls.append(url_for_this_month)

    # url_for_next_month = GenerateHaircutURL.mainBody(first_of_next_month, each_location_service_provider)
    # list_of_generated_urls.append(url_for_next_month)
    #
    # url_for_next_next_month = GenerateHaircutURL.mainBody(first_of_2_months_out, each_location_service_provider)
    # list_of_generated_urls.append(url_for_next_next_month)

print("Urls: ")
print(list_of_generated_urls)

list_of_each_page_source = []
iteration = 0

for each_url in list_of_generated_urls:
    returned_page_source = ScrapeWebPage.mainBody(each_url)
    list_of_each_page_source.append(returned_page_source)

#get list of available dates
#list_of_dates_available = FindMatchingDate.check_what_dates_are_available(list_of_page_sources)
list_of_dates_available = ListOfAvailableDates.mainBody(list_of_each_page_source)

print("list_of_dates_available")
print(list_of_dates_available)

date_was_matched_flag = False

date_was_matched_flag, date_matched = AttemptToMatchDate.mainBody(dates_and_times_to_search_list,list_of_dates_available)

print("returned results: ")
print(date_was_matched_flag)
print(date_matched)

# If dates was matched, attempt to book appointment
if date_was_matched_flag == True:
    # Build a new URL for the exact date and scrape it
    # Will attempt all location_service_provider_list as I didn't keep track of this well until now unfortunately
    wanted_date_url_to_book_list = []

    for each_set_of_provider_details in location_service_provider_list:
        date_matched_and_times = date_matched.split(",")
        date_matched_only = date_matched_and_times[0]

        wanted_date_url_to_book = GenerateHaircutURL.mainBody(date_matched_only,each_set_of_provider_details)
        wanted_date_url_to_book_list.append(wanted_date_url_to_book)

    print("List of urls to attempt to book: ")
    print(wanted_date_url_to_book_list)

    appointment_was_booked_flag = AttemptToBookAppointment.mainBody(date_matched,)

# If dates weren't matched, want to look for other dates from that week or future dates
# If found, send messages as a window was missed
if date_was_matched_flag == False:

    dates_that_week_found_flag = SearchForSurroundingDates.mainBody(dates_and_times_to_search_list,list_of_dates_available)
    if dates_that_week_found_flag == False:
        print("Carry on; nothing to see here")
    else:
        print("Dates were found the week of the wanted dates; send a message to the user")

    dates_found_after_last_wanted_date_flag = SearchForDatesAfterLastWanted.mainBody(dates_and_times_to_search_list,list_of_dates_available)
    if dates_found_after_last_wanted_date_flag == False:
        print("Carry on; nothing to see here")
    else:
        print("Dates were found after the wanted dates; send a message to the user")
