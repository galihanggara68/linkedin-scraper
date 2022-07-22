# LinkedIn Scraper

## Intro

This package is using [`Selenium Finder`](https://github.com/galihanggara68/selenium-finder) library as engine for scrape datas from LinkedIn webpage(Pre Login)

## Usage

### Clone or Install from pip

Clone this repo to your current directory

> git clone https://github.com/galihanggara68/linkedin-scraper.git

or install using pip

> pip3 install git+https://github.com/galihanggara68/linkedin-scraper.git@master

### Import library

First of all import LinkedIn class

```
from LinkedIn_Scraper.linkedin import LinkedInScraper
```

### Using Finder class

`LinkedIn` class has 3 parameters `driver` the Selenium WebDriver, `finder` a Finder object, and `cookie_path` a path of cookie json for login to LinkedIn

```
from selenium import webdriver

driver = webdriver.Chrome()

# global_wait default 10 second
# iterable_each_wait default 1 second
options = {"global_wait": 10, "iterable_each_wait": 2}
finder = Finder(driver, options)

# create LinkedInScraper instance
ld = LinkedInScraper(driver, finder, "www.linkedin.com.cookies.json")

# start scraping
ld.exec_scraper("Galih Anggara")

# get the result
print(ld.get_data())

```

## LinkedInScraper methods

### exec_scraper(username)

execute scraper with `username` parameter(the username to search for)

### get_data()

get scraped result
