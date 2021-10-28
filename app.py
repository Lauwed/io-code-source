import os
from flask import Flask, url_for, render_template, request, redirect
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request as urllib2
from time import sleep

# Load env vars
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/connexion')
@app.route('/connexion/<error>')
def connexion(error = None) :
    return render_template('connexion.html', error=error)

@app.route('/resultats')
@app.route('/resultats/<ig_username>')
def resultats(ig_username = None) :
    if ig_username :
        results = scrapping(ig_username)
        if results['publications'] == 0 :
            return redirect(url_for('connexion', error="erreur_username"))
        elif results['image_count'] == 1 :
            return redirect(url_for('connexion', error="erreur_private"))
        return render_template('resultats.html', results=results, username=ig_username)
    else :
        return redirect(url_for('connexion', error="erreur"))

@app.errorhandler(404)
def page_not_found(error) :
    return render_template('404.html'), 404


with app.test_request_context() :
    url_for('static', filename='app.css')
    url_for('static', filename='app.js')


def scrapping(name) :
    insta_url = "https://www.instagram.com/"

    def getsize(uri):
        file = urllib2.urlopen(uri)
        return len(file.read())

    # Start browser
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service = s)
    driver.get(insta_url)

    print('driver ok')

    sleep(1)

    # Accept cookies
    cookies_button = driver.find_element(By.CSS_SELECTOR, ".aOOlW.bIiDR")
    cookies_button.click()
    # Log into Instagram account
    username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

    username_input.send_keys(os.environ.get('INSTA_USERNAME'))
    password_input.send_keys(os.environ.get('INSTA_PASSWORD'))

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    # login_button.click()
    driver.execute_script("arguments[0].click();", login_button)

    # Wait login time
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[alt="lauweded\'s profile picture"]')))

    # Then, go on the user profil
    if '@' in name :
        name = name.replace('@', '')
    insta_user_url = "https://www.instagram.com/" + name + "/"
    driver.get(insta_user_url)

    element = None
    try :
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[data-testid="user-avatar"]')))
        print('User found')
    except :
        print('error')
    finally :
        print (element, 'element Selenium quand le JS a completement charge')

    print('Opening the HTML file to keep inner HTML of the page...');
    f = open("results.html", "w+")
    print('Writing inside this file...')
    while True :
        try :
            f.write(str(driver.find_element(By.CSS_SELECTOR, 'main').get_attribute('innerHTML').encode('utf-8').strip()))
            break
        except :
            return {
                "publications": 0
            }
    f.close()
    print('Inner HTML OK !')

    with open("results.html") as fp:
        soup = BeautifulSoup(fp, "lxml")

    # Get numbers of followers
    stats_account = soup.find_all(attrs={'class': 'k9GMp'})

    print('Looking for numbers of publications and followers');
    followers = 0
    publications = 0

    for index, num in enumerate(stats_account):
        # Numbers of publications
        if index == 0 :
            publications = num.find('span').find('span').text
        # Numbers of followers
        if index == 1 :
            followers = num.find('a').find('span').text

    if 'k' in str(followers) :
        followers = followers.replace('k', '')
        followers = float(followers) * 1000
    elif 'm' in str(followers) :
        followers = followers.replace('m', '')
        followers = float(followers) * 1000000

    if ',' in str(publications) :
        publications = publications.replace(',', '')

    if ',' in str(followers) :
        followers = followers.replace(',', '')

    print (followers, 'followers')
    print (publications, 'publications')

    # Get images and their sizes
    print('Scrapping all the images of the account')
    images = soup.find_all('img')
    sum_sizes = 0
    image_count = 0

    for image in images:
        size = getsize(image.get('src')) * 4
        sum_sizes += size
        image_count += 1

    print (sum_sizes, 'somme des tailles des images')
    print (image_count, 'le nombre d\'images')

    # Calculations

    # poids d'une image en moyenne
    average_size = float(sum_sizes) / float(image_count)
    print (average_size, 'Taille moyenne des images')

    # Nombre de publications par la taille moyenne
    size_tot = float(publications) * float(average_size)
    print (size_tot, 'Taille totale des images avec taille moyenne')

    # poids total de toutes les images base sur la taille moyenne en fonction du nombre de followers
    size_tot += float(followers) * float(average_size)
    print (size_tot, 'Taille totale multipliee par le nbre de followers')

    # Consommation electrique ; (poids total / 1E+06) * 1E-03
    elect = (size_tot / 1000000.0) * 0.001
    print (elect, 'Consommation en electricite')

    # Consommation en g de CO2
    emission = elect * 0.276
    emission_g = "%.2f" % (elect * 0.276 * 100)
    print (emission_g, emission, 'emission')

    # Calcul score
    score = 1500 / (float(emission_g) + (1500 / 255.))
    print (score, 'Score')

    # Score a envoyer a la fontaine

    # print ('\n\nPYSERIAL\n')
    #
    # sPort = '/dev/cu.usbmodem14101'  # On Mac - find this using >ls /dev/cu.usb*
    #
    # arduino = serial.Serial(sPort, 9600, timeout=.1)
    #
    # while True:
    #     time.sleep(1)  # give the connection a second to settle
    #     arduino.write(str(int(score)))
    #     data = arduino.readline()
    #     if data:
    #         print data.rstrip('\n')  # strip out the new lines for now
    #         break
    #     # (better to do .read() in the long run for this reason
    #
    # arduino.close()

    return {
        "publications": publications,
        "image_count": image_count,
        "sn_emission": 0,
        "fb_emission": 0,
        "tt_emission": 0,
        "ig_emission": emission_g,
        "tot_emission": emission_g,
        "score": score
    }