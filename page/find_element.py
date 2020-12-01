'''
管理定位元素
'''
from selenium.webdriver.common.by import By


class Find_Element:

    # .................首页.................
    # 登陆按钮
    home_login = (By.CSS_SELECTOR,'.red')
    # 搜索框
    home_search = (By.ID,'q')
    # 搜索按钮
    home_search_button = (By.CSS_SELECTOR,'.ecsc-search-button')
    # 我的订单
    home_order = (By.LINK_TEXT,'我的订单')
    # 鼠标移动到购物车按钮
    home_cart = (By.ID,'#hd-my-cart')
    # 点击去购物车结算
    home_cart_settlement = (By.CSS_SELECTOR,'.c-btn')
    # 获取产品名称  .goods-name
    home_cart_pname = (By.CSS_SELECTOR,'.goods-name')

    # .................登录页.................
    # 获取登录页面信息
    login_welcome = (By.CSS_SELECTOR,'.login-welcome')
    # 用户名
    login_name = (By.ID,'#username')
    # 密码
    login_pwd = (By.ID,'#password')
    # 验证码
    login_code = (By.ID,'#verify_code')
    # 点击登陆
    login_button = (By.CSS_SELECTOR,'.J-login-submit')

    # .................个人资料页.................
    # 点击个人资料
    personal_data = (By.LINK_TEXT,'个人信息')
    # 修改用户姓名
    personal_nickname = (By.ID,'nickname')
    # 点击确认保存
    personal_save = (By.CLASS_NAME,'save')

    # .................产品详细页面.................
    # 点击产品名字
    product_name = (By.LINK_TEXT,'小米9')
    # 点击加入购物车
    product_cart = (By.CSS_SELECTOR,'#join_cart')
    # 点击立即购买 join_cart_now
    product_immediately_cart = (By.CSS_SELECTOR,'#join_cart_now')
    # 切换ifram页面 #layui-layer-iframe1
    product_ifram = (By.CSS_SELECTOR,'#layui-layer-iframe1')
    # 获取添加成功信息
    personal_success = (By.CSS_SELECTOR,'.conect-title span')

    # .................购物车/立即购买页面.................
    # 点击结算
    s_cart_settlement = (By.CSS_SELECTOR,'.sc-acti-list .gwc-qjs')
    # 提交订单
    s_cart_submit_order = (By.CSS_SELECTOR,'.gwc-qjs span')

    # .................我的订单页面.................
    # 点击立即支付
    my_order_pay = (By.CSS_SELECTOR,'.ps_lj')

    # .................支付页面.................
    # 获取订单提交成功信息
    pay_order = (By.CSS_SELECTOR,'.erhuh h3')
    # 点击货到付款
    pay_delivery = (By.CSS_SELECTOR,"[value='pay_code=cod']")
    # 点击确认支付
    pay_confirm = (By.CSS_SELECTOR,'.button-confirm-payment')
    # 获取成功支付信息
    success_pay = (By.CSS_SELECTOR, '.erhuh h3')