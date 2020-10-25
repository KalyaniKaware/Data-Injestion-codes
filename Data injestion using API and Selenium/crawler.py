from selenium import webdriver

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def crawl(self):
        market = "https://www.spotify.com/us/select-your-market/"
        self.driver.get(market)
        i = 1
        while True:
            try:
                self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/ul/li[" + str(i) + "]/a/div/div[2]").click()
                self.driver.find_element_by_xpath("/html/body/div[2]/div/header/div/nav/ul/li[1]").click()
                print(f"on {i}")
                inner_html = self.driver.find_element_by_xpath('//*[@id="HERO-0"]/article/header/div/div[2]/h2').get_attribute("innerHTML")
                print(inner_html)
                self.driver.back()
                self.driver.back()
                i+=1
            except:
                print(f"Checked {i - 1} elements")
                break
            else:
                pass

#        inner_html = self.driver.find_element_by_xpath('//*[@id="HERO-0"]/article/header/div/div[2]/h2').get_attribute("innerHTML")
 #       print(inner_html)

bot = Bot()
bot.crawl()