import jwt
from sanic import Blueprint
from sanic.response import json

login = Blueprint("login", url_prefix="/login", version=1)

@login.post("/")
async def do_login(request):
    token = (jwt.encode({}, request.app.config.API_SECRET)).decode("utf-8")

    return json({"token": token})