from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time

service = Service("D:/Development/chromdriver.exe")
driver = webdriver.Chrome(service=service)

url = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

cookie = driver.find_element(By.ID, "cookie")
buy_cursor = driver.find_element(By.ID, "buyCursor")
buy_grandma = driver.find_element(By.ID, "buyGrandma")
buy_factory = driver.find_element(By.ID, "buyFactory")
buy_mine = driver.find_element(By.ID, "buyMine")
buy_shipment = driver.find_element(By.ID, "buyShipment")
buy_alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
buy_portal = driver.find_element(By.ID, "buyPortal")
buy_time_machine = driver.find_element(By.ID, "buyTime machine")


def buy_all():
    buy_time_machine.click()
    buy_portal.click()
    buy_alchemy_lab.click()
    buy_shipment.click()
    buy_mine.click()
    buy_factory.click()
    buy_grandma.click()
    buy_cursor.click()


start_time = time.time()
timeout = time.time() + 5
duration = 5 * 60

while True:
    cookie.click()
    if time.time() > timeout:
        try:
            buy_all()
        except StaleElementReferenceException:
            buy_cursor = driver.find_element(By.ID, "buyCursor")
            buy_grandma = driver.find_element(By.ID, "buyGrandma")
            buy_factory = driver.find_element(By.ID, "buyFactory")
            buy_mine = driver.find_element(By.ID, "buyMine")
            buy_shipment = driver.find_element(By.ID, "buyShipment")
            buy_alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
            buy_portal = driver.find_element(By.ID, "buyPortal")
            buy_time_machine = driver.find_element(By.ID, "buyTime machine")
        timeout = time.time() + 5
        if time.time() - start_time > duration:
            cps_number = driver.find_element(By.ID, "cps").text
            print(cps_number)
            break

while True:
    pass