import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
    return credentials

def test_VWO_login():
    file_path= os.getcwd()
    full_file_path = file_path + "/Untitled spreadsheet.xlsx"
    credentials = read_credentials_from_excel(full_file_path)

    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username,password)
        VWO_login(username,password)


def VWO_login(username,password):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    email_input = driver.find_element(By.XPATH, "//input[@data-qa='hocewoqisi']")
    password_input = driver.find_element(By.XPATH, "//input[@id='login-password']")
    submit_button = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")

    email_input.send_keys(username)
    password_input.send_keys(password)

    submit_button.click()

    time.sleep(6)
    driver.quit()