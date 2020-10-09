from selenium import webdriver

class Music():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def play(self):
        channel_name = input("Enter YouTube channel name:  ")
        url = "https://www.youtube.com/c/"+channel_name+"/videos"
        self.driver.get(url)

        path = self.driver.find_elements_by_xpath('//*[@id="items"]/ytd-grid-video-renderer[1]')
        path[0].click()

bot = Music()
bot.play()