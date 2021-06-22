import re
import json
import numpy as np


def generate_matrix(path):
    with open(path, 'r') as f:
        data = f.readlines()
        f.close()


with open("model_example/lever.info", 'r', encoding="utf-8") as f:
    data = f.readlines()
    f.close()


result = {}
for number in range(len(data)-1):
    result[number+1] = json.loads(re.split("[\t\n]", data[number+1].strip())[1])

dim = len(result)
result_matrix = np.zeros((dim, dim))
for i in result:
    for j in result[i]:
        result_matrix[i-1, j] = 1
max_number = 0
for lever in result:
    for node in result[lever]:
        if node > max_number:
            max_number = node

node_matrix = np.zeros((max_number, max_number))
for lever in result:
    node_matrix[result[lever][0] - 1, result[lever][1] - 1] = 1
    node_matrix[result[lever][1] - 1, result[lever][0] - 1] = 1
c = 1
