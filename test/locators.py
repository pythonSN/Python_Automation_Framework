from datetime import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Edge(executable_path="C:/Study/Python_Automation_Framework/drivers/MicrosoftWebDriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)
# locator - Name
driver.find_element_by_name("name").send_keys("Sandeep")
driver.find_element_by_name("email").send_keys("sandeepnaganath@gmail.com")

# locator  - CSS
#driver.find_element_by_css_selector("input[name='name']").send_keys("CSS")


# locator ID

driver.find_element_by_id("exampleInputPassword1").send_keys("Password")
driver.find_element_by_id("exampleCheck1").click()

#locator Drop-down by Select function

gender = Select(driver.find_element_by_id("exampleFormControlSelect1"))
gender.select_by_visible_text("Female")
#gender.select_by_index(0)

#locator - Xpath

#driver.find_element_by_xpath("//input[@type='submit']").click()

#locator - XPath by ChroPath Plug-in
driver.find_element_by_xpath("//input[@class='btn btn-success']").click()

#locator - Class
#print(driver.find_element_by_class_name("alert-success").text)
#locator - CSS Regular expression:

#print(driver.find_element_by_css_selector("div[class*='alert-success']").text)


#locator Xpath Regular expression:

print(driver.find_element_by_xpath("//div[contains(@class, 'alert-success')]").text)




driver.close()
driver.quit()

