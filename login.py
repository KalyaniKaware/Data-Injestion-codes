from selenium import webdriver

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def datacamp(self):
        self.driver.get("https://www.datacamp.com/")

        loginbutton = self.driver.find_elements_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/header/div/div[1]/div[2]/ul/li[5]/a')[0]
        loginbutton.click()

        user = self.driver.find_elements_by_xpath('// *[ @ id = "user_email"]')[0]
        user.click()
        user.send_keys('abc@gmail.com')

        ok = self.driver.find_elements_by_xpath('//*[@id="new_user"]/button')[0]
        ok.click()

        user1 = bot.driver.find_elements_by_xpath('// *[ @ id = "user_password"]')[0]
        user1.click()
        user1.send_keys('*****')

        ok1 = bot.driver.find_elements_by_xpath('// *[ @ id = "new_user"] / div[1] / div[3] / input')[0]
        ok1.click()

bot = Bot()
bot.datacamp()