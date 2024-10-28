from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
import math

driver_path = "gecko_driver/geckodriver"

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--headless')

service = Service(driver_path)
driver = webdriver.Firefox(service=service, options=firefox_options)
game_name = input("Please enter the name of a game: ")
game_name = '-'.join(game_name.split())

url = 'https://www.metacritic.com/game/'+ game_name + '/user-reviews/'
print(url)
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


# Use LLM to also see if the reviews blame the company or not
# First gather aspects using keyword extraction, then use ABSA on the aspects to get scores, anything with a positive score above a certain value is a pro

# main_page= 'https://www.metacritic.com/game/'+ game_name
# driver.get(main_page)
# time.sleep(3)

# names = {"Devs":"","Pubs":""}
# devs = driver.find_element(By.CLASS_NAME,'c-gameDetails_Developer')
# pubs = driver.find_element(By.CLASS_NAME,'c-gameDetails_Distributor')
# date = driver.find_element(By.CLASS_NAME,'c-gameDetails_ReleaseDate')

# names["Devs"] = devs.text[devs.text.index("\n")+1::]
# names["Pubs"] = pubs.text[pubs.text.index("\n")+1::]
# date = date.text()
# print(date) # Add more logic here to check if the game is x+ years old

# reddit_url = "https://www.reddit.com/search/?q=" + '+'.join(names["Devs"].split())
# driver.get(reddit_url)
# titles = driver.find_elements(By.TAG_NAME,'a')

# title_list = []

# for title in titles:
#     title_list.append(title.text)
# print(title_list)

driver.quit()