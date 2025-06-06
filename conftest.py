import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: '--browser_name=chrome' or '--browser_name=firefox'")
    
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: '--language=en' or '--language=ru'")
    
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)

    browser = None
    if browser_name == "chrome":
        print("\n\033[92mstart chrome browser for test..\033[0m")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\n\033[92mstart firefox browser for test..\033[0m")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\n\033[92mquit browser..\033[0m")
    browser.quit()
