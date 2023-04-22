import ScrapeWebPage
import SendDiscordMessage

from bs4 import BeautifulSoup

#Importing packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #EC = Expected Condition we'll be looking for on the page

import random
import time

def click_a_time_button(each_url,time_to_book, email_address, email_password):

    # Set up the webdriver
    driver = webdriver.Chrome('/path/to/chromedriver')

    # Load the webpage
    driver.get(each_url)

    # Use Beautiful Soup to parse the webpage
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Wait for a random period of time between 5 to 15 seconds
    waiting_time = random.randint(5, 15)
    time.sleep(waiting_time)

    # Find the button with the text "3:30 pm"
#    button = soup.find('button', text=time_to_book)

    print("time_to_book: ")
    print(time_to_book)

    # # Click the button with the specific time
    for button in WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//button[text()='" + time_to_book + "']"))):
        button.click()

    #button was clicked, need to log in for my username

    # https://stackoverflow.com/questions/69875125/find-element-by-commands-are-deprecated-in-selenium
    # For depreciated find_element*
    print("Email: " + email_address)

    email_field = driver.find_element(By.ID, "email-field")
    email_field.send_keys(email_address)

    print("Password: " + email_password)
    password_field = driver.find_element(By.ID, "password-field")
    password_field.send_keys(email_password)

    #    sign_in_button = driver.find_element_by_id('signin-button') #This is depreciated, see the method below
    sign_in_button = driver.find_element(By.ID, "signin-button")
    sign_in_button.click()

    time.sleep(15)


    print("A haircut is one step away from being booked")

    # #Click CONTINUE button to confirm haircut
    # for button in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//button[text()='Continue']"))):
    #     button.click()

    time.sleep(15)

    # now that we're signed in and have clicked the "accept button", make sure we're seeing the "THANKS! YOU'RE ALL BOOKED." message
    # Use Beautiful Soup to parse the webpage
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    if soup.findAll(text="THANKS! YOU'RE ALL BOOKED."):
        print("it was booked!!!")
        SendDiscordMessage.mainBody("An appointment was booked for a haircut!")
        appointment_was_booked_flag = True
    else:
        print("something is wrong, it was not booked")
        SendDiscordMessage.mainBody("An attempt was made to book an appointment was booked for a haircut! However, something has gone wrong.")
        appointment_was_booked_flag = False

    # # Close the webdriver
    driver.quit()

    return appointment_was_booked_flag

def matched_items_between_lists(first_list_of_items, second_list_of_items):
    matches = [i for i in first_list_of_items if i in second_list_of_items]

    print("first_list_of_items")
    print(first_list_of_items)

    print("second_list_of_items")
    print(second_list_of_items)

    # print("Checking types")
    # for each_item in first_list_of_items:
    #     print(type(each_item))
    #
    # for each_item in second_list_of_items:
    #     print(type(each_item))


    print("matches")
    print(matches)

    return matches
def check_page_source_for_wanted_times(page_source_of_wanted_date):
    list_of_times_available = []


    soup_of_page_source_for_url = BeautifulSoup(page_source_of_wanted_date, 'lxml')

    button_list = soup_of_page_source_for_url.find_all('button', {
        'class': 'service-availability-select-or-call-button custom-color-bg custom-color-border-color btn btn-block btn-primary ember-view'})

    for each_button in button_list:
        #        print("Button content: ")
        #        print(each_button.text)
        button_text_with_newline_characters_still_in_it = each_button.text

        # removing characters: https://www.journaldev.com/23763/python-remove-spaces-from-string#:~:text=Python%20String%20strip()%20function%20will%20remove%20leading%20and%20trailing%20whitespaces.&text=If%20you%20want%20to%20remove,or%20rstrip()%20function%20instead.
        button_text_with_newline_characters_removed = button_text_with_newline_characters_still_in_it.replace("\n", "")
        button_text_with_leading_trailing_spaces_removed = button_text_with_newline_characters_removed.strip()

        list_of_times_available.append(button_text_with_leading_trailing_spaces_removed)



    return list_of_times_available

def mainBody(wanted_date_url_to_book_list,date_matched_and_times, email_address, email_password):

    print("Attempting to book appointment with following day and times: ")
    print(date_matched_and_times)

    # index 0 is the date, don't need that at this point
    times_to_check = []

    date_matched_and_times.pop(0)

    print("date_matched_and_times: ")
    print(date_matched_and_times)

    print("wanted_date_url_to_book_list")
    print(wanted_date_url_to_book_list)
    print(type(wanted_date_url_to_book_list))

    for each_url in wanted_date_url_to_book_list:
        page_source_of_wanted_date = ScrapeWebPage.mainBody(each_url)

        list_of_times_available = check_page_source_for_wanted_times(page_source_of_wanted_date)

        print("list_of_times_available")
        print(list_of_times_available)

        matched_times = matched_items_between_lists(date_matched_and_times, list_of_times_available)

        print("matched_times:")
        print(matched_times)

        #If the list of matched times isn't empty, attempt to book whatever is first in the list!
        if matched_times !=[]:
            SendDiscordMessage.mainBody("Haircut: Matched date and time. Attempting to book")
            appointment_was_booked_flag = click_a_time_button(each_url,matched_times[0], email_address, email_password)

    return appointment_was_booked_flag