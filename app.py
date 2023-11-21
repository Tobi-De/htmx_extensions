#!/usr/bin/env python

from django.core.management import execute_from_command_line

from coltrane import initialize
from os import getenv


wsgi = initialize(**{"STATIC_URL": getenv("STATIC_URL", "static/")})

if __name__ == "__main__":
    execute_from_command_line()
