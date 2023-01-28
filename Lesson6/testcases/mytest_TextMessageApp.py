import time

from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = dict(
    deviceName='R58N40PQA1D', # Device name or just Android
    platformName='Android',
    appPackage='com.samsung.android.messaging/.ui.view.main',
    appActivity='.WithActivity',
    automationName= "uiautomator2",
    fullReset= "true"
)


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)



time.sleep(2)
driver.quit()
