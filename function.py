import time

#Import third part modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import def_input_text
import def_send_form


#YOU NEED TO SET THE CHROME DRIVER PATH
CHROME_DRIVER_PATH = "c:/Users/ambro/webdrivers/chromedriver.exe"


def funukce(iteration):
    # imgType = styl obrázku (steampunk, synthwave,...)


    #Add headless option
    browserOptions = Options()
    browserOptions.add_argument("--headless")

    #Create driver
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH,options=browserOptions)
    driver.get("https://forms.gle/vgyhdoJgG8ZG76iY8")

    #Type the text
    def_input_text.input_text(driver, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input", "I suck at programming")

    # send the form
    def_send_form.send_form(driver, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")

    # #Select the img type to generate
    # # imgTypeBox = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,f'{XPATH_IMG_TYPE} and @alt="{imgType}"]')))
    # # imgTypeBox.click()
    # #Click on the "Create" button
    # btnGenerate = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,XPATH_GENERETE)))
    # btnGenerate.click()

    # time.sleep(1)

    # #Click on the "Create" button
    # btnGenerate = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,XPATH_BTN_GENERATE)))
    # btnGenerate.click()

    # #Type the text
    # textfield = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH ,XPATH_NAME_TEXT)))
    # textfield.send_keys(inputText)

    # #Click on the "Save" button
    # btnGenerate = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,XPATH_SAVE)))
    # btnGenerate.click()
    
    # time.sleep(5)

    
# funukce()