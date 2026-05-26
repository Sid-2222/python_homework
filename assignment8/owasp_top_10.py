from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
import csv
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')

url = "https://owasp.org/Top10/2025/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    
    driver.get(url)
    time.sleep(5)
    heading = driver.find_element(By.ID,"top-102025-list")
    #print(heading.text)
    top_ten = heading.find_element(By.XPATH,"following-sibling::ol[1]")
   # print(top_ten.text)
    list_items = top_ten.find_elements(By.TAG_NAME, "li")
    list = []
    
    for item in list_items:
        title = item.text
        link = item.find_element(By.TAG_NAME, "a")
        href = link.get_attribute("href")
        list.append({
            "title": title,
            "href": href
        })
    
    df= pd.DataFrame(list)
    #print(list)
    df.to_csv("assignment8/owasp_top_10.csv", index=False)    
    
    input("Press Enter to close browser...") 
except Exception as e:
    print("couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")

finally:
    driver.quit()