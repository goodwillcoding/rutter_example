##########################################
Rutter / Pyramid / OpenAPI Example Project
##########################################

Example integration of Rutter with Pyramid including pyramid_openapi3
add on with 2 different API schemas and homepage that greets you

Very useful when you want to separate api endpoints defined in one project with
separate specs, auth and so on and so on.

In this example two API, Alpha and Bravo exist.
- Alpha is available on /
- Bravo is avaailable on /bravo

Each application has a /test api endpoint and OpenAPI explorer is available
for each.

Folder structure for the API is flat, component based, code is NOT organized
in specific app "super" folder. But that is easy enough to do.


How it works
============


This uses Rutter (https://rutter.rtfd.io/) package to mount two different
Pyramid WSGI applications as a composite WSGI application.

Each application has it's own Pyramid configurator to which pyramid_openapi3
is included and "attached" to.

One server, waitress runs both, two are not required.

Endpoints are defined in pyproject pyproject.toml (they could be defined in
setup.py as an alternative)

Single Pyramid application would be defined in `[app:main]`. But when there are
more then one application they each get their own block, not `main` one.
Each app has it's own settings which is heavily useful for example if debugtoolbar is not needed for one of the apps

.. code-block:: ini

    [app:home]
    # home endpoint is defined in pyproject.toml, in
    # [tool.poetry.plugins."paste.app_factory"] section
    use = egg:rutter_example#home

    pyramid.reload_templates = true
    pyramid.debug_authorization = false
    pyramid.debug_notfound = false
    pyramid.debug_routematch = false
    pyramid.default_locale_name = en
    pyramid.includes =
        pyramid_debugtoolbar

    [app:alpha]
    # alpha endpoint is defined in pyproject.toml, in
    # [tool.poetry.plugins."paste.app_factory"] section
    use = egg:rutter_example#alpha

    pyramid.reload_templates = true
    pyramid.debug_authorization = false
    pyramid.debug_notfound = false
    pyramid.debug_routematch = false
    pyramid.default_locale_name = en
    pyramid.includes =
        pyramid_debugtoolbar

    [app:bravo]
    # bravo endpoint is defined in pyproject.toml, in
    # [tool.poetry.plugins."paste.app_factory"] section
    use = egg:rutter_example#bravo

    pyramid.reload_templates = true
    pyramid.debug_authorization = false
    pyramid.debug_notfound = false
    pyramid.debug_routematch = false
    pyramid.default_locale_name = en
    pyramid.includes =
        pyramid_debugtoolbar


Change, renaming of any endpoints in pyproject.toml means you need to re-run
installation of the application. In this project using `poetry install`


Getting Started
===============

Clone the repository:

.. code:: shell

    git clone https://github.com/goodwillcoding/rutter_example


Install via poetry

.. code:: shell

    poetry install

Run Server

.. code:: shell

    poetry run pserve ./development.ini --reload


Gotchas
=======

Pyramid proutes, pview and likely other command only show routes for one of the applications, the last one to be defined (i.e. bravo)
That could prolly be updated by specifying parameter to those commands to indicate which app.

