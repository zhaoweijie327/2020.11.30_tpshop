'''
����poģʽ��ҳ���Ϊ���㣨���󡢲�����ҵ��
'''
import time

from base.base_driver import DriverBase, DriverHandles
from page.mp.mp_find_element import Mp_Find_Element


# �����
class Mp_PusairPage(DriverBase):

    def __init__(self):
        super().__init__()

    # ��λ���±���
    def find_pusair_title(self):
        return self.find_elemnet(Mp_Find_Element.article_title)

    # ��λiframҳ��
    def find_pusair_ifram(self):
        return self.find_elemnet(Mp_Find_Element.article_ifram)

    # ��λiframҳ��
    def find_pusair_content(self):
        return self.find_elemnet(Mp_Find_Element.article_content)

    # ��λѡ��ͼƬ
    def find_pusair_choose_picture(self):
        return self.find_elemnet(Mp_Find_Element.article_choose_picture)

    # ��λͼƬ
    def find_pusair_picture(self):
        return self.find_elemnet(Mp_Find_Element.article_picture)

    # ��λȷ��
    def find_pusair_ascertain(self):
        return self.find_elemnet(Mp_Find_Element.article_ascertain)

# ������
class Mp_PusairHandles(DriverHandles):

    def __init__(self):
        self.mpu_page = Mp_PusairPage()

    # ģ��д�����±���
    def input_pusair_title(self,title):
        self.input_senk(self.mpu_page.find_pusair_title(),title)

    # ģ��д����������
    def input_pusair_content(self,content):
        # ������ҳ��
        self.input_ifram(self.mpu_page.driver,self.mpu_page.find_pusair_ifram())
        # д������
        self.input_senk(self.mpu_page.find_pusair_content(),content)
        # �˳���ҳ��
        self.mpu_page.driver.switch_to.default_content()

    # ģ����ͼƬ
    def input_pusair_picture(self):
        self.input_click(self.mpu_page.find_pusair_choose_picture())
        self.input_click(self.mpu_page.find_pusair_picture())

    # ģ����ȷ��
    def input_pusair_ascertain(self):
        self.input_click(self.mpu_page.find_pusair_ascertain())

# ҵ���
class Mp_PusairBuissens:

    def __init__(self):
        self.mpu_handles = Mp_PusairHandles()

    # �������ݷ�������
    def mp_pusair_contant(self,title,content,driver,option_name):
        # �������
        self.mpu_handles.input_pusair_title(title)
        # ������������
        self.mpu_handles.input_pusair_content(content)
        # ���ͼƬ
        self.mpu_handles.input_pusair_picture()
        # ��������б�ؼ�
        self.mpu_handles.select_option(driver,'��ѡ��',option_name)
        # ���ȷ��
        self.mpu_handles.input_pusair_ascertain()
        time.sleep(2)