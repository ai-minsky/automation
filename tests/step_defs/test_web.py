#  Copyright (c) 2020. This code has been written by Andrei Izbavitelev

import pytest
from bs4 import BeautifulSoup
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

PAGE = 'http://qainterview.pythonanywhere.com'

scenarios('../features/web.feature')


@pytest.fixture
def browser():
    b = webdriver.Chrome()
    b.implicitly_wait(10)
    yield b
    b.quit()


# Given Steps

@given('Factorial home page is displayed')
def home(browser):
    browser.get(PAGE)


# When Steps

@when(parsers.parse('the user enter number "{number}"'))
def search_phrase(browser, number):
    input_field = browser.find_element_by_id('number')
    calculate_button = browser.find_element_by_xpath('//*[@id="getFactorial"]')
    input_field.clear()
    input_field.send_keys(number)
    calculate_button.click()


@when(parsers.parse('the user navigate "{link_text}"'))
def navigate_to_link(browser, link_text):
    link = browser.find_element_by_link_text(link_text)
    link.click()


# Then Steps

@then(parsers.parse('application shows factorial of "{number}" equals "{answer}"'))
def verify_correct_answer(browser, number, answer):
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="resultDiv"]'), answer)
    )
    result_filed = browser.find_element_by_xpath('//*[@id="resultDiv"]')

    try:
        number = int(number)
    except:
        number = str(number)

    if (isinstance(number, int)):
        assert result_filed.text == 'The factorial of ' + str(number) + ' is: ' + str(answer)
    else:
        assert result_filed.text == answer


@then(parsers.parse('application title is "{title}"'))
def verify_title(browser, title):
    assert browser.title == title


@then(parsers.parse('application shows textbody "{text}'))
def verify_correct_answer(browser, text):
    assert browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/h1').text == text


@then(parsers.parse('application shows correct footer "{footer}'))
def verify_correct_answer(browser, footer):
    assert browser.find_element_by_xpath('/html/body/div[2]/div/p[2]').text == footer


@then(parsers.parse('redirect to correct page "{resource}" "{text}"'))
def verify_title(browser, resource, text):
    try:
        if PAGE in browser.current_url:
            assert resource in browser.current_url
            soup = BeautifulSoup(browser.page_source, 'html.parser')
            assert text == soup.find('body').text
    finally:
        browser.get(PAGE)
