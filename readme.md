Here is a basic Sanic API with JWT auth, exceptions handling, versioning and OpenAPI doc.

## How to use it?
1. `docker-compose -f docker-compose.yml up --build`
2. Open http://localhost:8000/swagger/#/ to see the OpenAPI doc
2. Use Postman or curl get a token at localhost:8000/v1/login (POST)
3. Query localhost:8000/v1/hello (GET) to see a Hello World
4. Query localhost:8000/v1/hello?name=Clément (GET) to see a Hello Clément
5. Keep adding more name query parameters : localhost:8000/v1/hello?name=Clément&name=Other1&name=Other2 ...

## Resources:
- https://www.twilio.com/blog/2016/12/getting-started-with-sanic-the-asynchronous-uvloop-based-web-framework-for-python-3-5.html
- https://sanicframework.org/en/guide/deployment/running.html#sanic-server
- https://sanicframework.org/en/guide/best-practices/blueprints.html#listeners
- https://sanic-openapi.readthedocs.io/en/latest/sanic_openapi2/configurations.html