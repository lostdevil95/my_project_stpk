import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default='en', help='choose language - en, ru, fr of etc...')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    if browser_name == "chrome":
        print('\nЗапускаем Chrome для теста..')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(10)
    elif browser_name == "firefox":
        print("\nЗапускаем Firefox для теста..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.implicitly_wait(10)
    else:
        raise pytest.UsageError("--browser_name должен быть chrome или firefox")
    yield browser
    print("\nЗакрываем браузер..")
    browser.quit()