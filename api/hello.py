import jwt
from sanic import Blueprint
from sanic.response import json
from sanic_openapi import doc

from auth import protected

hello = Blueprint("hello", url_prefix="/hello", version=1)

@hello.get('/')
@doc.consumes(doc.String(name="name"), location="query")
@protected
async def test(request):
    args = request.args
    if 'name' in args:
        names = [name for name in args['name'] if name is not None]
        helloTarget = str(names[0]) if len(names) == 1 else '%s and %s' % (', '.join(names[0:len(names)-1]), str(names[len(names)-1:len(names)][0]))
    else:
        helloTarget = 'world'

    return json({'info': 'Hello %s' % helloTarget, 'args': args})