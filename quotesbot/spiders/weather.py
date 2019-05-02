import scrapy
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import matplotlib.pyplot as plt
import json

class ToScrapeCSSSpider(scrapy.Spider):
    name = "weather"
    print('Enter zipcode:')
    zipcode = input()
    url = 'https://www.weather.gov/'
    driver = webdriver.Chrome()
    driver.get(url)

    search_box = driver.find_element_by_id('inputstring') # find search box on page
    search_box.clear() # clear search box
    search_box.send_keys(zipcode) # type zipcode into search box
    time.sleep(1) # pause for 1 sec to let search options come up
    search_box.send_keys(u'\ue007') # enter to auto-complete first option
    search_box.send_keys(u'\ue007') # enter to search

    time.sleep(5) # pause for 5 sec to let the page come up

    locationurl = driver.current_url # get current url to scrape weather

    # use current url for spider scraping
    start_urls = [
        locationurl
    ]

    time.sleep(5) # pause for 5 sec to let the page come up
    print('Begin scraping data...')

    #  scraping code:
    def parse(self, response):
        for weather in response.css("div.tombstone-container"):
            yield {
                'day': weather.css("p.period-name::text").get(),
                'desc': weather.css("p.short-desc::text").get(),
                'temp': weather.css("p.temp::text").get()
            }
