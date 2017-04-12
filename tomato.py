#! /usr/bin/env python3

from colorize import colorize
from printer import Printer
from sound import SOUNDS
from timer import Timer

from os import chdir
from os.path import dirname
chdir(dirname(__file__))



class Tomato:
    def __init__(self, timer_generator):
        self.timer_generator = timer_generator
        self.printer = Printer()

    def start(self):
        for timer in self.timer_generator():
            timer.bind_printer(self.printer)
            timer.start()

    @classmethod
    def create_timers(cls, timers_values):
        timers = [Timer(**value) for value in timers_values]

        def generator():
            while True:
                for timer in timers:
                    yield timer
        return cls(generator)

# T_10 = Timer(10, sound=SOUNDS['short'])

# T5 = Timer(5 * 60, sound=SOUNDS['short'])
# T10 = Timer(10 * 60, sound=SOUNDS['short'])
# T20 = Timer(20 * 60, sound=SOUNDS['long'])
# T30 = Timer(30 * 60, sound=SOUNDS['long'])
# T40 = Timer(40 * 60, sound=SOUNDS['long'])


# def simple_timer_generator():
#     while True:
#         T30.name = colorize('Work', 'light-red')
#         yield T30
#         T30.name = colorize('Rest', 'light-green')
#         yield T20

# def simple_timer_generator():
#     while True:
#         T_10.name = colorize('Work', 'light-red')
#         yield T_10
#         T_10.name = colorize('Rest', 'light-green')
#         yield T_10


def main():
    # tomato = Tomato(simple_timer_generator)
    tomato = Tomato.create_timers([
        {
            'length': 30 * 60,
            'name': colorize('Work', 'light-red'),
            'sound': 'long'
        }, {
            'length': 30 * 60,
            'name': colorize('Rest', 'light-green'),
            'sound': 'long'
        }
    ])
    tomato.start()



if __name__ == '__main__':
    main()
