# Table Of Content

# PythonSeleniumRequestBehave (Cucumber de python)
Automation Framework that works with Python Selenium or Request and Behave (Cucumber for python). 
In that case the Behave read the feature files and then execute pytest to manage all the Selenium test automatically or execute request to in case of API test.

Made in that way you can obtain all pytest power but using BDD and at the same time you can execute API test depending on the feature.

# Install
To be executed is necessary to install following tools:
- python
- pytest (with pip)
- Selenium (with pip)
- Selenium drivers (downloading chromedriver, geckodriver, etc)
- behave
- request

# Configuration
In the feature files you need to add one tag ("web" or "api"), and the framework will detect it and will execute API test or User Interface test with Selenium.

- Example to execute API test:
  
    Feature: Api functionality
    
    @api

    Scenario: User can test also API

        Given I visit public marvel api
        When I obtain the first published title
        Then I can obtain deeper info from this title

- Example to execute WEBDRIVER test:
  
    Feature: Login functionality
    
    @web

    Scenario: User can log in with valid credentials

        Given I visit the login page
        When I enter next valid credentials user1 amd pass1
        Then I should see the dashboard

# To Execute
First of all, you need to change myconfig.py in features directory to adapt it to your needs.

Then, in order to execute, you need to use next sentences in project directory:
- behave

(it will execute all <tests>.feature files that exists in features folder)
.
