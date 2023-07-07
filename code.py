import time
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

# RGBW
colors = [(0x00, 0x00, 0x00, 0xFF), (0x00, 0x00, 0x00, 0x00)]
hz = 10

print("Running at {}Hz".format(hz))
while True:
    for c in colors:
        pixels.fill(c)
        pixels.show()
        time.sleep(1 / (len(colors) * hz))
