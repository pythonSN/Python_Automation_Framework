from selenium import webdriver
driver = webdriver.Ie(executable_path="C:\Study\Python_Automation_Framework\drivers\IEDriverServer.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
driver.find_element_by_id("welcome").click()
driver.find_element_by_link_text("Logout").click()
driver.close()
driver.quit()
print("Test Completed")


