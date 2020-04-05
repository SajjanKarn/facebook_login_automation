from selenium import webdriver
import creditentials

# driver get
driver = webdriver.Firefox()

driver.get("https://facebook.com")


# Navigating TO The elements
email_input = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
login_btn = driver.find_element_by_xpath("//*[@id=\"u_0_b\"]")

# The Real Movies Begins....
email_input.send_keys(creditentials.username)
password.send_keys(creditentials.password)
login_btn.click()
