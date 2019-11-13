from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS()
driver.get("https://www.instagram.com/lauweded/")

f = open("results.html", "w+")
f.write(driver.find_element_by_class_name('FyNDV').get_attribute('innerHTML').encode('utf-8').strip())
f.close()

with open("results.html") as fp :
    soup = BeautifulSoup(fp, "lxml")

print(soup)