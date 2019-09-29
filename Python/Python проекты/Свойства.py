class Rectangle:
    def __init__(self, width=1, height=1):
        if width < 0:
            self.__width = 0
        else:
            self.__width = width
        if height < 0:
            self.__height = 0
        else:
            self.__height = height

    @property
    def _width(self):
        return self.__width

    @_width.setter
    def _width(self, new_width):
        if not new_width < 0:
            self.__width = new_width

    def publicsetwidth(self, new_width):
        if not new_width < 0:
            self.__width = new_width

    def publicgetwidth(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if not new_height < 0:
            self.__height = new_height


def main():
    rect = Rectangle(7)

    # print(rect.width)
    print(rect.publicgetwidth())
    print(rect.height)

    rect.width = 9
    rect.publicsetwidth(17)
    rect.height = 11

    print(rect.width)
    print(rect.publicgetwidth())
    print(rect.height)


if __name__ == "__main__":
    main()
