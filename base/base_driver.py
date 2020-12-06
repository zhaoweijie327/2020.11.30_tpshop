'''
封装driver基类
'''
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from page.mp.mp_find_element import Mp_Find_Element
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

    # 公用控件操作
    def select_option(self,driver,channel_name,element,option_name):
        # 获取控件元素
        xpath_text = "[placeholder*='{}']".format(channel_name)
        css_string = driver.find_element_by_css_selector(xpath_text)
        # 点击频道
        self.input_click(css_string)
        # 获取拼到里面的元素
        option_list = driver.find_elements_by_css_selector(element)
        # 是否找到标识符
        is_element = False
        # 遍历寻找正确文本
        for option_element in option_list:
            # 如果相同就点击事件
            if self.input_text(option_element) == option_name:
                self.input_click(option_element)
                is_element = True
                break
            # 如果不相等则鼠标悬浮到该项并且向下按键
            else:
                ActionChains(driver).move_to_element(option_element).send_keys(Keys.DOWN).perform()
                is_element = False

        # 找不到元素抛出异常
        if is_element is False:
            NoSuchElementException("can't find {} option".format(option_name))
