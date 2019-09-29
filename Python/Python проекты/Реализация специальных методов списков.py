class TypedList:
    def __init__(self, example_element, initial_list=[]):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must be a list")
        for element in initial_list:
            self.__check(element)
        self.elements = initial_list[:]

    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Attempted to add an element of incorrect type to a typed list")

    def __setitem__(self, i, element):
        self.__check(element)
        self.elements[i] = element

    def __getitem__(self, i):
        return self.elements[i]

    def __len__(self):
        return len(self.elements)

    def __delitem__(self, i):
        del self.elements[i]

    def append(self, item):
        self.__check(item)
        self.elements.append(item)


def main():
    x = TypedList("", 5 * [""])
    x[2] = "Hello"
    x[3] = "There"
    print(x[2], x[3])
    print(x[2:4])
    a, b, c, d, e = x
    print([a, b, c, d])
    print(len(x))
    del x[0]
    print(len(x), x.elements)
    # x.append(7)
    x.append("7")
    print(len(x), x.elements)


if __name__ == "__main__":
    main()
