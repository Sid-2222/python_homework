from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
import json
import csv
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))#,options=options
results = []
try:
    driver.get(url)
    time.sleep(10)
    search_results = driver.find_elements(By.CSS_SELECTOR,"li.cp-search-result-item")
   # print("result num:", len(search_results))
    for item in search_results:
        title = item.find_element(By.CLASS_NAME,"title-content").text
        author_elements = item.find_elements(By.CLASS_NAME,"author-link")
        authors = []
        for a in author_elements:
            authors.append(a.text)
        author_text = "; ".join(authors)
        
        try:
            format_year = item.find_element(By.CLASS_NAME,"display-info-primary").text
            
        except:
            format_year = "Not Available"
      
        book_dict = {
            "Title": title,
            "Author": author_text,
            "Format-Year": format_year
        }
        
        results.append(book_dict)
    
    df = pd.DataFrame(results)
    print(df)
    df.to_csv("assignment8/get_books.csv", index=False)
    df.to_json("assignment8/get_books.json", orient='records', indent=4)

        #
        # result_dict = {}
        # try:
        #     title = item.find_element(By.CLASS_NAME,"title-content").text
        #     result_dict["title"] = title
        # except:
        #     result_dict["title"] = "No title"
            
        # results.append(result_dict)
   # for r in results:
      #  print(r)

    # all_li = driver.find_elements(By.TAG_NAME, "li")
    # for li in all_li:
    #     results_ul = li.find_elements(By.CSS_SELECTOR, "ul.results")
    #     for ul in results_ul:
    #         items = ul.find_elements(By.CSS_SELECTOR, "li[data-test-id='searchResultItem']")
    #         for item in items:
    #             titles = item.find_elements(By.CLASS_NAME, "title-content")
    #             for t in titles:
    #                 print(t.text)
    
    
     
    input("Press Enter to close browser...")
except Exception as e:
    print("couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")

finally:
    driver.quit()
