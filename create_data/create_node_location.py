#!/user/bin/python3
# @Author: torch
# -*- coding: utf-8 -*-
# @time: 2021/6/17 9:27
# @File: create_node_location.py
# @email: 947993284@qq.com
import random


def get_displacement_by_coordinate(z, t):
    """
    获取不同时刻、不同Z坐标下节点的位移
    :param z: 竖坐标
    :param t: 时间步
    :return:  对于的y方向位移
    """
    move_step = z*(20-z)/100
    time_move_step = t*(20-t)/200 + 1
    return move_step*time_move_step


result = {
    "time": [i for i in range(20)],
    "water_level": [round(20 + random.uniform(-200, 200)/400, 2) for j in range(20)],
    "data": []
}


def get_relationship(node_index):
    result_list = []
    row = node_index//10
    column = node_index % 10
    if row == 0:
        if column == 0:
            result_list.append(10)
            result_list.append(1)
        elif column == 9:
            result_list.append(" ")
