import random
import time

from adafruit_led_animation.animation import Animation

from ..strip import num_strands, strand_length


class Bounce(Animation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.e_start = None
        self.e_len = None
        self.e_amp = None

    def calc_amp_height(self):
        delta = time.monotonic() - self.e_start
        dist = abs(delta - self.e_len / 2) * 2 / self.e_len  # 0 to 1
        return self.e_amp * (1 - dist**1.5) * strand_length

    def draw_strip(self, sid: int):
        h = self.calc_amp_height()
        print(h)
        for px in range(h):
            self.pixel_object[strand_length * sid + px] = self.color

    def draw(self):
        self.pixel_object.fill((0, 0, 0, 0))
        if self.e_start is None or time.monotonic() - self.e_start > self.e_len:
            self.e_start = time.monotonic()
            self.e_len = random.uniform(0.2, 0.8)
            self.e_amp = random.uniform(0.1, 1)
        for s in range(num_strands):
            self.draw_strip(s)
