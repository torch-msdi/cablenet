import numpy as np
import config
from material.material import material_data
from base.mesh import Mesh

try:
    import log.report
except ImportError:
    raise ImportError("日志模块初始化错误")
import logging


class NodeForce(object):
    # 节点的受力属性，只能用类中的私有方法修改
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

        if self.is_tower_pontoon and self.is_anchor:
            logging.error(
                "ERROR 201：节点编号{}，节点类型无法同时为索塔浮箱及锚固点".format(
                    self.index))
            raise TypeError(
                "ERROR 201：节点编号{}，节点类型无法同时为索塔浮箱及锚固点".format(
                    self.index))
        if self.is_ordinary_pontoon and self.is_tower_pontoon:
            logging.error(
                "ERROR 202：节点编号{}，节点类型无法同时为索塔浮箱及普通浮箱".format(
                    self.index))
            raise TypeError(
                "ERROR 202：节点编号{}，节点类型无法同时为索塔浮箱及普通浮箱".format(
                    self.index))
        if self.is_ordinary_pontoon and self.is_anchor:
            logging.error(
                "ERROR 203：节点编号{}，节点类型无法同时为锚固点及普通浮箱".format(
                    self.index))
            raise TypeError(
                "ERROR 203：节点编号{}，节点类型无法同时为锚固点及普通浮箱".format(
                    self.index))

    def gravity_force(self):
        # 修正节点重力
        try:
            self.__gravity[0, 2] = self.quality * \
                config.acceleration_of_gravity  # 计算节点所受重力
        except ValueError:
            logging.error("ERROR 204: 节点质量必须为数字")

    def internal_force(self):
        # 修改杆件内力
        pass

    def support_force(self):
        # 修改节点所受地面支持力支持力
        pass

    def friction_force(self):
        # 修改节点所受地面摩擦力
        pass

    def buoyancy_force(self):
        # 修改节点所受水体浮力
        pass

    def water_pressure_force(self):
        # 修改节点所受等效水压力
        pass

    def water_resistance_force(self, water_speed, velocity, water_level):
        # 修改节点运动所受水体阻力
        if self.is_ordinary_pontoon:
            relative_velocity = velocity - water_speed

    def external_force(self):
        assert self
        # 计算节点所受的合外力
        self.__external_force = self.__gravity + self.__internal + self.__support + \
            self.__friction + self.__buoyancy + \
            self.__water_pressure + self.__water_resistance

    def calculate_step(self):
        # 每一步对应的受力整合计算
        self.gravity_force()
        self.internal_force()
        self.support_force()
        self.friction_force()
        self.buoyancy_force()
        self.water_pressure_force()
        self.water_resistance_force()
        self.external_force()


class LeverForce(object):
    # 杆件的受力属性
    __internal_force = np.zeros((1, 3))  # 杆件所受内力

    def __init__(self, **kwargs):
        try:
            self.index = kwargs["杆件编号"]  # 杆件编号
            self.elastic_modulus = kwargs["杆件弹性模量"]  # 杆件弹性模量
            self.max_stress = kwargs["杆件最大应力"]  # 杆件最大应力，即断裂应力
            self.natural_length = kwargs["自然长度"]  # 杆件在不受外力作用时的长度
        except KeyError:
            logging.error("ERROR 002: lever.info 文件格式错误")

    def strain_stress(self):
        pass

    def is_fracture(self):
        # 判断杆件在当前受力条件下是否发生断裂
        if self.__internal_force >= self.max_stress:
            return True
        else:
            return False
