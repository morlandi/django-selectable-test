import pprint
from django.conf import settings

try:
    import sqlparse
except ImportError:
    class sqlparse:
        @staticmethod
        def format(text, *args, **kwargs):
            return text


def trace(message, prettify=False):

    if type(message) is list:
        text = '\n'.join([str(item) for item in message])
    else:
        text = str(message)

    if prettify:
        text = pprint.pformat(text)

    if settings.DEBUG:
        print '\x1b[1;33;40m' + text + '\x1b[0m'


def prettyprint_queryset(qs, colorize=True):
    if settings.DEBUG:
        if colorize: print '\x1b[1;33;40m'
        print sqlparse.format(str(qs.query), reindent=True, keyword_case='upper')
        if colorize: print '\x1b[0m'

