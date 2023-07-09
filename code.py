from lights.strip import pixels
from lights.animations.bounce import Bounce


anim = Bounce(pixels, 0.01, (200, 0, 0, 0))

while True:
    anim.animate()
