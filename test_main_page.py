from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, "#login_link")