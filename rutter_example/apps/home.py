import os

from pyramid.config import Configurator


def main(global_config, **settings):

    with Configurator(settings=settings, package="rutter_example") as config:

        # ~~~~~ #
        config.include("pyramid_jinja2")
        config.add_jinja2_search_path(
            "rutter_example:templates/", prepend=True
        )

        # ~~~~~ #
        # add home routes
        config.include(".routes.home")

        # ~~~~~ #
        # scan for and register home views
        config.scan(".views.home")

    return config.make_wsgi_app()
