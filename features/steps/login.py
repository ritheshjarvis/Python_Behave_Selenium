import time
from behave import when, then
from selenium import webdriver
from features.pages.home import Home
from features.pages.login import Login


@when(u'user launches the website')
def step_impl(context):
    # context.driver = webdriver.Chrome()
    context.driver.get('https://www.saucedemo.com/')
    context.driver.implicitly_wait(30)


@then(u'login page is displayed')
def step_impl(context):
    Login(context.driver).verify_login_page()


@when(u'user enters the username "{username}"')
def step_impl(context, username):
    Login(context.driver).enter_username(username)


@when(u'user enters the password "{password}"')
def step_impl(context, password):
    Login(context.driver).enter_password(password)


@when(u'user clicks on the login button')
def step_impl(context):
    Login(context.driver).click_login()


@then(u'home page is displayed')
def step_impl(context):
    Home(context.driver).verify_home_page()