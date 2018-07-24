import math
p2 = math.pi*2

def source(func):
    def outer(n, t, res=200):
        r = float(res)
        return [
            func(n, (t+x/r) % 1)
            for x in range(res)
        ]
    return outer

@source
def circle(n, t):
    phi = n*p2*t
    return (math.cos(phi), math.sin(phi))
