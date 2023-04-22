from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

from bs4 import BeautifulSoup

import SendDiscordMessage

# Define the URL you want to scrape
# url = 'https://www.bestbuy.com/site/wd-easystore-18tb-external-usb-3-0-hard-drive-black/6427995.p?skuId=6427995'
# url = 'https://www.bestbuy.com/site/pny-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-with-dual-fan-black/6519166.p?skuId=6519166'
url = 'https://httpbin.org/headers'
# url = 'https://go.booker.com/location/nhills/service/2705223/Short%20Cut%20/select-date/provider/1082020'
# url = "https://whatismyipaddress.com/"

# Generate a random user agent header using fake_useragent library
ua = UserAgent()
headers = {'User-Agent': ua.random}

# Define the proxy you want to use
proxy = 'http://p.webshare.io:9999'


def check_webpage_source_for_security_block(webpage_source, security_block):

    soup = BeautifulSoup(webpage_source, 'html.parser')
    if soup.findAll(text="Security Block!"):
        print("Found a security block page. We can't move on yet and will need to search it again")
    else:
        security_block = False

    return security_block

def scrape_web_page(url):
    # Set up the Selenium driver with the proxy and headers
    options = Options()
    #    options.add_argument('--proxy-server={}'.format(proxy))  # Comment in/out for use of proxy
#    options.add_argument('user-agent={}'.format(headers['User-Agent']))  # Comment in/ out for change of headers
    # options.add_argument('user-agent={}'.format(headers))
    driver = webdriver.Chrome(options=options)

    # Navigate to the URL
    driver.get(url)

    # Wait for the class to become available on the page
    try:
        #    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='my-button']")))
        element = WebDriverWait(driver, 10).until(
            # EC.presence_of_element_located((By.CLASS, "power-calendar-container")))
            # element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ember64")))
        #    for button in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//button[text()='"+ first_time_from_list +"']"))):
        #        button.click()
        print("Found The Class I was Waiting For!")
        # button.click()
    except Exception as e:
        print("Class is not available on the page")
        #    print(e)

    # # Wait for the button to become available on the page
    # try:
    #     #    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='my-button']")))
    #     button = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//button[text()='" + "Add to Cart" + "']")))
    #     #    for button in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//button[text()='"+ first_time_from_list +"']"))):
    #     #        button.click()
    #     print("Buy Button is available!")
    #     button.click()
    # except Exception as e:
    #     print("Buy Button is not available on the page")
    #     #    print(e)
    #
    # # Wait for the button to become available on the page
    # try:
    #     #    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='my-button']")))
    #     button = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//button[text()='" + "Sold Out" + "']")))
    #     #    for button in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//button[text()='"+ first_time_from_list +"']"))):
    #     #        button.click()
    #     print("Sold Out!")
    #     button.click()
    # except Exception as e:
    #     print("Sold Out Button is not available on the page")

    # Get the page content
    page_content = driver.page_source



    # Print the page content
    # print(page_content)

    # Get the page content
    # page_content = driver.execute_script("return document.documentElement.outerHTML")
    # # Save the page content to a file
    # with open('/Users/bryan/Downloads/output.html', 'w', encoding='utf-8') as f:
    #     f.write(page_content)

    # Close the driver
    driver.quit()

    return page_content


def mainBody(received_url):

    security_block = True
    number_of_times_security_block_comes_up = 0

    while security_block == True:

        webpage_source = scrape_web_page(received_url)
        security_block = check_webpage_source_for_security_block(webpage_source, security_block)

        if security_block == True:
            #security page detected, wait 5 min before trying again
            number_of_times_security_block_comes_up = number_of_times_security_block_comes_up + 1
            if number_of_times_security_block_comes_up > 5:
                SendDiscordMessage.mainBody("A security page has come up 5 time in a row")
                number_of_times_security_block_comes_up = 0
            time.sleep(300)
        else:
            print("moving on, no security page")
            number_of_times_security_block_comes_up = 0


    return webpage_source


