from selenium.webdriver.common.by import By


class Mp_Find_Element:

    xpath = "//*[contains(text(),'{}')]"

    # ...............��½.......................
    # �û���
    login_username = (By.CSS_SELECTOR,"[placeholder='�������ֻ���']")
    # ����
    login_code = (By.CSS_SELECTOR,"[placeholder='��֤��']")
    # ��½
    login_button = (By.XPATH,"//*[text()='��¼']")
    # ...............��ҳ.......................
    # ���ݹ���
    home_content = (By.XPATH,"//*[text()='���ݹ���']")
    # ��������
    home_article = (By.XPATH,"//*[contains(text(),'  ��������')]")
    # ...............����ҳ.......................
    # ���±���
    article_title = (By.CSS_SELECTOR,"[placeholder='��������']")
    # ����ifram��ҳ��
    article_ifram = (By.CSS_SELECTOR,"#publishTinymce_ifr")
    # ������������
    article_content = (By.CSS_SELECTOR,"#tinymce br")
    # ���ѡ��ͼƬ
    article_choose_picture = (By.CSS_SELECTOR,".title")
    # ���ͼƬ
    article_picture = (By.CSS_SELECTOR,".img_list img")
    # �ؼ������Ԫ��
    article_kongjian = ".el-select-dropdown__item span"
    # ���ȷ��
    article_ascertain = (By.XPATH,"//*[text()='ȷ ��']")
