# -*- encoding: utf-8 -*-
# This is your configuration file.  Please write valid python!
# See http://posativ.org/acrylamid/conf.py.html

# -*- encoding: utf-8 -*-
# This is your config file.  Please write in a valid python syntax!
# See http://acrylamid.readthedocs.org/en/latest/conf.py.html

SITENAME = 'Numbers @ Coding in the trenches'
WWW_ROOT = 'http://numbers.codinginthetrenches.com/'

AUTHOR = 'Michael Hughes'
EMAIL = 'michael@mihughes.com'

TYPOGRAPHY_MODE = "2"

FILTERS = ['rst+pygments(css_class=highlight)', 'hyphenate', 'h1','typo']
VIEWS = {
        '/': {'filters': 'summarize', 'view': 'index', 'pagination': '/page/:num/'},
        '/:year/:slug/': {'view': 'entry'},
        '/tag/:name/': {'filters': 'summarize', 'view':'tag', 'pagination': '/tag/:name/:num/'},
        '/atom/': {'filters': ['h2', 'nohyphenate'], 'view': 'atom'},
        '/rss/': {'filters': ['h2', 'nohyphenate'], 'view': 'rss'},
        '/articles/': {'view': 'articles'},
        '/:slug/':{'view':'page'}, # static pages
        '/sitemap.xml': {'view': 'sitemap'},
    # # Here are some more examples

    # # '/:slug/' is a slugified url of your static page's title
    # '/:slug/': {'view': 'page'},

    # # '/atom/full/' will give you a _complete_ feed of all your entries
    # '/atom/full/': {'filters': 'h2', 'view': 'atom', 'num_entries': 1000},

    # # a feed containing all entries tagges with 'python'
    # '/rss/python/': {'filters': 'h2', 'view': 'rss',
    #                  'if': lambda e: 'python' in e.tags},

    # # a full typography features entry including MathML and Footnotes
    # '/:year/:slug': {'filters': ['typography', 'Markdown+Footnotes+MathML'],
    #                  'view': 'entry'},

    # # translations!
    # '/:year/:slug/:lang/': {'view': 'translation'},
}

THEME = 'shadowplay'
ENGINE = 'acrylamid.templates.jinja2.Environment'
DATE_FORMAT = '%d.%m.%Y'
BLOGROLL = [ ('Home', 'http://codinginthetrenches.com/') ]

DEPLOYMENT = { "copy_local":"rsync -av --delete $OUTPUT_DIR /srv/http/numbers.codinginthetrenches.com/" }
