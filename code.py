from lights.strip import pixels
from lights.animations.strobe import Strobe

hz = 10

anim = Strobe(pixels, hz, (0, 0, 0, 255))
print("Running at {}Hz".format(hz))
while True:
    anim.animate()
