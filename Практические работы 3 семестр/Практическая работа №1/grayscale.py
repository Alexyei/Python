#-----------------------------------------------------------------------
# grayscale.py
#-----------------------------------------------------------------------

import sys
import stddraw
import luminance
from picture import Picture
import os
#-----------------------------------------------------------------------

# Accept the name of a JPG or PNG file as a command-line argument.
# Read an image from the file with that name. Create and show a
# gray scale version of that image.
# print(type(sys.argv[1]))
# print(os.getcwd())
# print(os.path.join("","flowers.jpg"))
pic = Picture(r"flowers.jpg")

for col in range(pic.width()):
    for row in range(pic.height()):
        pixel = pic.get(col, row)
        gray = luminance.toGray(pixel)
        pic.set(col, row, gray)

stddraw.setCanvasSize(pic.width(), pic.height())
stddraw.picture(pic)
pic.save("grayscaleFlowers.jpg")
stddraw.show()

print(2)

#-----------------------------------------------------------------------

# python grayscale.py mandrill.jpg

# python grayscale mandrill.png

# python grayscale.py darwin.jpg

# python grayscale.py darwin.png

