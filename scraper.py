from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
import math


driver_path = "/home/saatvik/MetaMetaCritic/gecko_driver/geckodriver"

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--headless')

service = Service(driver_path)
driver = webdriver.Firefox(service=service, options=firefox_options)

url = 'https://www.metacritic.com/game/risk-of-rain-2/user-reviews/'
driver.get(url)

time.sleep(3)
reviews = driver.find_elements(By.CLASS_NAME, 'c-siteReview_quote')
frac_stats = driver.find_elements(By.CLASS_NAME,'c-scoreCount_count')

review_text_list = []
for review in reviews:
    review_text = review.find_element(By.TAG_NAME,'span').text
    review_text_list.append(review_text)
print(review_text_list)

frac_stats_dict = {"Positive":[0,0],"Mixed":[0,0],"Negative":[0,0]}
labels = ["Positive","Mixed","Negative"]
j = 0
for stats in frac_stats:
    spans = stats.find_elements(By.TAG_NAME,'span')
    i = 0
    for span in spans:
        frac_stats_dict[labels[j]][i] = span.text
        i += 1
    j += 1
print(frac_stats_dict)




driver.quit()