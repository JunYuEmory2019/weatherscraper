# Weather Scraper
This is a Scrapy project to scrape weather data from a government weather site (https://www.weather.gov/)

This project is meant to help us learn how to scrape webs but also gather relevant data for the upcoming week.


## Beginning installations
Run the following commands in Terminal window:

    $ pip install scrapy

    $ pip install matplotlib


## Extracted data

This project extracts weather temperature, chances of rain, days, and the highs and lows of each days.
The extracted data looks like this sample:

    {
              'day': weather.css("p.period-name::text").get(),
              'desc': weather.css("p.short-desc::text").get(),
              'temp': weather.css("p.temp::text").get()
    }


## Spiders

This project contains one spider named `weather` and it employs CSS selectors,
rather than XPath expressions.

You can learn more about the spiders by going through the
[Scrapy Tutorial](http://doc.scrapy.org/en/latest/intro/tutorial.html).


## Running the spider

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl weather

If you want to save the scraped data to a file, you can pass the `-o` option:

    $ scrapy crawl weather -o INPUTNAME.json

"INPUTNAME" can be replaced with any file name.

Then input the zip code as a 6 digit number, with no spaces, such as:

    30322


## Running the visualization

This project contains a file named `plot.py` which analyzes and plots the
high and low temperatures of the weather data from the JSON file.

Run the file with the `python` command, such as:

    $ python plot.py

Then input the file name with ".json" at the end, and no spaces, such as:

    INPUTNAME.json

The figure will be automatically saved as INPUTNAME.png.
