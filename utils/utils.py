# to read the function name
import inspect


def whoami():
    return inspect.stack()[1][3]


# CONSTANTS

URL = "https://opensource-demo.orangehrmlive.com/"
USERNAME = "Admin"
PASSWORD = "admin123"

CHROME_PATH = "C:/Study/Python_Automation_Framework/drivers/chromedriver.exe"
IE_PATH = "C:/Study/Python_Automation_Framework/drivers/IEDriverServer.exe"
EDGE_PATH = "C:/Study/Python_Automation_Framework/drivers/MicrosoftWebDriver.exe"

SCREENSHOTS_PATH = "C:/Study/Python_Automation_Framework/screenshots/"