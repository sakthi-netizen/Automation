from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("C:\python\chromedriver")
driver.get("https://www.google.com/maps/@13.1487775,79.9304626,15z")
sleep(2 )

def searchplace():
    place = driver.find_element_by_class_name("tactile-searchbox-input")
    place.send_keys("chennai")
    submit = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    submit.click()
searchplace()

def directions():
    sleep(5)
    directions = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/button/span/img")
    directions.click()
directions()

def find():
    sleep(5)
    find = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
    find.send_keys("Tiruvallur")
    sleep(5)
    search = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search.click()
find()

def kilometers():
    sleep(5)
    totalkilometers = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[1]/div[1]/div[2]/div")
    print("TotalKilometers:",totalkilometers.text)
    sleep(5)
    car = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[1]/div[1]/div[1]/span[1]")
    print("Car Travel:",car.text)
    bus = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[3]/div/div[2]/div[1]/div")
    print("Bus Travel:",bus.text)
kilometers()