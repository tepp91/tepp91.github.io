#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGINS = [
    'pelican_gist',
]

AUTHOR = 'Tepp'
SITENAME = "Tepp's note"
SITEURL = ''
SITEDESC = "ソフトウェア（主にゲーム）開発中に調べた事を、備忘録として記録しているWebサイトです。"
TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'Japanese'

PATH = 'content'

DIRECT_TEMPLATES = ['index']

AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
ARTICLE_URL = 'contents/{category}/{slug}.html'
ARTICLE_SAVE_AS = 'contents/{category}/{slug}.html'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SUBMENU = False
DISPLAY_SEARCH_FORM = False

DEFAULT_DATE_FORMAT = '%Y-%m-%d'
CATEGORY_SUBSTITUTIONS = (('C++', 'cpp'),)

GOOGLE_ANALYTICS = 'UA-80111091-2'

# Themes
THEME = 'themes/blueidea'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# GitHub
# GITHUB_URL = 'https://github.com/tepp91'

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/DevTepp', 'twitter.png'),
          ('github',  'https://github.com/tepp91',   'github.png'),
          ('blog',    'http://tepp.hatenablog.jp/',  'hatena.png'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
