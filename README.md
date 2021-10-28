# io-code-source

![screencapture-127-0-0-1-5000-resultats-lauweded-2021-10-27-15_38_40](https://user-images.githubusercontent.com/15716589/139077075-661f64d9-40f0-4bbe-ab55-d813ecaf6bc5.png)

[![GitHub open issues](https://img.shields.io/github/issues/Lauwed/io-code-source.svg)](https://github.com/Lauwed/io-code-source/issues?q=is%3Aopen+is%3Aissue)
[![MIT License](https://img.shields.io/github/license/Lauwed/io-code-source.svg)](https://github.com/Lauwed/io-code-source/blob/master/LICENSE)

## Getting Started

### Activate the Virtual Environment
On macOS
```
$ source venv\Scripts\activate
```
On PowerShell
```
$ venv\Scripts\activate
```

### Run this command to create your own Virtual Environment
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
pip install python-dotenv
```

### Create your `.env` file
A `.env` file is needed because you need to be connected on your instagram account to be able to visite other people account. It should be created on the same folder then the file `app.py` and it should contain ;
```
INSTA_USERNAME=<your-username>
INSTA_PASSWORD=<your-password>
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

## Troubleshooting
### If you have problems with virtual environment or file problems, please try first to delete the `env` **folder**, then follow this guide : [Installing packages using pip and virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
