import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

promised_down = 120
promised_up = 10

TWITTER_EMAIL = TWITTER_EMAIL
TWITTER_PASSWORD = TWITTER_PASSWORD

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(name="detach", value=True)
        self.driver = webdriver.Chrome(chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://speedtest.xfinity.com/")

        time.sleep(5)
        go_button = self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[2]/div[1]/div/div/div/button')
        go_button.click()

        time.sleep(30)
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[2]/details/summary/div/dl/dd')

        close_button = self.driver.find_element(By.CLASS_NAME, value='_pi_closeButton')
        close_button.click()

        more_options = self.driver.find_element(By.XPATH, value ='//*[@id="app"]/div[2]/details/summary/div/div/p')
        more_options.click()

        time.sleep(25)
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="app"]/div[2]/details/div/div/dl/div[1]/dd')
        values = [self.down.text, self.up.text]
        return values

    def tweet_at_provider(self, up, down):
        self.driver.get("https://x.com/login")

        time.sleep(15)
        email_input = self.driver.find_element(By.NAME, value="text")
        email_input.send_keys(TWITTER_EMAIL, Keys.ENTER)

        time.sleep(3)
        verify_input = self.driver.find_element(By.NAME, value="text")
        verify_input.send_keys(TWITTER_USERNAME, Keys.ENTER)

        time.sleep(3)
        password_input = self.driver.find_element(By.NAME, value="password")
        password_input.send_keys(TWITTER_PASSWORD, Keys.ENTER)

        time.sleep(3)
        new_post_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        new_post_button.click()

        time.sleep(20)
        post_input = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        post_input.send_keys(f"My download speed is: {down}, and my upload speed is: {up}. Not too bad!")
        post_input.send_keys(Keys.CONTROL, Keys.ENTER)

        time.sleep(10)
        close_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/button')
        close_button.click()

new_bot = InternetSpeedTwitterBot()
values = new_bot.get_internet_speed()
new_bot.tweet_at_provider(up=values[1], down=values[0])
