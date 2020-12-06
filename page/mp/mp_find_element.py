#-*-coding:utf-8 -*-
from selenium.webdriver.common.by import By


class Mp_Find_Element:

    # 控件里面的元素
    article_kongjian = ".el-select-dropdown__item span"
    # ...............登陆.......................
    # 用户名
    login_username = (By.CSS_SELECTOR,"[placeholder='请输入手机号']")
    # 密码
    login_code = (By.CSS_SELECTOR,"[placeholder='验证码']")
    # 登陆
    login_button = (By.XPATH,"//*[text()='登录']")
    # ...............首页.......................
    # 内容管理
    home_content = (By.XPATH,"//*[text()='内容管理']")
    # 发布文章
    home_article = (By.XPATH,"//*[contains(text(),'  发布文章')]")
    # ...............文章页.......................
    # 文章标题
    article_title = (By.CSS_SELECTOR,"[placeholder='文章名称']")
    # 进入ifram子页面
    article_ifram = (By.CSS_SELECTOR,"#publishTinymce_ifr")
    # 输入文章内容
    article_content = (By.CSS_SELECTOR,"body")
    # 点击选择图片
    article_choose_picture = (By.CSS_SELECTOR,".title")
    # 点击图片
    article_picture = (By.CSS_SELECTOR,".img_list img")
    # 点击确定
    article_ascertain = (By.XPATH,"//*[text()='确 定']")
    # 发表
    article_fabiao = (By.XPATH,"//*[text()='发表']")