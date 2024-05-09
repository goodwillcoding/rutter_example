from datetime import datetime

from pyramid.view import view_config


@view_config(
    route_name="home_route", renderer="rutter_example:templates/home.jinja2"
)
def hello_home(request):
    return {"data": datetime.now()}
