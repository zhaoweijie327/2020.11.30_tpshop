import json
import time

import allure
from selenium import webdriver

from config import BAS_URL

'''
获取webdriver对象
获取json数据方法
'''

class DriverUtils:

    __driver = None

    __key = True


    @classmethod
    def open_driver(cls):
        if cls.__driver is None:
            # 打开webdriver驱动
            cls.__driver = webdriver.Chrome()
            # 打开窗口最大化
            cls.__driver.maximize_window()
            # 隐式等待
            cls.__driver.implicitly_wait(10)
        return cls.__driver

    @classmethod
    def check_open_key(cls,key):
        # 修改开关
        cls.__key = key

    @classmethod
    def close_driver(cls):
        # 关闭浏览器
        if cls.__driver is not None and cls.__key is True:
            cls.open_driver().quit()
            cls.__driver = None

    @classmethod
    def screen_image(cls,name="截图"):
        # 截图到报告
        png_name = BAS_URL + '/image/tp_shop_{}.png'.format(int(time.time()*10000))

        cls.open_driver().get_screenshot_as_file(png_name)

        with open(png_name,"rb") as file:
            allure.attach(file.read(),name,attachment_type=allure.attachment_type.PNG)

# json数据驱动
def data_path(data_url,data_values):
    # 创建数据列表
    data_list = []
    # 读取json数据
    with open(data_url,"r",encoding="utf-8") as file:
        # json数据转成字典格式
        data_dict = json.load(file)
        # 获取值
        data_json = data_dict.get(data_values)
        # 将获取到的值保存在列表内
        data_list.append(list(data_json.values()))
    # 返回列表数据
    return data_list