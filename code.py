import time
from lights.strip import pixels

# RGBW
colors = [(0x00, 0x00, 0x00, 0xFF), (0x00, 0x00, 0x00, 0x00)]
hz = 10

print("Running at {}Hz".format(hz))
while True:
    for c in colors:
        pixels.fill(c)
        pixels.show()
        time.sleep(1 / (len(colors) * hz))
