# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'hwp'
SITENAME = u'DDC#DACBF#GDGB'
SITEURL = 'hwp.github.io'

PATH = 'content'
STATIC_PATHS = ['images', 'css']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('github', 'https://github.com/hwp'), )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# theme
THEME = 'pelican-clean-blog'

HEADER_COVER = 'images/home_bg.jpg'
CSS_OVERRIDE = 'css/myblog.css'
