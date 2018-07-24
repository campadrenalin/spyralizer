import math
p2 = math.pi*2

def transform(func):
    def outer(n, t, src):
        l = float(len(src))
        return [
            func(n, (t+i/l) % 1, point)
            for i, point in enumerate(src)
        ]
    return outer

@transform
def downscale(n, t, point):
    scaled = (point[0]/n, point[1]/n)
    downward = 1-(float(1)/n)
    return (scaled[0], scaled[1] + downward)

@transform
def rotate(n, t, point):
    phi = n*t*p2
    s = math.sin(phi)
    c = math.cos(phi)
    return (
        point[0]*c - point[1]*s,
        point[0]*s + point[1]*c,
    )
