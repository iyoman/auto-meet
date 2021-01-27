import schedule
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.binary_location=r'[LOCATION OF vivaldi.exe]'
options.add_argument(r"user-data-dir=C:\dev-app2") # this is the directory for the desired user data to be used in the tab created
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1,
    "profile.default_content_setting_values.media_stream_mic":1,
    "profile.default_content_setting_values.media_stream_camera":1, 
    "profile.default_content_setting_values.geolocation":1
})
options.add_experimental_option("detach", True)
date = datetime.datetime.now()
day = date.strftime("%A")
print(date)
if day in ('Tuesday', 'Thursday'):
    day = 'x'
    print('X Day')
else:
    day = 'y'
    print('Y Day')

def login(driver, meetcode):
    driver.get("https://accounts.google.com/Login")
    time.sleep(1)
    if driver.current_url == "https://myaccount.google.com/?utm_source=sign_in_no_continue":
        print('Already Logged in...')
    else:
        driver.find_element_by_xpath("//input[@name='identifier']").send_keys("[EMAIL ADDRESS HERE]")
        time.sleep(1)
        #Next Button:
        driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
        time.sleep(1)
        #Password:
        driver.find_element_by_xpath("//input[@name='password']").send_keys("[PASSWORD HERE]")
        time.sleep(1)
        print('Logged in...')
        #next button:
        driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()
        time.sleep(1)
    #opening Meet:
    driver.get("https://meet.google.com")
    driver.refresh()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]").click()
    time.sleep(.5)
    driver.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input").send_keys(meetcode)
    time.sleep(.5)
    driver.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div/div[2]/span/div/div[4]/div[2]/div/span/span").click()
    time.sleep(3)
        # Turning off video 
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div").click()
    time.sleep(.5)
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div").click()
    time.sleep(.5)
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]").click()
    print("Joined")

def class1():
    if day == 'x':
        print('Entering Economics...')
        meetcode = "[FIRST CLASS MEETCODE]"
    else:
        print("Entering Spanish...")
        meetcode = "[FIRST CLASS MEETCODE]"
    driver = webdriver.Chrome(executable_path=r'C:\Users\isaac\chromedriver\chromedriver.exe', options=options)
    login(driver, meetcode)

def class2():
    if day == 'x':
        print('Entering Physics...')
        meetcode = "[SECOND CLASS MEETCODE]"
    else:
        print("Entering Math...")
        meetcode = "[SECOND CLASS MEETCODE]"
    driver = webdriver.Chrome(executable_path=r'C:\Users\isaac\chromedriver\chromedriver.exe', options=options)
    login(driver, meetcode)

def class3():
    if day == 'x':
        print('Entering Chamber...')
        meetcode = "[THIRD CLASS MEETCODE]"
    else:
        print("Entering English...")
        meetcode = "[THIRD CLASS MEETCODE]"
    driver = webdriver.Chrome(executable_path=r'C:\Users\isaac\chromedriver\chromedriver.exe', options=options)
    login(driver, meetcode)

def class4():
    if day == 'x':
        print('Entering History...')
        meetcode = "[FOURTH CLASS MEETCODE]"
    else:
        print("Entering Guitar...")
        meetcode = "[FOURTH CLASS MEETCODE]"
    driver = webdriver.Chrome(executable_path=r'C:\Users\isaac\chromedriver\chromedriver.exe', options=options)
    login(driver, meetcode)

if __name__ == "__main__":
    schedule.every().day.at("10:03").do(class1)
    schedule.every().day.at("11:05").do(class2)
    schedule.every().day.at("12:55").do(class3)
    schedule.every().day.at("14:00").do(class4)
    print("Running...")
    while True:
        schedule.run_pending()  # check if we need to run anything
        time.sleep(20) # wait 20 seconds before checking each time again
