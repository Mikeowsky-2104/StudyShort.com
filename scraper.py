from selenium import webdriver
from selenium.webdriver.common.by import by
from selenium.webdriver.chrome.service import Service
import csv
import time

page_to_scrape = wevdriver.Chrome(service=browser_driver)
page_to_scrape.get("https://quotes.toscrape.com/").text

page_to_scrape.find_element(By.LINK_TEXT, "Login").click()
