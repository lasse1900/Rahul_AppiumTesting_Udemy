import time

from appium import webdriver

desired_cap = {}
desired_cap['platformName'] = 'Android'
desired_cap['deviceName'] = 'Android'
desired_cap['appPackage'] = 'com.sec.android.app.popupcalculator'
desired_cap['appActivity'] = '.Calculator'


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)
driver.implicitly_wait(5)

driver.find_element_by_id('com.sec.android.app.popupcalculator:id/calc_keypad_btn_02').click()
#driver.find_element_by_accessibility id('2').click()  # Depricated
driver.find_element_by_id('com.sec.android.app.popupcalculator:id/calc_keypad_btn_add').click()
driver.find_element_by_id('com.sec.android.app.popupcalculator:id/calc_keypad_btn_04').click()
driver.find_element_by_id('com.sec.android.app.popupcalculator:id/calc_keypad_btn_equal').click()

result = driver.find_element_by_id('com.sec.android.app.popupcalculator:id/calc_edt_formula').text

print(result)
assert int(result) == 6
time.sleep(2)
driver.quit()

