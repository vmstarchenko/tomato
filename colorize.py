#! /usr/bin/env python3


COLORS = {
    'black':        '\033[0;30m',
    'dark-gray':    '\033[1;30m',
    'red':          '\033[0;31m',
    'light-red':    '\033[1;31m',
    'green':        '\033[0;32m',
    'light-green':  '\033[1;32m',
    'brown':        '\033[0;33m',
    'yellow':       '\033[1;33m',
    'blue':         '\033[0;34m',
    'light-blue':   '\033[1;34m',
    'purple':       '\033[0;35m',
    'light-purple': '\033[1;35m',
    'cyan':         '\033[0;36m',
    'light-cyan':   '\033[1;36m',
    'light-gray':   '\033[0;37m',
    'white':        '\033[1;37m',
}
NC_COLOR = '\033[0m'


def colorize(string, color):
    color = COLORS.get(color, None)
    if color is None:
        return string
    return color + string + NC_COLOR
