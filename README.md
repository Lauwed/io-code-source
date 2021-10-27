# io-code-source

## Getting Started

### Activate the Virtual Environment
```
$ source venv\Scripts\activate
```

Run this command to create your own Virtual Environment
```
$ py -3 -m venv venv     
```

### Install all the packages
```
pip install Flask
pip install beautifulsoup4
pip install -U selenium
pip install webdriver-manager
pip install lxml
```

### Launch Flask
```
$ flask run
```
If you have error messages, try to run those commands first, then retry :
```
$ export FLASK_APP=app
```
```
$ export FLASK_ENV=development
```
Don't hesitate to read [this article](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-fr) if you need help

## Packages
- Flask
- Beautiful soup 4
- Selenium
- webdriver_manager
- lxml

## Structure
- The folders `static` and `templates` contains all the client-side files.
- The file `app.py` contains the main script of the application. It is from this file that Flask runs.
- The file `commands.py` contains the different commands for the Arduino. **WIP**
- The file `results.html` contains temporarily the HTML page that the script is scraping.
- The file `scraping.py` is the script test for scraping a page.