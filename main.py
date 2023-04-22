import ReadInParametersFile
import FirstOfTheMonths
import GenerateHaircutURL
import ScrapeWebPage
import ListOfAvailableDates
import AttemptToMatchDate
import SearchForSurroundingDates
import SearchForDatesAfterLastWanted
import AttemptToBookAppointment
import SendDiscordMessage

import time
import datetime


def is_hour_between(start, end):

    # Time Now
    now = datetime.datetime.now().time()

    is_between = False

    is_between |= start <= now <= end
    is_between |= end < start and (start <= now or now <= end)

    return is_between
def heart_of_the_operation(dates_and_times_to_search_list, location_service_provider_list, email_address, email_password):


    first_of_this_month, first_of_next_month, first_of_2_months_out = FirstOfTheMonths.mainBody()


    list_of_generated_urls = []
    list_of_page_sources = []
    list_of_locations_service_provider = []
    # Create URLs for 1st of month, 1st of next month, 1st of next-next month
    # GenerateHaircutURL.mainBody(date, location_service_provider)
    # For loop in case there are multiple location_service_provider


    for each_location_service_provider in location_service_provider_list:
        url_for_this_month = GenerateHaircutURL.mainBody(first_of_this_month, each_location_service_provider)
        list_of_generated_urls.append(url_for_this_month)
        list_of_locations_service_provider.append(each_location_service_provider)

        url_for_next_month = GenerateHaircutURL.mainBody(first_of_next_month, each_location_service_provider)
        list_of_generated_urls.append(url_for_next_month)
        list_of_locations_service_provider.append(each_location_service_provider)

        url_for_next_next_month = GenerateHaircutURL.mainBody(first_of_2_months_out, each_location_service_provider)
        list_of_generated_urls.append(url_for_next_next_month)
        list_of_locations_service_provider.append(each_location_service_provider)

    list_of_each_page_source = []
    list_of_each_locations_service_provider = []

    # for each of the URLS, check at that time for matches
    date_was_matched_flag = False
    iteration = 0
    for each_url in list_of_generated_urls:
        returned_page_source = ScrapeWebPage.mainBody(each_url)
        list_of_each_page_source.append(returned_page_source)
        list_of_each_locations_service_provider.append(list_of_locations_service_provider[iteration])
        iteration += 1

        # while still looking at this URL, let's search for the matches

    #get list of available dates
    #list_of_dates_available = FindMatchingDate.check_what_dates_are_available(list_of_page_sources)
        list_of_dates_available = ListOfAvailableDates.mainBody(list_of_each_page_source)

        print("list_of_dates_available")
        print(list_of_dates_available)

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
            print("List of date & times to attempt to book: ")
            print(date_matched_and_times)

            appointment_was_booked_flag = AttemptToBookAppointment.mainBody(wanted_date_url_to_book_list,date_matched_and_times, email_address, email_password)

            if appointment_was_booked_flag == True:
                print("We're done here. An appointment has been booked. Let's shut it down")
                return 0

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

    return 0

# File Read In Parameters: [Wanted Days, Times];[Provider Details];email;password
dates_and_times_to_search_list, location_service_provider_list, email_address, email_password = ReadInParametersFile.mainBody()

#setting up a loop that will infinitely loop until something is booked
print("Starting up haircut program")
SendDiscordMessage.mainBody("Starting up haircut program")

#Will continue to loop through program until something happens
while 0!=1:

    #send a discord message in the morning to say it's still running
    if is_hour_between(datetime.time(22,3), datetime.time(22,15)):
        SendDiscordMessage.mainBody("Program is still running")


    print("Searching for date: ", dates_and_times_to_search_list)
    print("Executing Code & looping")

    returned_status = heart_of_the_operation(dates_and_times_to_search_list, location_service_provider_list, email_address, email_password)

    #OK, we're back after running through all that. Let's sleep for 10 minutes
    print("Sleeping for 10 minutes before searching again")
    time.sleep(600) #sleep for 10 minutes
