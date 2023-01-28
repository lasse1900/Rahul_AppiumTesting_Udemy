import time

from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = dict(
    deviceName='R58N40PQA1D', # Device name or just Android
    platformName='Android',
    appPackage='com.samsung.android.dialer',
    appActivity='.DialtactsActivity'
)


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

driver.find_element(By.ID,'com.samsung.android.dialer:id/one').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/two').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/three').click()
driver.find_element(By.ID,'com.samsung.android.dialer:id/seven').click()


driver.find_element(By.ID,'com.samsung.android.dialer:id/dialButton').click()


time.sleep(2)
driver.quit()
