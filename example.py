import sources
from transforms import *
from draw import via_cairo
import random

def randomized(size=100):
    src_func = random.choice(sources.choices)
    points = src_func(random.randint(2,7), random.random(), res=size*5)
    for transformation in (downscale, rotate, scale):
        points = transformation(random.randint(4,7), random.random(), points)
    via_cairo(size, size, points)

randomized(256)
