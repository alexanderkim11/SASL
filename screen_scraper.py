from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

PATH = r"C:\Users\Alex Kim\Documents\SASL\chromedriver.exe"


username = input("Username: ")
password = input("Password: ")
team_id = input("Team ID: ")

link = "https://football.instatscout.com/teams/" + team_id
driver = webdriver.Chrome(PATH)
driver.get(link)

#UVA team id = 20337

try:
    email = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email.send_keys(username)

    passw = driver.find_element_by_name("pass")
    passw.send_keys(password)

    login_button = driver.find_element_by_name("commit")
    login_button.click()

except:
    print("Login Error")

# Add code to pull data from website and insert into spreadsheet or something?
    #What data to insert?
    #Where to send data? (i.e. Excel, Google Sheets, etc?)