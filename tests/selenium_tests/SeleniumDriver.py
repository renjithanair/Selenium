from selenium import webdriver
import time

# driver = webdriver.Firefox(executable_path="C:\\Grid\\geckodriver.exe")
# driver = webdriver.Ie(executable_path="C:\\Grid\\IEdriverserver.exe")

driver = webdriver.Chrome("C:\\Users\\renji\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)
driver.get("https://qavbox.github.io/demo")
assert "QAVBOX" in driver.title
driver.find_element_by_link_text("SignUp Form").click()
driver.save_screenshot("C:\\Users\\renji\\Downloads\\Grid\\test.png")
time.sleep(3)
driver.quit()