import os

from pyramid.config import Configurator


def main(global_config, **settings):

    with Configurator(settings=settings) as config:

        # ~~~~~ #
        # add and configure bravo OpenAPI
        config.include("pyramid_openapi3")
        config.pyramid_openapi3_spec(
            os.path.realpath(
                os.path.join(
                    os.path.dirname(__file__), "..", "openapi", "bravo.yaml"
                )
            ),
            route="/spec",
        )
        config.pyramid_openapi3_add_explorer(route="/")

        # ~~~~~ #
        # add bravo routes
        config.include("..routes.bravo")

        # ~~~~~ #
        # scan for and register bravo views
        config.scan("..views.bravo")

    return config.make_wsgi_app()
