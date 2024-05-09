import os

from pyramid.config import Configurator


def main(global_config, **settings):

    with Configurator(settings=settings) as config:

        # ~~~~~ #
        # add and configure alpha OpenAPI
        config.include("pyramid_openapi3")
        config.pyramid_openapi3_spec(
            os.path.realpath(
                os.path.join(
                    os.path.dirname(__file__), "..", "openapi", "alpha.yaml"
                )
            ),
            route="/spec",
        )
        config.pyramid_openapi3_add_explorer(route="/")

        # ~~~~~ #
        # add alpha routes
        config.include("..routes.alpha")

        # ~~~~~ #
        # scan for and register alpha views
        config.scan("..views.alpha")

    return config.make_wsgi_app()
