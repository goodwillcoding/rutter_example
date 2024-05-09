from datetime import datetime

from pyramid.view import view_config


@view_config(
    route_name="alpha_route",
    request_method="GET",
    renderer="json",
    openapi=True,
)
def hello_alpha(request):
    return {"response": "Hello, Alpha %s" % datetime.now()}
