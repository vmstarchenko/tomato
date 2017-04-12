import time

from sound import play_audiofile, SOUNDS

class Timer:
    def __init__(self, length, name='Timer', step=1, printer=None, sound=None):
        self.length = length if length > 0 else 0
        self.name = str(name)
        self.step = step if step > 0 else 1
        self.printer = printer
        self.sound = SOUNDS['short'] if sound is None else SOUNDS[sound]

    def start(self):
        if self.printer is None:
            raise ValueError('cant start timer if printer is none')

        start_time = time.time()
        end_time = start_time + self.length

        st_start_time = time.localtime(start_time)
        st_end_time = time.localtime(end_time)
        st_time = time.localtime(end_time - start_time)

        print('Start timer: <%s>' % self.name,
              time.strftime('timer length:\t%02d:%02d:%02d' % (
                  st_time.tm_hour - 3,
                  st_time.tm_min,
                  st_time.tm_sec)),
              time.strftime('start time:\t%x\t%X', st_start_time),
              time.strftime('end time:\t%x\t%X', st_end_time),
              sep='\n  ')

        now = start_time

        while now < end_time:
            st_now_time = time.localtime(now)
            st_end_time = time.localtime(end_time - now)

            self.printer(
                time.strftime('%x %X #', st_now_time),
                '%02d:%02d:%02d' % (
                    st_end_time.tm_hour - 3,
                    st_end_time.tm_min,
                    st_end_time.tm_sec),
                clean=True)

            time.sleep(self.step)
            now = time.time()

        self.printer.clean()
        print('Stop timer.\n')
        self.play_sound()

    def bind_printer(self, printer):
        self.printer = printer

    def play_sound(self):
        play_audiofile(self.sound)
