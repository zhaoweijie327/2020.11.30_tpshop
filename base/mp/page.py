from page.mp.home_page import Mp_HomeBuissens
from page.mp.login_page import Mp_LoginBuissens
from page.mp.pusair_page import Mp_PusairBuissens


class Page:

    @classmethod
    def get_login_page(cls):
        '''
        登陆
        :return:
        '''
        return Mp_LoginBuissens()

    @classmethod
    def get_home_page(cls):
        '''
        内容管理
        :return:
        '''
        return Mp_HomeBuissens()

    @classmethod
    def get_pusair_page(cls):
        '''
        发布内容
        :return:
        '''
        return Mp_PusairBuissens()
