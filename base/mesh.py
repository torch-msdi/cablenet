import numpy as np
from scipy.interpolate import griddata  # 引入scipy中的二维插值库
from config import mesh_size, xy_range, auto_range, xyz_file_path, interpolate_method, model_path
import re
import logging


class Mesh(object):
    # 地形网格处理
    def __init__(self):
        """
        初始化地形
        """

        # 打开地形文件
        try:
            with open(model_path + "/" + xyz_file_path, 'r') as file:
                self.data = file.readlines()
        except FileNotFoundError:
            logging.error("ERROR 003: 地形文件未找到！")
            raise FileNotFoundError("ERROR 003: 地形文件未找到！")

        # 记录地形文件x, y, z
        self.xy = ([], [])
        self.z = []

        line = 1  # 记录当前行数

        # 向对象的xy及z属性中添加地形数据
        # 检查文件格式是否出错，写入报错日志
        try:
            for sub_data in self.data:
                split_data = re.split("[\t\n]", sub_data)
                self.xy[0].append(float(split_data[0]))
                self.xy[1].append(float(split_data[1]))
                self.z.append(float(split_data[2]))
                line += 1
        except ValueError:
            logging.error(f"ERROR 004: 第{line}行地形文件格式错误！")
            raise FileNotFoundError(f"ERROR 004: 地形文件第{line}行格式错误！")

        # 获取地形边界
        if auto_range:
            self.min_x, self.min_y = min(self.xy[0]), min(self.xy[1])
            self.max_x, self.max_y = max(self.xy[0]), max(self.xy[1])
        else:
            self.min_x, self.min_y = xy_range[0][0], xy_range[0][1]
            self.max_x, self.max_y = xy_range[0][1], xy_range[1][1]
        self.data = self.interpolate_mesh()

    def interpolate_mesh(self):
        # 获取网格大小，插值范围
        logging.info("当前地形范围为x:{}~{}m, y:{}~{}m".format(self.min_x,
                                                        self.max_x,
                                                        self.min_y,
                                                        self.max_y))
        print("当前地形范围为x:{}~{}m, y:{}~{}m".format(self.min_x,
                                                 self.max_x,
                                                 self.min_y,
                                                 self.max_y))

        # 判断网格数量是否超出内存大小
        if auto_range:
            try:
                mesh_x, mesh_y = np.mgrid[self.min_x:self.max_x:mesh_size,
                                          self.min_y:self.max_y:mesh_size]
            except MemoryError:
                logging.error("ERROR 005: 网格数量过多，请增大网格尺寸，或者缩小生成网格范围！")
                raise MemoryError("ERROR 005: 网格数量过多，请增大网格尺寸，或者缩小生成网格范围！")
        else:
            try:
                mesh_x, mesh_y = np.mgrid[xy_range[0][0]:xy_range[1][0]:mesh_size,
                                          xy_range[0][1]:xy_range[1][1]:mesh_size]
            except MemoryError:
                logging.error("ERROR 005: 网格数量过多，请增大网格尺寸，或者缩小生成网格范围！")
                raise MemoryError("ERROR 005: 网格数量过多，请增大网格尺寸，或者缩小生成网格范围！")

        # noinspection PyTypeChecker
        mesh_z = griddata(self.xy, self.z, (mesh_x, mesh_y),
                          method=interpolate_method)

        return [mesh_x, mesh_y, mesh_z]

    def is_on_mesh(self, location):
        """
        判断节点是否位于网格之上，如果是返回True, 否则返回False
        :param location: [x, y ,z]
        :return: bool
        """
        # 获取当前location处网格编号
        number_x = (location[0] - self.min_x)//mesh_size
        number_y = (location[1] - self.min_y)//mesh_size

        # 判断location 是否过小，避免出现负索引仍然可以索引2维数组
        if number_x < 0 or number_y < 0:
            logging.error("ERROR 006: 索网范围超出地形范围")
            raise ValueError("ERROR 006: 索网范围超出地形范围")

        # 找到对应location处地形高程值
        try:
            mesh_z = self.data[2][number_x, number_y]
        except IndexError:
            logging.error("ERROR 006: 索网范围超出地形范围")
            raise ValueError("ERROR 006: 索网范围超出地形范围")

        # 如果location高于地形值，返回2
        if mesh_z == location[2]:
            return 1
        # 如果刚好贴地，返回1
        elif mesh_z > location[2]:
            return 2
        # 在地形以下返回0
        else:
            return 0

    def show(self):
        """
        显示二维网格
        :return: PIC
        """
        pass
