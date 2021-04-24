import sys
from stdlib_python import stddraw
import luminance
from stdlib_python.picture import Picture
from stdlib_python import color
# import math
# import os
# import pygame

# import grayscale
# import picture
# sys.path.append(os.path.join(sys.path[0], r'stdlib-python'))
# print(type(sys.path))
# print(sys.path[0])
# print(os.path.join(sys.path[0], r'stdlib-python'))

def main():
    grayColors = {}
    # print(os.path.join("","папка/flowers.jpg"))
    # print(sys.argv[1])
    pic = Picture(sys.argv[1])
    pixelCount = pic.width() * pic.height()
    for col in range(pic.width()):
        for row in range(pic.height()):
            pixel = pic.get(col, row)
            gray = luminance.toGray(pixel)
            grayColors[gray.getRed()]=grayColors.get(gray.getRed(),0)+1

    stddraw.setCanvasSize(256*4+1, 400)
    stddraw.setYscale(0,grayColors.get(max(grayColors, key=grayColors.get),0)+400)
    stddraw.setXscale(0,256*4)
    stddraw.clear(color.Color(0,220,0))
    # stddraw.setPenColor(color.RED)
    # stddraw.filledRectangle(0,0,100,100)
    # print(max(grayColors, key=grayColors.get))
    # print(sum(grayColors.values()))
    # print(grayColors.get(max(grayColors, key=grayColors.get),0))
    # print(5265/430400*100)
    # print(round(5265 / 430400 * 100))
    for i in range(256):
        count = grayColors.get(i,0)
        stddraw.setPenColor(color.Color(i,i,i))
        stddraw.filledRectangle(i*4+1.0,0,4.0,count)

    stddraw.show()


if __name__ == "__main__":
    # sys.path.append(os.path.join(sys.path[0], r'stdlib-python'))
    # print(sys.path)
    # os.environ['PATH'] += ','+r"C:\Users\Наталия\Desktop\Практическая работа №1\stdlib-python"
    main()
