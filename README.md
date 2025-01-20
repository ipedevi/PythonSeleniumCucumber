# Table Of Content
<!-- TOC -->
* [PythonSeleniumBehave (Cucumber de python)](#pythonseleniumbehave-cucumber-de-python)
* [To Execute](#to-execute)
<!-- TOC -->
# PythonSeleniumBehave (Cucumber de python)
Automation Framework that works with Python Selenium and Behave (Cucumber for python). 
In that case the Behave read the feature files and then execute pytest to manage all the Selenium test automatically.

Made in that way you can obtain all pytest power but using BDD.

To be executed is necessary to install following tools:
- python
- pytest (with pip)
- Selenium (with pip)
- Selenium drivers (downloading chromedriver, geckodriver, etc)
- behave

# To Execute
First of all, you need to change myconfig.py in features directory to adapt it to your needs.

Then, in order to execute, you need to use next sentences in project directory:
- behave

(it will execute all <tests>.feature files that exists in features folder)
