#! /usr/bin/env python3

import sys

class Printer:
    def __init__(self, show_warnings=False):
        self.show_warnings = show_warnings
        self.printed_number = 0

    def __call__(self, *args, sep=' ', end='', clean=False):
        string = sep.join(str(_) for _ in args) + end
        string_len = len(string)
        if self.show_warnings and '\n' in string:
            print('Warning: print newline', file=sys.stderr)

        if clean:
            string = '\b' * self.printed_number + string
            self.printed_number = 0
            self.printed_number += string_len

        print(string, end=end, flush=True)

    def __del__(self):
        self.clean()

    def clean(self):
        print('\b' * self.printed_number, end='', flush=True)
        self.printed_number = 0
        return self

