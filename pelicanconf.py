#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

RELATIVE_URLS = False

AUTHOR = 'Taell'
SITENAME = 'Taell'
#SITEURL = ''
PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# pagination
DEFAULT_PAGINATION = False

THEME = './theme'

# Delete the output directory before generating new files.
DELETE_OUTPUT_DIRECTORY = True

# dont create following standard pages
AUTHORS_SAVE_AS = None
ARCHIVES_SAVE_AS = None
CATEGORIES_SAVE_AS = None
TAGS_SAVE_AS = None

# keep this for access to page variable
DIRECT_TEMPLATES = []

# copy robots.txt to root
STATIC_PATHS = ['extra'] 
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/.htaccess': {'path': '.htaccess'},
}
