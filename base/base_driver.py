'''
封装driver基类
'''
from selenium.webdriver import ActionChains

from utils import DriverUtils


class DriverBase:

    def __init__(self):
        self.driver = DriverUtils.open_driver()

    # find_element定位元素方法
    def find_elemnet(self,loc):
        return self.driver.find_element(*loc)

    # find_elements一组定位元素方法
    def find_elements(self,loc):
        return self.driver.find_elements(*loc)

class DriverHandles:

    # 输入方法
    def input_senk(self,element,text):
        # 清除输入框中的内容
        element.clear()
        # 输入
        element.send_keys(text)

    # 点击方法
    def input_click(self,element):
        element.click()

    # 获取信息
    def input_text(self,element):
        return element.text

    # 切换窗口方法
    def input_windows(self,driver):
        # 获取所有窗口语句柄
        lists = driver.window_handles
        # 切换指定窗口
        driver.switch_to.window(lists[-1])

    # 滚动条
    def input_gundongtiao(self,driver):
        js = "window.scrollTo(0,3000)"
        driver.execute_script(js)

    # 页面切换
    def input_ifram(self,driver,element):
        driver.switch_to.frame(element)

    # 恢复到主页面(页面切换)
    def input_default(self,driver):
        driver.switch_to.default()

    # 鼠标操作
    def input_actions(self,driver,element):
        ActionChains(driver).move_to_element(element).perform()

