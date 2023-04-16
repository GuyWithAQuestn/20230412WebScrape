def open_and_read_file():
    # Going to bypass the inputs, and get inputs from the file instead
    FileParametersReadIn = open("ScrapeParameters.txt", "r")
    collected_data_as_string = FileParametersReadIn.readlines()
    FileParametersReadIn.close()
    print("Here's what I read in: ", collected_data_as_string)
    collected_data_as_list = collected_data_as_string[0].split(";")

    dates_and_times_to_search = str(collected_data_as_list[0])
    dates_and_times_to_search_list = dates_and_times_to_search.split("|")

    location_service_provider = str(collected_data_as_list[1])
    location_service_provider_list = location_service_provider.split("|")

    email_address = str(collected_data_as_list[2])
    email_password = str(collected_data_as_list[3])

    #    which_bundled_preferences = str(collected_data_as_list[1]).strip('\n')
    # had to add in the above .strip('\n') as a newline character was coming along with the last variable there and messing things up

    return dates_and_times_to_search_list, location_service_provider_list, email_address, email_password


def mainBody():
    dates_and_times_to_search_list, location_service_provider_list, email_address, email_password = open_and_read_file()
    return dates_and_times_to_search_list, location_service_provider_list, email_address, email_password
