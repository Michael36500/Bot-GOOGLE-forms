import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def send_form(driver, where):
    button = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, where)))
    button.click()
