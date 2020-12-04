'''
利用po模式将页面分为三层（对象、操作、业务）
'''
import time

from base.base_driver import DriverBase, DriverHandles
from page.mp.mp_find_element import Mp_Find_Element


# 对象层
class Mp_PusairPage(DriverBase):

    def __init__(self):
        super().__init__()

    # 定位文章标题
    def find_pusair_title(self):
        return self.find_elemnet(Mp_Find_Element.article_title)

    # 定位ifram页面
    def find_pusair_ifram(self):
        return self.find_elemnet(Mp_Find_Element.article_ifram)

    # 定位ifram页面
    def find_pusair_content(self):
        return self.find_elemnet(Mp_Find_Element.article_content)

    # 定位选择图片
    def find_pusair_choose_picture(self):
        return self.find_elemnet(Mp_Find_Element.article_choose_picture)

    # 定位图片
    def find_pusair_picture(self):
        return self.find_elemnet(Mp_Find_Element.article_picture)

    # 定位确定
    def find_pusair_ascertain(self):
        return self.find_elemnet(Mp_Find_Element.article_ascertain)

# 操作层
class Mp_PusairHandles(DriverHandles):

    def __init__(self):
        self.mpu_page = Mp_PusairPage()

    # 模拟写入文章标题
    def input_pusair_title(self,title):
        self.input_senk(self.mpu_page.find_pusair_title(),title)

    # 模拟写入文章内容
    def input_pusair_content(self,content):
        # 进入子页面
        self.input_ifram(self.mpu_page.driver,self.mpu_page.find_pusair_ifram())
        # 写入内容
        self.input_senk(self.mpu_page.find_pusair_content(),content)
        # 退出子页面
        self.mpu_page.driver.switch_to.default_content()

    # 模拟点击图片
    def input_pusair_picture(self):
        self.input_click(self.mpu_page.find_pusair_choose_picture())
        self.input_click(self.mpu_page.find_pusair_picture())

    # 模拟点击确定
    def input_pusair_ascertain(self):
        self.input_click(self.mpu_page.find_pusair_ascertain())

# 业务层
class Mp_PusairBuissens:

    def __init__(self):
        self.mpu_handles = Mp_PusairHandles()

    # 输入内容发布文章
    def mp_pusair_contant(self,title,content,driver,option_name):
        # 输入标题
        self.mpu_handles.input_pusair_title(title)
        # 输入文章内容
        self.mpu_handles.input_pusair_content(content)
        # 点击图片
        self.mpu_handles.input_pusair_picture()
        # 点击下拉列表控件
        self.mpu_handles.select_option(driver,'请选择',option_name)
        # 点击确认
        self.mpu_handles.input_pusair_ascertain()
        time.sleep(2)