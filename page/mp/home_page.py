#-*-coding:utf-8 -*-
'''
利用po模式将页面分为三层（对象、操作、业务）
'''
import time

from base.base_driver import DriverBase, DriverHandles
from page.mp.mp_find_element import Mp_Find_Element


# 对象层
class Mp_HomePage(DriverBase):

    def __init__(self):
        super().__init__()

    # 定位内容管理
    def find_home_content(self):
        return self.find_elemnet(Mp_Find_Element.home_content)

    # 定位发布文章
    def find_home_article(self):
        return self.find_elemnet(Mp_Find_Element.home_article)

# 操作层
class Mp_HomeHandles(DriverHandles):

    def __init__(self):
        self.mp_page = Mp_HomePage()

    # 模拟点击内容管理操作
    def input_home_content(self):
        self.input_click(self.mp_page.find_home_content())

    # 模拟点击发布文章操作
    def input_home_article(self):
        self.input_click(self.mp_page.find_home_article())

# 业务层
class Mp_HomeBuissens:

    def __init__(self):
        self.mh_handles = Mp_HomeHandles()

    # 点击内容管理发布文章
    def mp_home_ca(self):
        # 点击内容管理
        self.mh_handles.input_home_content()
        # 点击文章发布
        self.mh_handles.input_home_article()
        time.sleep(2)

