from datetime import datetime

from pyramid.view import view_config


@view_config(
    route_name="bravo_route",
    request_method="GET",
    renderer="json",
    openapi=True,
)
def hello_bravo(request):
    return {"response": "Hello Bravo %s" % datetime.now()}
