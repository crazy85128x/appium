# test_appium_android.py
import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class TestAppiumAndroid:
    def test_appium_android_real_dev(self):
        print('Appium version = ', webdriver.__version__)
        options = webdriver.AppiumOptions()  # 直接使用 AppiumOptions，如果出現錯誤則可能需要更新 Appium Python 客戶端或檢查導入方式

        options.set_capability('platformName', 'Android')
        options.set_capability('automationName', 'UiAutomator2')
        options.set_capability('appPackage', 'com.samsung.android.calendar')
        options.set_capability('appActivity', 'com.samsung.android.app.calendar.activity.MainActivity')
        options.set_capability('noReset', True)

        appium_server_url = 'http://localhost:4723/wd/hub'
        driver = webdriver.Remote(appium_server_url, options=options)
        time.sleep(1)  # 實際測試中應該避免使用 time.sleep
        driver.quit()
        assert True
