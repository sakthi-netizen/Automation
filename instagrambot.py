from selenium import webdriver
import time

browser = webdriver.Chrome("C:\python\chromedriver")
browser.get("https://www.instagram.com/")
time.sleep(2)

def login():
    name = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    name.send_keys("username")
    time.sleep(2)
    password = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    password.send_keys("password")
    password.submit()
    time.sleep(2)
login()

def notify():
    notnow = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    notnow.click()
    time.sleep(2)
    noti = browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
    time.sleep(2)
notify()

def message():
    msgclick = browser.find_element_by_class_name("xWeGp")
    msgclick.click()
    time.sleep(5)
message()

def final():
    chat = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[2]/a/div/div[2]/div[1]/div/div/div/div")
    chat.click()
    time.sleep(3)
    msg = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
    msg.send_keys("Have a good day")
    time.sleep(2)
    send = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
    send.click()
final()

