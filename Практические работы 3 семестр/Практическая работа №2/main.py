from stdlib_python import stddraw
from Rectangle import Rectangle



def drawRectangles(x0, y0, cellSize, width, height):
    # rects = [[], []]
    # for row in range(2):
    stddraw.setPenColor(stddraw.BLUE)
    rects = []
    for i in range(5):
        rx0 = x0 + i * cellSize + (cellSize - width) // 2
        ry0 = y0 + (cellSize - height) // 2
        # rects[row].append(Rectangle(rx0, ry0, rx0 + width, ry0 + height))
        # rects[row][i].draw()
        rects.append(Rectangle(rx0, ry0, rx0 + width, ry0 + height))
        rects[i].draw()
        # stddraw.setPenColor(stddraw.BLUE)
        # stddraw.show()
    return rects


def drawAnotherRects(x0, y0, cellSize, width, height):
    stddraw.setPenColor(stddraw.RED)
    rects = []
    # center
    rx0 = x0 + (cellSize - width) // 2
    ry0 = y0 + (cellSize - height) // 2
    rects.append(Rectangle(rx0, ry0, rx0 + width, ry0 + height))
    rects[-1].draw()

    # right top
    rx0 = x0 + cellSize + (cellSize - width)
    ry0 = y0 + (cellSize - height)
    rects.append(Rectangle(rx0, ry0, rx0 + width, ry0 + height))
    rects[-1].draw()

    # right bottom
    rx0 = x0 + 2 * cellSize + (cellSize - width)
    ry0 = y0
    rects.append(Rectangle(rx0, ry0, rx0 + width, ry0 + height))
    rects[-1].draw()
    # left top
    rx0 = x0 + 3 * cellSize
    ry0 = y0 + (cellSize - height)
    rects.append(Rectangle(rx0, ry0, rx0 + width, ry0 + height))
    rects[-1].draw()

    # left bottom
    rx0 = x0 + 4 * cellSize
    ry0 = y0
    rects.append(Rectangle(rx0, ry0, rx0 + width, ry0 + height))
    rects[-1].draw()

    return rects


# rects[1][-1].draw()
def writeStats(rects, another):
    print("Площади синих: " + " ".join(map(lambda x: str(x.area()), rects)))
    print("Площади красных: " + " ".join(map(lambda x: str(x.area()), another)))
    print("Периметры синих: " + " ".join(map(lambda x: str(x.perimeter()), rects)))
    print("Периметры красных: " + " ".join(map(lambda x: str(x.perimeter()), another)))
    print("Синий пересекает красный: "+" ".join(map(lambda x, y: str(x.intersects(y)), rects,another)))
    print("Синий содержит красный: "+" ".join(map(lambda x, y: str(x.contains(y)), rects,another)))


def writeAllStats(rects, another):
    text1 = {0:"Правый верхний угол",1:"Правый нижний угол", 2:"Левый нижний угол",3:"Левый верхний угол"}
    text2 = {0: "Нижняя строка", 1: "Верхняя строка"}
    for i in range(len(rects)):
        print(text1[i])
        for j in range(2):
            print(text2[j])
            writeStats(rects[i][j], another[i][j])
            print()
        print()
        print()


def draw():
    stddraw.setCanvasSize(1000, 400)
    stddraw.setXscale(-500, 500)
    stddraw.setYscale(-200, 200)
    stddraw.clear(stddraw.CYAN)
    stddraw.setPenColor(stddraw.ORANGE)
    stddraw.filledRectangle(0, 0, 500, 200)
    stddraw.filledRectangle(-500, -200, 500, 200)

    rt = []
    rt.append(drawRectangles(0, 0, 100, 35, 25))
    rt.append(drawRectangles(0, 100, 100, 70, 50))

    rb = []
    rb.append(drawRectangles(0, -200, 100, 35, 25))
    rb.append(drawRectangles(0, -100, 100, 70, 50))

    lb = []
    lb.append(drawRectangles(-500, -200, 100, 35, 25))
    lb.append(drawRectangles(-500, -100, 100, 70, 50))


    lt = []
    lt.append(drawRectangles(-500, 0, 100, 35, 25))
    lt.append(drawRectangles(-500, 100, 100, 70, 50))
    # stddraw.setPenColor(stddraw.RED)

    rects = [rt, rb, lb, lt]

    rt = []
    rt.append(drawAnotherRects(0, 0, 100, 40, 25))
    rt.append(drawAnotherRects(0, 100, 100, 80, 60))

    rb = []
    rb.append(drawAnotherRects(0, -200, 100, 35, 30))
    rb.append(drawAnotherRects(0, -100, 100, 35, 40))

    lb = []
    lb.append(drawAnotherRects(-500, -200, 100, 35, 25))
    lb.append(drawAnotherRects(-500, -100, 100, 35, 35))


    lt = []
    lt.append(drawAnotherRects(-500, 0, 100, 25, 20))
    lt.append(drawAnotherRects(-500, 100, 100, 70, 50))

    another =[rt, rb, lb, lt]
    # writeStats(rects[0][0],another[0][0])
    writeAllStats(rects, another)
    stddraw.show()


def main():
    # stddraw.setCanvasSize(800, 600)
    # stddraw.setYscale(-299,300)
    # stddraw.setXscale(-399, 400)
    # rect1 = Rectangle(10, 10, 200, 200)
    # rect2 = Rectangle(10, -10, 200, -200)
    # rect3 = Rectangle(-10, -10, -200, -200)
    # rect4 = Rectangle(-10, 10, -200, 200)
    # stddraw.clear(stddraw.CYAN)
    # # stddraw.setPenRadius(0.01)
    # stddraw.setPenColor(stddraw.GREEN)
    # rect1.draw()
    # # stddraw.setPenRadius(0.02)
    # stddraw.setPenColor(stddraw.ORANGE)
    # rect2.draw()
    # stddraw.setPenColor(stddraw.BLUE)
    # rect3.draw()
    # stddraw.setPenColor(stddraw.RED)
    # rect4.draw()
    # stddraw.show()
    draw()


if __name__ == "__main__":
    main()
