from sources import circle
from transforms import *
from draw import via_cairo
import random

def randomized(size=100):
    points = circle(random.randint(2,7), random.random(), res=size*5)
    for transformation in (downscale, rotate):
        points = transformation(random.randint(2,7), random.random(), points)
    via_cairo(size, size, points)

randomized()
