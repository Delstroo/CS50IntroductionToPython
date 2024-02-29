import sys
import Image

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
 
images[0].save(
    "gus.gif", save_all=True, append_image=[images[2]], duration=200, loop=0
)