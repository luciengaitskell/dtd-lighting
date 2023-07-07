import board
from adafruit_neopxl8 import NeoPxl8


# Customize for your strands here
num_strands = 8
strand_length = 84
first_led_pin = board.NEOPIXEL0

num_pixels = num_strands * strand_length

pixels = NeoPxl8(
    first_led_pin,
    num_pixels,
    num_strands=num_strands,
    auto_write=False,
    brightness= 1, # 0.50,
    bpp=4,
)
