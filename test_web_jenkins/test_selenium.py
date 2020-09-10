from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://baidu.com/")
    driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("测试开发工程师")
    sleep(3)
