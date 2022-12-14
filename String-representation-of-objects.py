#!/bin/python

import math
import os
import random
import re
import sys


class Car:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Car with the maximum speed of {} {}".format(self.a,self.b)

class Boat:
    def __init__(self,a):
        self.a = a
    def __str__(self):
        return "Boat with the maximum speed of {} knots".format(self.a)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(raw_input())
    queries = []
    for _ in xrange(q):
        args = raw_input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("invalid vehicle type")
        fptr.write("%s\n" % vehicle)
    fptr.close()
