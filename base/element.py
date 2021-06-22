import numpy as np
try:
    import log.report
except ImportError:
    raise ImportError("日志模块初始化错误")
import logging


class Node(object):
    __gravity = np.zeros((1, 3))  # 节点重力
    __internal = np.zeros((1, 3))  # 节点杆件内力
    __support = np.zeros((1, 3))  # 节点支持力
    __friction = np.zeros((1, 3))  # 节点摩擦力
    __buoyancy = np.zeros((1, 3))  # 节点所受浮力
    __water_pressure = np.zeros((1, 3))  # 节点所受等效水压力
    __water_resistance = np.zeros((1, 3))  # 节点所受水体运动阻力
    __external_force = np.zeros((1, 3))  # 节点所受合外力

    def __init__(self, **kwargs):
        # 初始化节点对象，由node.info文件提供节点信息
        try:
            self.index = kwargs["节点编号"]
            self.quality = kwargs["节点质量"]
            self.location = kwargs["节点初始位置"]
            self.velocity = kwargs["节点初始速度"]
            self.is_anchor = kwargs["是否为锚固点"]
            self.is_ordinary_pontoon = kwargs["是否为普通浮箱"]
            self.is_tower_pontoon = kwargs["是否为索塔浮箱"]
            self.pontoon_shape = kwargs["浮箱形状"]
        except KeyError:
            logging.error("ERROR 001: node.info 文件格式错误")
