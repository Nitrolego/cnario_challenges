"""
PLP_001 - PLP_004 is not doable due to a lack of complete data on the challenge page.
PLP_005 - Partially doable - Pagination controls cannot be fully validated due to incomplete data.
"""
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.mark.skip(reason="Not doable due to incomplete data on the page")
def test_PLP_001(playwright: Playwright):
    #Count products in each category

    #browser setup
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #go to page under test
    page.goto("https://www.cnarios.com/challenges/product-listing-pagination#challenge")
    
    #clean up
    context.close()
    browser.close()

@pytest.mark.skip(reason="Not doable due to incomplete data on the page")
def test_PLP_002(playwright: Playwright):
    #Find specific product and identify its page
    #Not doable due to incomplete data on the page

    #browser setup
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #go to page under test
    page.goto("https://www.cnarios.com/challenges/product-listing-pagination#challenge")
    
    #clean up
    context.close()
    browser.close()

@pytest.mark.skip(reason="Not doable due to incomplete data on the page")
def test_PLP_003(playwright: Playwright):
    #Find highest-rated product in each category
    #Not doable due to incomplete data on the page

    #browser setup
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #go to page under test
    page.goto("https://www.cnarios.com/challenges/product-listing-pagination#challenge")
    
    #clean up
    context.close()
    browser.close()

def test_PLP_004(playwright: Playwright):
    #Find most expensive product in each category
    #Not doable due to incomplete data on the page

    #browser setup
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #go to page under test
    page.goto("https://www.cnarios.com/challenges/product-listing-pagination#challenge")
    
    #clean up
    context.close()
    browser.close()

def test_PLP_005(playwright: Playwright):
    #Validate pagination controls
    #Not doable due to incomplete data on the page

    #browser setup
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #go to page under test
    page.goto("https://www.cnarios.com/challenges/product-listing-pagination#challenge")
    
    #clean up
    context.close()
    browser.close()

def test_PLP_005(playwright: Playwright):
    #Validate pagination controls
    #Not doable due to incomplete data on the page

    #browser setup
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #go to page under test
    page.goto("https://www.cnarios.com/challenges/product-listing-pagination#challenge")
    
    #clean up
    context.close()
    browser.close()

def test_PLP_005(playwright: Playwright):
    #Validate pagination controls
    #Not doable due to incomplete data on the page

    #browser setup
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #go to page under test
    page.goto("https://www.cnarios.com/challenges/product-listing-pagination#challenge")
    
    #clean up
    context.close()
    browser.close()

def test_PLP_006(playwright: Playwright):
    #Verify product card details format

    #browser setup
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #go to page under test
    page.goto("https://www.cnarios.com/challenges/product-listing-pagination#challenge")

    #setup: login as admin
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    #test: click the logout button
    page.get_by_role("button", name="Logout").click()

    #assert: logout successful (see login form)
    expect(page.get_by_role("heading", name="Login", exact=True)).to_be_visible()
    expect(page.get_by_role("textbox", name="Username")).to_be_empty()
    expect(page.get_by_role("textbox", name="Password")).to_be_empty()
    
    #clean up
    context.close()
    browser.close()