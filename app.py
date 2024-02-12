#!/usr/bin/env python

from django.core.management import execute_from_command_line

from coltrane import initialize

wsgi = initialize(
    **{
        "INSTALLED_APPS": ["htmx_extensions"],
    }
)

if __name__ == "__main__":
    execute_from_command_line()
