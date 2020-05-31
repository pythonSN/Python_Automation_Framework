import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Study/Python_Automation_Framework/drivers/chromedriver.exe")
#driver.maximize_window()
driver.get("https://www.makemytrip.com/")
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("Del")
time.sleep(2)
cities = driver.find_elements_by_css_selector("p[class*='font14 appendBottom5 blackText']")
for city in cities:
    #print(city.text)
    if city.text == "Del Rio, United States":
        city.click()
        break
driver.find_element_by_id("toCity").click()
driver.find_element_by_xpath("//p[contains(text(),'Delhi, India')]").click()
driver.close()
driver.quit()

