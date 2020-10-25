from selenium import webdriver

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def crawl(self):
        i = 1
        market = "https://www.spotify.com/us/select-your-market/"
        self.driver.get(market)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/ul/li[" + str(i) + "]/a/div/div[2]").click()
        self.driver.find_element_by_xpath("/html/body/div[2]/div/header/div/nav/ul/li[1]").click()
        print(f"on {i}")
        inner_html = self.driver.find_element_by_xpath('//*[@id="HERO-0"]/article/header/div/div[2]/h2').get_attribute(
            "innerHTML")
        print(inner_html)

#        inner_html = self.driver.find_element_by_xpath('//*[@id="HERO-0"]/article/header/div/div[2]/h2').get_attribute("innerHTML")
 #       print(inner_html)

bot = Bot()
bot.crawl()