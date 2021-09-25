import os
from sanic import Sanic
from sanic.response import json
from sanic.exceptions import NotFound
from sanic_openapi import swagger_blueprint

from login import login
from hello import hello

app = Sanic("My first Sanic API")

app.config.API_SECRET = os.environ.get('API_SECRET')
app.config.API_VERSION = '0.0.1'
app.config.API_TITLE = 'My first Sanic API'
app.config.API_TERMS_OF_SERVICE = 'http://example.com'
app.config.API_CONTACT_EMAIL = 'youremail(at)domain.com'
app.config.API_DESCRIPTION = 'Here is the description.'
app.config.API_LICENSE_NAME = 'Here is the license.'
app.config.API_LICENSE_URL = 'http://example.com'
# app.config.API_SECURITY = [{"ApiKeyAuth": []}]
# app.config.API_SECURITY_DEFINITIONS = {
#     "ApiKeyAuth": {"type": "apiKey", "in": "header", "name": "Authorization"}
# }

app.blueprint(login)
app.blueprint(hello)
app.blueprint(swagger_blueprint)

@app.route("/")
async def test(request):
    return json({"info": "Welcome to the API, please visit /swagger/ to get started"})

@app.exception(NotFound)
async def ignore_404s(request, exception):
    return json({"error": "Not found"}, status=404)

async def server_error_handler(request, exception):
    return json({"error": "Server error"}, status=500)

app.error_handler.add(Exception, server_error_handler)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)