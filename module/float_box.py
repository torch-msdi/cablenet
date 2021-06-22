"""
浮箱单元
"""


class FloatBox(object):
    def __init__(self, **kwargs):
        """
        浮箱初始化
        """
        self.shape = kwargs["shape"]
        self.water_level = kwargs["water_level"]
        self.force = kwargs["force"]
        self.position = kwargs["position"]
        self.quality = kwargs["quality"]

    def composition_force(self):
        """
        计算浮箱的合外力，判断浮箱下一个状态
        :return:
        """
        pass

    def buoyancy_by_water_level(self):
        """
        通过水位和浮箱位置来计算浮力
        :return:
        """
        pass

    def box_resistance_in_water(self):
        """
        计算浮箱在水体中非垂向移动时，水体作用在浮箱上的阻力
        :return:
        """
        pass


class FloatBoxSystem(FloatBox):
    """
    浮箱系统，继承浮箱的属性
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __iter__(self):
        """
        浮箱系统中浮箱可迭代
        :return:
        """
        return self

    def __next__(self):
        pass

    def composition_force(self):
        """
        计算浮箱系统的合外力
        :return: 合外力
        """
        pass

    def buoyancy_by_water_level(self):
        """
        计算浮箱系统产生的浮力
        :return: 浮箱系统总浮力
        """
        pass

    def box_resistance_in_water(self):
        """
        浮箱系统非垂向的来自于水体的阻力
        :return: 非垂向水体阻力
        """
        pass
