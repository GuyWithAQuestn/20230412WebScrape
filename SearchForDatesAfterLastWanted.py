from datetime import date, timedelta, datetime

def get_list_of_wanted_dates_extracted_from(dates_and_times_to_search_list):

    list_of_wanted_dates = []

    for each_group_of_date_and_times in dates_and_times_to_search_list:

        each_group_of_date_and_times_as_list = each_group_of_date_and_times.split(",")
        wanted_date_only = each_group_of_date_and_times_as_list[0]
        list_of_wanted_dates.append(wanted_date_only)

    return list_of_wanted_dates

def get_wanted_dates_with_latest_date(list_of_wanted_dates):

    list_of_wanted_dates_dateobj = []
    latest_date_dateobj = date.today()

    print("All the wanted dates: ")
    print(list_of_wanted_dates)
    # print("The Latest Date of the following")

    for each_date in list_of_wanted_dates:
        print("each dates: ")
        print(each_date)
        print(type(each_date))

        list_of_wanted_dates_dateobj.append(datetime.strptime(each_date, '%Y-%m-%d').date())

    #loop through the dates and assign the latest date to latest_date_dateobj
    for each_date_dateobj in list_of_wanted_dates_dateobj:
        if each_date_dateobj > latest_date_dateobj:
            latest_date_dateobj = each_date_dateobj


    print("latest_date_dateobj")
    print(latest_date_dateobj)

    return latest_date_dateobj

def check_If_Available_Dates_later_than_wanted_date(latest_wanted_date,list_of_dates_available):

    list_of_available_dates_dateobj = []
    dates_available_after_wanted_dates = False

    for each_date in list_of_dates_available:
        list_of_available_dates_dateobj.append(datetime.strptime(each_date, '%Y-%m-%d').date())

    #loop through the dates and assign the latest date to latest_date_dateobj
    for each_date_dateobj in list_of_available_dates_dateobj:
        if each_date_dateobj > latest_wanted_date:
            dates_available_after_wanted_dates = True

    return dates_available_after_wanted_dates

def mainBody(dates_and_times_to_search_list,list_of_dates_available):

    list_of_wanted_dates = get_list_of_wanted_dates_extracted_from(dates_and_times_to_search_list)

    latest_wanted_date = get_wanted_dates_with_latest_date(list_of_wanted_dates)

    dates_that_week_flag = check_If_Available_Dates_later_than_wanted_date(latest_wanted_date,list_of_dates_available)

    # list_of_wanted_dates_and_times = []
    # list_of_wanted_dates_and_times = dates_and_times_to_search.split("|")

    #     list_of_dates_and_times = dates_and_times_to_search.split("|")
    #
    #     for each_date in list_of_dates_and_times:
    #         list_of_specific_dates = each_date[0]

    return dates_that_week_flag