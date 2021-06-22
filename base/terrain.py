import re

with open("model_example/terrain.xyz", 'r') as f:
    content = f.readlines()
    f.close()


class Terrain(object):
    def __init__(self, filepath):
        self.filepath = filepath


