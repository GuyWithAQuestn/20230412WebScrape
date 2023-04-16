def search_for_matching_date(dates_and_times_to_search_list,list_of_dates_available):

    print("This is what made it in: ")
    print(dates_and_times_to_search_list)
    print(list_of_dates_available)


    exact_matched_date_found = False
    each_wanted_date_time = "0000-00-00"
    # each_wanted_date_time = dates_and_times_to_search_list.split("|")

    for each_group_of_date_and_times in dates_and_times_to_search_list:

        print("each_group_of_date_and_times is of type: ")
        print(type(each_group_of_date_and_times))

        each_group_of_date_and_times_as_list = each_group_of_date_and_times.split(",")
        wanted_date_only = each_group_of_date_and_times_as_list[0]
        for each_available_date in list_of_dates_available:
            print("Comparing The Values: ")
            print(wanted_date_only)
            print(each_available_date)
            if wanted_date_only == each_available_date:
                print("Matching Date Found")
                exact_matched_date_found = True
                return exact_matched_date_found, each_group_of_date_and_times


    # if made it back here, there was no matching date
    return exact_matched_date_found, each_wanted_date_time

def mainBody(dates_and_times_to_search_list,list_of_dates_available):
    date_was_matched_flag = False

    date_was_matched_flag, dates_and_times = search_for_matching_date(dates_and_times_to_search_list,list_of_dates_available)

    # list_of_wanted_dates_and_times = []
    # list_of_wanted_dates_and_times = dates_and_times_to_search.split("|")

    #     list_of_dates_and_times = dates_and_times_to_search.split("|")
    #
    #     for each_date in list_of_dates_and_times:
    #         list_of_specific_dates = each_date[0]

    return date_was_matched_flag, dates_and_times