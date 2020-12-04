'''
路径获取
日志编写
'''
import os
import logging.handlers

# 获取路径
import time

BAS_URL = os.path.abspath(os.path.dirname(__file__))

TITLE = None

# 日志
def log():
    # 创建日志器对象
    rizhi = logging.getLogger()
    rizhi.setLevel(level=logging.INFO)
    # 创建处理器
    lht = logging.handlers.TimedRotatingFileHandler(BAS_URL + '/log/log{}.log'.format(int(time.time() * 1000)),when='M',interval=1,backupCount=2)
    ls = logging.StreamHandler()
    # 创建格式化器对象
    fmt_name = '%(asctime)s %(levelname)s [%(name)s] ' \
               '[%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt=fmt_name)
    # 给处理器设置格式化器
    lht.setFormatter(formatter)
    # 给日志器添加处理器
    rizhi.addHandler(lht)
    rizhi.addHandler(ls)