import math
p2 = math.pi*2

choices = []

def source(func):
    def outer(n, t, res=200):
        r = float(res)
        return [
            func(n, (t+x/r) % 1)
            for x in range(res)
        ]
    choices.append(outer)
    return outer

@source
def circle(n, t):
    phi = n*p2*t
    return (math.cos(phi), math.sin(phi))

@source
def reverse_circle(n, t):
    phi = -n*p2*t*5
    return (math.cos(phi), math.sin(phi))

@source
def flat(n, t):
    phi = n*p2*t
    return (2*math.cos(phi), 0)

def lerp(a, b, percent):
    percent = float(percent)
    inverse = 1-percent
    return (
        a[0]*inverse + b[0]*percent,
        a[1]*inverse + b[1]*percent,
    )

def path(n, t, possibles):
    l = len(possibles)
    progress = (n*l*t) % l
    percent, sector = math.modf(progress)
    sector = int(sector)
    s_next = (sector+1) % l
    return lerp(possibles[sector], possibles[s_next], percent)

@source
def cross(n, t):
    return path(n, t, [
        (-1, -1),
        (0, 0),
        (-1,  1),
        (0, 0),
        ( 1,  1),
        (0, 0),
        ( 1, -1),
        (0, 0),
    ])

@source
def triangle(n, t):
    return path(3*n, t, [
        (0, -1),
        (-1,  1),
        ( 1,  1),
    ])

@source
def tan(n, t):
    phi = -n*p2*t
    return (math.tan(phi), math.atan(phi))

@source
def saw(n, t):
    if n <= 3:
        n = -n
    x = (n*t*2) % 1 - 0.5
    return (x,x)

@source
def jag(n, t):
    x = math.floor(n*t*5) % 5
    return (x,x)

@source
def wobble1(n, t):
    return (math.cos(n*t*p2*7)*5, 0)

@source
def wobble2(n, t):
    return (math.cos(n*t*p2*7)*3, math.sin(n*t*p2*5)*3)

#choices = (circle,)
