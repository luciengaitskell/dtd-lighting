from lights.strip import pixels
from lights.animations.ryde import KniteRyde


anim = KniteRyde(pixels, 0.05, (0, 0, 0, 0.4))

while True:
    anim.animate()
