from selenium import webdriver
import time

# driver = webdriver.Chrome("D:\Users\taps1\PycharmProjects\new\drivers\chromedriver.exe")
driver = webdriver.Firefox()
# driver = webdriver.Chrome()


# driver.set_page_load_timeout("10")
driver.get("https://gateway.iitmandi.ac.in/facstaff/login.php")
driver.find_element_by_name("username").send_keys("intern_tapaswin")
driver.find_element_by_name("password").send_keys("ITW@1234#")
# driver.find_element_by_name("submit").click()
# driver.find_element_by_id("submit").click()
# driver.find_element_by_value("submit").click()
driver.find_element_by_css_selector(type("Submit")).click()
# driver.find_element_by_link_text("Submit")
time.sleep(10)
driver.quit()
