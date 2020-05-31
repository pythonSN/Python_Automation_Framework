from selenium import webdriver

driver = webdriver.Edge(executable_path="C:/Study/Python_Automation_Framework/drivers/MicrosoftWebDriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
# to check total no of check boxes
print(len(checkboxes))

for checkbox in checkboxes:
    # to select and get the value of option2 checkbox
    if checkbox.get_attribute("value") == 'option2':
        checkbox.click()
        # to verify whether checkbox option 2 is selected or not.
        assert checkbox.is_selected()

radiobuttons=driver.find_elements_by_name("radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

# driver.close()
# driver.quit()
