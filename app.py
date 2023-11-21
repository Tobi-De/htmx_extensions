#!/usr/bin/env python

from django.core.management import execute_from_command_line

from coltrane import initialize, DEFAULT_INSTALLED_APPS

wsgi = initialize(
    **{
        "INSTALLED_APPS": ["htmx_extensions"] + DEFAULT_INSTALLED_APPS,
    }
)

if __name__ == "__main__":
    execute_from_command_line()
