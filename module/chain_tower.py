"""
索塔单元
"""
from float_box import FloatBox


class ChainTower(FloatBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_height = kwargs["max_height"]
        self.min_height = kwargs["min_height"]

    def composition_force(self):
        """
        计算索塔浮箱收到的合外力，水平方向合外力自动归零
        :return:
        """
