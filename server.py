from draw import render, plan_basic
from bottle import route, run, response

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

if __name__ == '__main__':
    run(host='localhost', port=8080)
