from selenium import webdriver
import creditentials

url = "https://facebook.com"

driver = webdriver.Firefox()

driver.get(url)

email_input = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
login_btn = driver.find_element_by_xpath("//*[@id=\"u_0_b\"]")

email_input.send_keys(creditentials.username)
password.send_keys(creditentials.password)
login_btn.click()
