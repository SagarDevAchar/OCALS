"""
    OCALS: Online Class Automatic Login System
    ---------------------------------------------------------
    Copyright (c) 2020 Sagar Dev Achar
    Under MIT License
    ---------------------------------------------------------
    Completed on:   15 September 2020
                    05:03 PM

    Coded By:   Sagar Dev Achar
    ---------------------------------------------------------
    Description:
        Selenium + ChromeDriver based script which simulates
        a student's visit and actions on the Google Meet
        Web Application and automatically waits, enters and
        exits Google Meet classes on the basis of their
        start times. Works on the assumption that all
        classes have a duration of 1 hour
    ---------------------------------------------------------
    DO NOT TERMINATE THE AUTOMATED CHROME WINDOW OR THE
    APPLICATION WINDOW!
"""

# =============================== IMPORTS ===============================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException

import datetime as dt
import time
import sys
import msvcrt

# ======================== Custom Input Function =========================


def secure_password_input(prompt=''):
    p_s = ''
    proxy_string = [' '] * 64
    while True:
        sys.stdout.write('\x0D' + prompt + ''.join(proxy_string))
        c = msvcrt.getch()
        if c == b'\r':
            break
        elif c == b'\x08':
            p_s = p_s[:-1]
            proxy_string[len(p_s)] = " "
        else:
            proxy_string[len(p_s)] = "*"
            p_s += c.decode()

    sys.stdout.write('\n')
    return p_s


# ============================= Begin of CLI =============================
print("\nOCALS - Online Classes Auto-Login System")
print("By Sagar Dev Achar")
print("\nPLEASE DO NOT INTERFERE UNTIL IN A MEETING!")
print("DO NOT TERMINATE THE AUTOMATED CHROME WINDOW", end='\n\n')
print("-" * 75, end='\n\n')

print("DISCLAIMER: The following credentials will be kept private")

# -------------------------- Credential Inputs ---------------------------
USERNAME = input("\nG-Mail ID : ")
PASSWORD = secure_password_input("Password  : ")

# -------------------- WebDriver Initialization & Login ------------------
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 1,
                                          "profile.default_content_setting_values.media_stream_camera": 1,
                                          "profile.default_content_setting_values.notifications": 2})
chrome = webdriver.Chrome(executable_path="chromedriver.exe",
                          options=options)
chrome.maximize_window()

chrome.implicitly_wait(5)

chrome.get("https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687"
           "-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A"
           "%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16"
           "%3A221d2247cc1ebbf6%2C10%3A1599018953%2C16%3Aa885e0b78634aafb"
           "%2Cb210e8568e9afb8c24d187341cbc38a04d919f8365b4f479057ed2004d21eea2%22%2C%22cdl%22%3Anull%2C%22cid%22%3A"
           "%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22"
           "%2C%22ses%22%3A%221decfeaa153445929a9cb99e4b63e01f%22%7D&response_type=code&flowName=GeneralOAuthFlow")

print("\nLogging you in...", end='')

mail_input = chrome.find_element_by_id("identifierId")
mail_input.send_keys(USERNAME + "\n")

try:
    WebDriverWait(chrome, 10).until(expected_conditions.element_to_be_clickable((By.NAME, "password")))
except TimeoutException:
    print("\x0DLogin Error! Please check the Input Credentials!")
    print("\n" + "-" * 75, end='\n\n')

    chrome.quit()
    del USERNAME, PASSWORD

    input("Press ANY key to exit...")
    exit(0)

password_input = chrome.find_element_by_name("password")
password_input.send_keys(PASSWORD + "\n")

del USERNAME, PASSWORD

try:
    WebDriverWait(chrome, 10).until(lambda driver: "https://stackoverflow.com/" in driver.current_url)

    print('\x0DLogged in Successfully!')
except TimeoutException:
    print("\x0DLogin Error! Please check the Input Credentials!")
    print("\n" + "-" * 75, end='\n\n')

    chrome.quit()
    input("Press ANY key to exit...")
    exit(0)

# -------------------- Google Meet Navigation & Access -------------------


def pull_from_meet():   # Google Meet Reader and Filter Function
    current_time = dt.datetime.now()
    sessions = chrome.find_elements_by_class_name("wKIIs")
    events_return = []

    for session in sessions:
        session_info = session.text.split("\n")
        try:
            session_time = dt.datetime.strptime(session_info[0], "%I:%M %p").replace(year=current_time.year,
                                                                                     month=current_time.month,
                                                                                     day=current_time.day)
        except ValueError:
            session_time = dt.datetime.strptime(session_info[0], "%H:%M").replace(year=current_time.year,
                                                                                  month=current_time.month,
                                                                                  day=current_time.day)

        if (session_time + session_duration) > current_time:
            events_return.append([session_time,
                                  session_info[1],
                                  session])

    return events_return


chrome.get("https://meet.google.com/#")

print("\n" + "-" * 75, end='\n\n')

time_now = dt.datetime.now()
session_duration = dt.timedelta(minutes=14, seconds=45)     # <| </>

events = pull_from_meet()

if not events:
    print("No Classes Today! ENJOYYY!")
else:
    print("Upcoming / Ongoing Classes for Today:")
    print("- - - - - - - - - - - - - - - - - - -")
    for event in events:
        print(event[0].strftime("%I:%M %p"), end="    ")
        print(event[1])

    print("\n" + "-" * 75, end='\n\n')
    print("Action Log:", end='\n\n')

    events_for_the_day = len(events)

    for e in range(events_for_the_day):
        events = pull_from_meet()
        time_now = dt.datetime.now()
        if (events[0][0] - time_now).seconds < 60 or "\nNOW" in events[0][2].text.upper():
            print("Joining %s..." % events[0][1], end='')

            try:
                events[0][2].click()
            except StaleElementReferenceException:
                events = pull_from_meet()
                events[0][2].click()
        else:
            print("Waiting for %s to start... " % events[0][1], end='')
            time.sleep((events[0][0] - time_now).seconds)
            print("\x0DJoining Class: %s...       " % events[0][1], end='')

            try:
                events[0][2].click()
            except StaleElementReferenceException:
                events = pull_from_meet()
                events[0][2].click()

        button_array = chrome.find_element_by_class_name("EhAUAc")

        mute = button_array.find_element_by_class_name("ZB88ed")
        mute.click()

        vid = button_array.find_element_by_class_name("GOH7Zb")
        vid.click()

        join = chrome.find_element_by_xpath("//*[@id=\"yDmH0d\"]/c-wiz/div/div/div[5]/div[3]/div/div[2]/div/div/div["
                                            "2]/div/div[2]/div/div[1]/div[1]")
        try:
            join.click()
        except StaleElementReferenceException:
            join = chrome.find_element_by_xpath("//*[@id=\"yDmH0d\"]/c-wiz/div/div/div[5]/div[3]/div/div["
                                                "2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]")
            join.click()

        print("\x0DIn class: %s...            " % events[0][1], end='')

        time.sleep((events[0][0] + session_duration - time_now).seconds)

        hang_up = chrome.find_element_by_xpath("//*[@id=\"ow3\"]/div[1]/div/div[5]/div[3]/div[9]/div[2]/div[2]/div")
        try:
            hang_up.click()
        except StaleElementReferenceException:
            hang_up = chrome.find_element_by_xpath("//*[@id=\"ow3\"]/div[1]/div/div[5]/div[3]/div[9]/div[2]/div[2]/div")
            hang_up.click()

        print("\x0DDone with %s!              " % events[0][1])

        chrome.get("https://meet.google.com/#")

print("\n" + "-" * 75, end='\n\n')

chrome.quit()
input("Press ANY key to exit...")
