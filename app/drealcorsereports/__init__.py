"""Main entry point
"""
from pyramid.config import Configurator


def main(global_config, **settings):
    del global_config
    config = Configurator(settings=settings)

    config.include("drealcorsereports.models.includeme")
    config.include("drealcorsereports.security")
    config.include("cornice")

    config.scan("drealcorsereports.views")

    return config.make_wsgi_app()
