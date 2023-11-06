import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import colorama
from colorama import Fore
colorama.init()
from time import sleep

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.add_argument('proxy-server=106.122.8.54:3128')
    options.add_argument('--headless')
    options.add_argument(r'--user-data-dir=C:\Users\saidl\AppData\Local\Google\Chrome\User Data\Default')

    browser = uc.Chrome(
options=options,
    )
browser.get("https://www.udemy.com")