** Automation with Selenium: **
* youtube.py and login.py were created to test how selenium could be used.
* youtube.py needs an input of the channel for which you need to play the latest video
* login.py has code to enter login information for datacamp.com website

** Data injestion using API and Selenium folder content **
1. APICalls.py is used to see how API calls can be done and how data can be saved in an object
2. crawler.py was written to test how Selenium crawler can be written for spotify website
3. scraper.py is a code to get data from all countries where Spotify is used. This data is stored in result.csv file. 
The idea here is to extract cost data, convert it to USD and compare pricing all over the world. Other data analysis could also be done.
Code is written in OOPS using python packages urllib, BeautifulSoup. 

NOTE: scraper could not be written in Selenium because the website detected my bot and execution is interrupted. Hence, webpage scrapping using BeautifulSoup
