import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument("--disable-gpu")
    print("initiating chrome driver")
    driver = webdriver.Chrome(options=chrome_options,executable_path="/var/lib/jenkins/webdriver/chromedriver")
    driver.get("http://seleniumeasy.com/test")
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()
