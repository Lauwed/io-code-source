from bs4 import BeautifulSoup
# from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# import os
import urllib.request as urllib2

def getsize(uri):
    file = urllib2.urlopen(uri)
    return len(file.read())

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = s)
driver.get("https://www.instagram.com/lauweded/")

f = open("results.html", "w+")
f.write(str(driver.find_element(By.CLASS_NAME, 'SCxLW').get_attribute('innerHTML').encode('utf-8').strip()))
f.close()

with open("results.html") as fp :
    soup = BeautifulSoup(fp, "lxml")

# Get numbers of followers

stats_account = soup.find_all(attrs={'class': 'k9GMp'})
followers = 0
publications = 0

for index, num in enumerate(stats_account) :
    # Numbers of publications
    if index == 0 :
        publications = num.find('span').text
    # Numbers of followers
    if index == 1 :
        followers = num.find('span').text

print(followers)

# Get images and their sizes

images = soup.find_all('img')
sum_sizes = 0
image_count = 0

for image in images:
    # print(image.get('src'))
    size = getsize(image.get('src')) * 4
    size_str = str(size) + ' bytes'
    # print(size_str)
    sum_sizes += size
    image_count += 1

# print(sum_sizes)
# print(image_count)

# Calculations

# poids d'une image en moyenne
average_size = float(sum_sizes) / float(image_count)
print(average_size)

# Nombre de publications par la taille moyenne
size_tot = float(publications) * average_size
print(size_tot)

# poids total de toutes les images base sur la taille moyenne en fonction du nombre de followers
size_tot += float(followers) * average_size
print(size_tot)

# Consommation electrique ; (poids total / 1E+06) * 1E-03
elect = (size_tot / 1000000.0) * 0.001
print(elect)

# Consommation en CO2
emission = elect * 0.276
print(emission)