"""
日志系统
版本： 1.01
创建日期： 2021/02/15
"""

import logging.handlers
import config


with open(config.model_path + "/log.log", 'w') as f:
    f.close()


logger = logging.getLogger()  # 报错日志模块
logger.setLevel(logging.DEBUG)  # 日志级别DEBUG
formatter = logging.Formatter("%(message)s")  # 输出日志格式

path = config.model_path + "/log.log"  # 报错日志文件路径

handler = logging.FileHandler(filename=path)
handler.setFormatter(formatter)
logger.addHandler(handler)
