from draw import render, plan_basic
from bottle import route, run, response
import colors

colors.configure('''
    #1D395C #DDECFF #FFF
    #442C67 #FFC7FF #FFF
    #243304 #23FF1C #8DFF97
    #7A3129 #C15444 #DD9B98
    #523D0A #EFE77B #F9FEF6 #53BCEA
''')

def serve(seed=None):
    data = render(commands=plan_basic(seed)).getvalue()
    response.set_header('Content-Type', 'image/png')
    response.set_header('Content-Length', len(data))
    return data

@route('/seed/<seed>')
def from_seed(seed):
    return serve(seed)

@route('/random')
def from_rand():
    return serve()

# For debug purposes only
if __name__ == '__main__':
    run(host='localhost', port=8080)
