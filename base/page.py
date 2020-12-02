from page.addcart_page import AddcartBuissens
from page.home_page import HomeBuissens
from page.login_page import LoginBuissens
from page.myorder_page import MyorderBuissens
from page.product_page import ProductBuissens


class Page:

    @classmethod
    def get_home_page(cls):
        '''
        .................首页.................
        :return:
        '''
        return HomeBuissens()

    @classmethod
    def get_login_page(cls):
        '''
        .................登陆.................
        :return:
        '''
        return LoginBuissens()

    @classmethod
    def get_product_page(cls):
        '''
        # .................产品详细页面.................
        :return:
        '''
        return ProductBuissens()

    @classmethod
    def get_addcart_page(cls):
        '''
        # .................购物车结算/提交页面.................
        :return:
        '''
        return AddcartBuissens()

    @classmethod
    def get_myorder_page(cls):
        '''
        # .................支付.................
        :return:
        '''
        return MyorderBuissens()