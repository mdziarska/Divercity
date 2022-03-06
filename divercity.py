'''

This code includes automation tests for checking the possible broken links on the footer section using Python and Selenium
URL: http://develop.divercity.io/

Successful responses (200–299)
Redirection messages (300–399)
Client error responses (400–499)
Server error responses (500–599)
999 - request denied

'''

import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://develop.divercity.io/")
driver.maximize_window()
driver.implicitly_wait(10)
all_links = driver.find_elements(By.XPATH,"//footer//a")
for elem in all_links:
    print(elem.text,end=" ")
    link=str(elem.get_attribute('href'))
    if(link.startswith("http")):
        response = requests.get(link)
        print(link,response.status_code,end=" ")
        if(int(response.status_code)>299):
            print("link is broken")
    else:
        print("link is not proper ",link)
    print()


