#! /usr/bin/env python3

from os import system

SOUNDS = {
    'long': 'sounds/alarm.wav',
    'short': 'sounds/single_alarm.wav'
}


def play_audiofile(audiofile):
    system('play ' + str(audiofile) + ' 2>/dev/null')
