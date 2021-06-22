#!/user/bin/python3
# @Author: torch
# -*- coding: utf-8 -*-
# @time: 2021/6/17 9:14
# @File: create_terrain.py
# @email: 947993284@qq.com


def get_altitude_by_x(data):
    return round(-0.2*data, 2)


result = "x" + "\t" + "y" + "\t" + "z" + "\n"

for i in range(40):
    for j in range(60):
        result += str(j-30) + "\t" + str(i) + "\t" + str(get_altitude_by_x(j-30)) + "\n"

with open('terrain.xyz', "w") as f:
    f.write(result)

