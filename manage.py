import time
from sanic import Sanic
from sanic.response import  text,html
from jinja2 import Environment, PackageLoader

app = Sanic(__name__)
app.static('/static','./static')
env = Environment(loader=PackageLoader(__name__, 'templates'))

@app.route('/hh')
async def hh(request):
    # return text(str(request.url))
    return html(env.get_template('index.html').render(var='World'))

if __name__ == '__main__':
    app.run(port=8000,debug=True)