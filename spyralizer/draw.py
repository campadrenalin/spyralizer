from spyralizer.seed import from_string
from spyralizer.transforms import *
from spyralizer import sources, colors
import random

def plan_basic(seed=None, src_choices=sources.choices, trans=(downscale, rotate, scale), size=256):
    if seed:
        with from_string(seed):
            return plan_basic(None)
    src_func = random.choice(src_choices)
    points = src_func(random.randint(2,7), random.random(), res=size*5)
    for transformation in trans:
        points = transformation(random.randint(4,7), random.random(), points)
    cols = random.choice(colors.palettes)

    commands = [('background', cols[0]) ]
    for i, col in enumerate(cols[1:]):
        commands.append( ('lines', col, scale(5-3*i, 0, points)) )
    return commands

class Cairo(object):
    def __init__(self, w, h):
        import cairo
        self.w = w
        self.h = h
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
        self.ctx = cairo.Context(self.surface)
        self.ctx.scale(self.w, self.h)

    def background(self, color):
        self.ctx.set_source_rgb(*color)
        self.ctx.rectangle(0, 0, 1, 1)
        self.ctx.fill()

    def lines(self, color, points):
        self.ctx.set_source_rgb(*color)
        self.ctx.set_line_width(0.01)
        for x, y in points:
            self.ctx.line_to(0.5+x/2,0.5+y/2)
        self.ctx.close_path()
        self.ctx.stroke()

    def finish(self, fobj):
        import cStringIO
        fobj = fobj or cStringIO.StringIO()
        self.surface.write_to_png(fobj)
        return fobj

def render(backend=Cairo, size=256, commands=[], fobj=None):
    b = backend(size, size)
    for command in commands:
        ctype, args = command[0], command[1:]
        getattr(b, ctype)(*args)
    return b.finish(fobj)
