from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException



url="https://open.spotify.com/album/4g5aWAkAKX8qQvRVQAgDXR"


driver = webdriver.Chrome(executable_path="C:\\pythonProjects\\spotify on loop player\\chromedriver.exe")

driver.maximize_window()
driver.get(url)
time.sleep(5)
driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[1]/header/div[5]/button[2]").click()
time.sleep(25)
driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div[3]/div/button[1]").click()
for loop in range(2):
    driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[2]").click()
    time.sleep(5)
    if ElementClickInterceptedException:
        pass
time.sleep(5)
while True:
    try:
        driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[1]/button[2]').click()
        time.sleep(40)
    except NoSuchElementException:
        pass
        print("not found")
