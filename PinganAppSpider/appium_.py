import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# 手机、软件信息
cap = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "54adc63e",
    "appPackage": "com.pingan.papd",
    "appActivity": "com.pingan.papd.ui.activities.JKLogoActivity",
    "noReset": True
}

# 建立连接
driver = webdriver.Remote('http://localhost:4723/wd/hub', cap)


def get_size():
    '''获取手机屏幕尺寸'''
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


# 等待加载
time.sleep(10)

# 点击关掉广告
try:
    if WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(
            "//android.widget.ImageView[@resource-id='com.pingan.papd:id/pop_ad_close_half']")):
        driver.find_element_by_xpath(
            "//android.widget.ImageView[@resource-id='com.pingan.papd:id/pop_ad_close_half']").click()
except:
    pass

# 点击 去医疗
# try:
#     if WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(
#             "//android.widget.ImageView[@resource-id='com.pingan.papd:id/tabSwitch']")):
#         driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.pingan.papd:id/tabSwitch']").click()
# except:
#     pass

# 等待加载
time.sleep(3)

# 点击 全国专家
driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.pingan.papd:id/textTab2']").click()

# 等待数据加载
time.sleep(3)

# 点击 全国
driver.find_element_by_xpath("//android.view.View[@content-desc='全国']").click()
# driver.find_element_by_class_name("android.view.View").click()

# 等待数据加载
time.sleep(3)

# 点击 北京
driver.find_element_by_xpath(
    "//android.view.View/android.view.View[5]/android.view.View[2]/android.view.View[2]").click()

# 等待数据加载
time.sleep(3)

# 循环滑动
while True:
    try:
        # 滑动
        l = get_size()

        # 滑动参数
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.85)
        y2 = int(l[1] * 0.15)

        # 滑动
        driver.swipe(x1, y1, x1, y2)
        # 等待刷新
        time.sleep(0.5)
    except:
        pass