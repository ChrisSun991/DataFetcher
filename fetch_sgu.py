from selenium import webdriver
import pandas as pd
import numpy as np


def fetch() -> bool:
    try:
        # Download chromedriver before running the code: https://chromedriver.chromium.org/downloads
        driver = webdriver.Chrome("/Users/Chris/chromedriver")
        driver.get("https://www.sgx.com/derivatives/negotiated-large-trade-nlt?cc=Fef&category=futures")
        title = driver.find_element_by_xpath(
            '//*[@id="page-container"]/template-base/div/div/sgx-widgets-wrapper/widget-derivatives-nlt/section[1]/div[1]/sgx-table/sgx-table-toolbar/div[2]/span')
        title.click()
        driver.close()
        return True
    except Exception as e1:
        print(e1)
        print("Download the appropriate Chrome Driver for your device: https://chromedriver.chromium.org/downloads")
        print("If version not shown, remove try except and run the code again")
        return False