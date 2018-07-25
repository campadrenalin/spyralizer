'''
Default config:
    #000 #222 #FFF
'''
import re

palettes = []
patterns = re.compile(r'#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}')

def interpret_color(cstr):
    if re.match('#[0-9a-fA-F]{6}', cstr):
        chunks = re.findall(r'..', cstr.lstrip('#'))
        return tuple(int(x, 16)/float(0xff) for x in chunks)
    elif re.match('#[0-9a-fA-F]{3}', cstr):
        chunks = cstr.lstrip('#')
        return tuple(int(x, 16)/float(0xf) for x in chunks)

def configure(conf):
    global palettes
    palettes = []
    for line in conf.split("\n"):
        found = patterns.findall(line)
        if found:
            palettes.append([interpret_color(x) for x in found])

configure('#000 #222 #FFF')
