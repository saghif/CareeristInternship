from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# init driver
driver = webdriver.Chrome(executable_path='/Users/bojanskaljak/Desktop/JoBeASY/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

driver.find_element(By.ID, 'helpsearch').send_keys('Cancel order',Keys.RETURN)
sleep(2)
#driver.find_element(By.ID, 'helpsearch').send_keys(Keys.RETURN)

# verify
expected_result = 'Cancel Items or Orders'
actual_result = driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']").text
assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {expected_result}'
if (expected_result == actual_result):
    print("testcase passed")
else:
    print("testcase failed")
driver.quit()

