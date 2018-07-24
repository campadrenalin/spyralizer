def via_cairo(w, h, points):
    import cairo
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
    ctx = cairo.Context(surface)
    ctx.scale(w, h)
    ctx.set_source_rgb(0,0,0)
    ctx.rectangle(0, 0, 1, 1)
    ctx.fill()

    ctx.set_source_rgb(1,1,1)
    ctx.set_line_width(0.01)
    for x, y in points:
        ctx.line_to(0.5+x/2,0.5+y/2)
    ctx.close_path()
    ctx.stroke()
    surface.write_to_png('example.png')
