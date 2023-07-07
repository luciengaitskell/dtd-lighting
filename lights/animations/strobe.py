from adafruit_led_animation.animation import Animation


class Strobe(Animation):
    @staticmethod
    def _calc_frametime(hz):
        return 1 / (2 * hz)

    def __init__(self, pixel_object, hz, color, peers=None, paused=False, name=None):
        speed = self._calc_frametime(hz)
        super().__init__(pixel_object, speed, color, peers, paused, name)
        self._c_on = False

    def set_hz(self, hz):
        self.speed = self._calc_frametime(hz)

    def draw(self):
        self._c_on = not self._c_on
        self.pixel_object.fill(self.color if self._c_on else (0, 0, 0, 0))
