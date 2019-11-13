from bs4 import BeautifulSoup
from PIL import Image
from selenium import webdriver
import os
import urllib2

def getsize(uri):
    file = urllib2.urlopen(uri)
    return len(file.read())

driver = webdriver.PhantomJS()
driver.get("https://www.instagram.com/lauweded/")

f = open("results.html", "w+")
f.write(driver.find_element_by_class_name('SCxLW').get_attribute('innerHTML').encode('utf-8').strip())
f.close()

with open("results.html") as fp :
    soup = BeautifulSoup(fp, "lxml")

# Get numbers of followers

stats_account = soup.find_all(attrs={'class': 'g47SY'})
followers = 0
publications = 0

for index, num in enumerate(stats_account) :
    if index == 0 :
        publications = num.text
    if index == 1 :
        followers = num.text

print followers

# Get images and their sizes

images = soup.find_all('img')
sum_sizes = 0
image_count = 0

for image in images:
    print(image.get('src'))
    size = getsize(image.get('src')) * 4
    size_str = str(size) + ' bytes'
    print size_str
    sum_sizes += size
    image_count += 1

print sum_sizes
print image_count

# Calculations

# poids d'une image en moyenne
average_size = float(sum_sizes) / float(image_count)
print average_size

# Nombre de publications par la taille moyenne
size_tot = float(publications) * average_size
print size_tot

# poids total de toutes les images base sur la taille moyenne en fonction du nombre de followers
size_tot += float(followers) * average_size
print size_tot

# Consommation electrique ; (poids total / 1E+06) * 1E-03
elect = (size_tot / 1000000.0) * 0.001
print elect

# Consommation en CO2
emission = elect * 0.276
print emission