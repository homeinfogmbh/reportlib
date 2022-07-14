"""Reportlib configuration."""

from functools import cache, partial

from configlib import load_config


__all__ = ['CONFIG_FILE', 'get_config']


CONFIG_FILE = 'comcat.conf'
get_config = partial(cache(load_config), CONFIG_FILE)
