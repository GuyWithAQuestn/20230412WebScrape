from datetime import date, timedelta, datetime

def get_list_of_wanted_dates_extracted_from(dates_and_times_to_search_list):

    list_of_wanted_dates = []

    for each_group_of_date_and_times in dates_and_times_to_search_list:

        each_group_of_date_and_times_as_list = each_group_of_date_and_times.split(",")
        wanted_date_only = each_group_of_date_and_times_as_list[0]
        list_of_wanted_dates.append(wanted_date_only)

    return list_of_wanted_dates


def check_If_Available_Dates_After_Wanted_Date(next_hair_cut_date, list_of_dates_available):
    # Checks if any available dates are equal or after wanted date
    available_dates_after_wanted_date = False
    next_haircut_date_object = datetime.strptime(next_hair_cut_date, '%Y-%m-%d').date()

    for each_available_date in list_of_dates_available:
        available_date = datetime.strptime(each_available_date, '%Y-%m-%d').date()
        if available_date < next_haircut_date_object:
            pass
        else:
            available_dates_after_wanted_date = True  # A date is equal or past wanted date

    return available_dates_after_wanted_date


def check_If_Available_Dates_During_Week_Of_Wanted_Date(list_of_wanted_dates, list_of_dates_available):
    # Checks if any available dates are during the same week of wanted date
    # list of wanted dates --> a list of the dates that will we will then search for the days in that week Sunday_thru_Saturday_dates
    # list_of_dates_available --> list of dates can currently be scheduled

    available_dates_during_week_of_wanted_date_flag = False
    complete_list_of_Sun_thru_Sat_dates_to_check = []

    print("list_of_wanted_dates")
    print(list_of_wanted_dates)

    for each_wanted_haircut_date in list_of_wanted_dates:
        # get the days of that week:
        Sunday_thru_Saturday_dates = get_days_of_week_for_day_in_question(each_wanted_haircut_date)

        # for each_day in Sunday_thru_Saturday_dates:
        #     complete_list_of_Sun_thru_Sat_dates_to_check.append(each_day)

        # now check for any commonalies between the lists
        for each_weekday_of_wanted_days_week in Sunday_thru_Saturday_dates:

            # print("Comparing: ")
            # print(each_weekday_of_wanted_days_week)
            # print(type(each_weekday_of_wanted_days_week))
            # print(list_of_dates_available)
            # for each_of_them in list_of_dates_available:
            #     print(type(datetime.strptime(each_of_them, '%Y-%m-%d')))

            # Currently, the each_weekday_of_wanted_days_week is a date object
            # while Sunday_thru_Saturday_dates is a list of strings
            # convert the each_weekday_of_wanted_days_week to a string for comparisson

            each_weekday_of_wanted_days_week_str = each_weekday_of_wanted_days_week.strftime('%Y-%m-%d')


            # each_weekday_of_wanted_days_week_dateobj = datetime.strptime(each_weekday_of_wanted_days_week, '%Y-%m-%d')

            if each_weekday_of_wanted_days_week_str in list_of_dates_available:
                print("Found a match of the days of the week with available dates!!")
                available_dates_during_week_of_wanted_date_flag = True
            else:
                print("No matches were found in the list of available dates")

    return available_dates_during_week_of_wanted_date_flag


def get_days_of_week_for_day_in_question(date_in_question_str):
    Sunday_through_Saturday = []
    # convert string to date
    date_in_question = datetime.strptime(date_in_question_str, '%Y-%m-%d').date()

    sunday_of_week = date_in_question - timedelta(days=date_in_question.isoweekday() % 7)
    monday_of_week = (date_in_question - timedelta(days=date_in_question.isoweekday() % 7)) + timedelta(days=1)
    tuesday_of_week = (date_in_question - timedelta(days=date_in_question.isoweekday() % 7)) + timedelta(days=2)
    wednesday_of_week = (date_in_question - timedelta(days=date_in_question.isoweekday() % 7)) + timedelta(days=3)
    thursday_of_week = (date_in_question - timedelta(days=date_in_question.isoweekday() % 7)) + timedelta(days=4)
    friday_of_week = (date_in_question - timedelta(days=date_in_question.isoweekday() % 7)) + timedelta(days=5)
    saturday_of_week = (date_in_question - timedelta(days=date_in_question.isoweekday() % 7)) + timedelta(days=6)

    Sunday_through_Saturday.append(sunday_of_week)
    Sunday_through_Saturday.append(monday_of_week)
    Sunday_through_Saturday.append(tuesday_of_week)
    Sunday_through_Saturday.append(wednesday_of_week)
    Sunday_through_Saturday.append(thursday_of_week)
    Sunday_through_Saturday.append(friday_of_week)
    Sunday_through_Saturday.append(saturday_of_week)

    print("Sunday_through_Saturday")
    print(Sunday_through_Saturday)

    return Sunday_through_Saturday

def mainBody(dates_and_times_to_search_list,list_of_dates_available):

    list_of_wanted_dates = get_list_of_wanted_dates_extracted_from(dates_and_times_to_search_list)


    dates_that_week_flag = check_If_Available_Dates_During_Week_Of_Wanted_Date(list_of_wanted_dates,list_of_dates_available)

    # list_of_wanted_dates_and_times = []
    # list_of_wanted_dates_and_times = dates_and_times_to_search.split("|")

    #     list_of_dates_and_times = dates_and_times_to_search.split("|")
    #
    #     for each_date in list_of_dates_and_times:
    #         list_of_specific_dates = each_date[0]

    return dates_that_week_flag