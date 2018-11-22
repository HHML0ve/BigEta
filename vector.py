# -*- coding: utf-8 -*-
import math


class CVector(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "%s, %s" % (self.x, self.y)

    def __sub__(self, other):
        return super(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return super(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return super(self.x * other.x, self.y * other.y)

    def __divmod__(self, other):
        return super(self.x / other.x, self.y / other.y)

    @classmethod
    def from_points(cls, p1, p2):
        return cls(p2[0] - p1[0], p2[1] - p1[1])

    # 计算模长
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # 规范化
    def normalize(self):
        magnitude = self.magnitude()
        self.x /= magnitude
        self.y /= magnitude
