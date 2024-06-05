from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
path ="C:/Users/prati/Downloads/chromedriver-win64/chromedriver.exe"
s = Service(path)
driver = webdriver.Chrome(service = s)
driver.get("https://www.google.com/")
time.sleep(2)

# to search anything
box = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
# The below line will pass the text you want to search
box.send_keys("House of dragon")
# To automatically press enter key
box.send_keys(Keys.ENTER)
time.sleep(3)

# To open the hbo site
driver.find_element_by_xpath("""//*[@id="kp-wp-tab-overview"]/div[4]/div/div/div/div/div/div[1]/div/div/span/a/h3""").click()
time.sleep(2)
#To save the screenshot
driver.save_screenshot("E:/Python Projects/Web Scrapping/Web-Scrapping/dragon1.png")


# chrome driver  download link

# https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.141/win64/chromedriver-win64.zip