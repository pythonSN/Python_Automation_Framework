import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="ie", help="Type browser name: chrome or ie or edge")


@pytest.fixture(scope="class")
def test_setup(request):
    global driver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:/Study/Python_Automation_Framework/drivers/chromedriver.exe")
    elif browser == 'ie':
        driver = webdriver.Ie(executable_path="C:/Study/Python_Automation_Framework/drivers/IEDriverServer.exe")
    elif browser == 'edge':
        driver = webdriver.Edge(executable_path="C:/Study/Python_Automation_Framework/drivers/MicrosoftWebDriver.exe")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")
