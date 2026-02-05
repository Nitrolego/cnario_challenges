import re
from playwright.sync_api import Page, expect

def test_empty_fields(page: Page):
    page.goto("https://www.cnarios.com/challenges/login-flow#challenge")
    #setup: go to page

    #test: input empty credentials
    #assert: "Both username and password are required"

def test_invalid_credentials(page: Page):
    #setup: go to page

    #test: input invalid credentials
    #assert: "fail message"
    print("test")

def test_login_as_user(page: Page):
    #setup: go to page

    #test: input valid credentials as user
    #assert: "You are logged in as USER"
    print("test")

def test_login_as_admin(page: Page):
    #setup: go to page

    #test: input valid credentials as admin
    #assert: "You are logged in as ADMIN"
    print("test")

def test_logout(page: Page):
    #setup, 
    # go to page
    # login as user/admin

    #click logout button
    #assert: "login form is visible again"
    print("test")