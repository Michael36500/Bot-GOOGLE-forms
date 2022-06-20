import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def input_text(driver, where, what, delay = 0.001):
    # global driver
    # where = xpath
    #what = string
    textfield = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, where)))
    for a in what:
        textfield.send_keys(a)
        time.sleep(delay)