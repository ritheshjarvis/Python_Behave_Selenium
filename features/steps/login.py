import time
from behave import when, then
from selenium import webdriver
from features.pages.home import Home
from features.pages.login import Login


@when(u'user launches the website')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.saucedemo.com/')
    context.driver.implicitly_wait(30)


@then(u'login page is displayed')
def step_impl(context):
    Login(context.driver).verify_login_page()


@when(u'user enters the username "standard_user"')
def step_impl(context):
    Login(context.driver).enter_username('standard_user')


@when(u'user enters the password "secret_sauce"')
def step_impl(context):
    Login(context.driver).enter_password('secret_sauce')


@when(u'user clicks on the login button')
def step_impl(context):
    Login(context.driver).click_login()


@then(u'home page is displayed')
def step_impl(context):
    Home(context.driver).verify_home_page()
    time.sleep(3)
