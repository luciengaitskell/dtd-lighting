from adafruit_led_animation.animation import Animation
from ..strip import num_strands, strand_length


class KniteRyde(Animation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chaser_count = 3
        self.chaser_length = 10
        self.chaser_term = 1.75
        self.chaser_idx: dict[int, list] = {}

    def draw_chaser(self, sid: int, cidx: int):
        for delta in range(self.chaser_length):
            idx = (cidx + delta) % strand_length
            color = [c / ((delta + 1) ** self.chaser_term) for c in self.color]
            self.pixel_object[sid * strand_length + idx] = color
            # print(color)

    def draw_strand(self, sid: int):
        if sid not in self.chaser_idx:
            self.chaser_idx[sid] = [
                0,
                int(strand_length / 3),
                int(strand_length * 2 / 3),
            ]

        for chase_idx, chase_px in enumerate(self.chaser_idx[sid]):
            self.draw_chaser(sid, chase_px)
            self.chaser_idx[sid][chase_idx] = (
                self.chaser_idx[sid][chase_idx] - 1
            ) % strand_length

    def draw(self):
        self.pixel_object.fill((0, 0, 0, 0))
        for strand in range(num_strands):
            self.draw_strand(strand)
