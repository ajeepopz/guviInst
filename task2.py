from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class GuviInsta:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(10)

    def quit(self):
        self.driver.quit()




    def getNumberOfFollowers(self):
        xpath = "//a[@href='/guviofficial/followers/']"
        self.driver.find_element(by=By.XPATH, value=xpath).text


    def getNumberOfFollowing(self):
        xpath = '//*[@id="mount_0_0_bA"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a'
        return self.driver.find_element(by=By.XPATH, value=xpath).text



url = 'https://www.instagram.com/guviofficial/'
obj = GuviInsta(url)
obj.boot()
obj.getNumberOfFollowers()
obj.getNumberOfFollowing()
obj.quit()
