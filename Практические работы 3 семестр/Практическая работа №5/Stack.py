class Stack:

    #-------------------------------------------------------------------

    # Construct an empty Stack object.

    def __init__(self):
        self._a = []  # Items

    #-------------------------------------------------------------------

    # Return True if self is empty, and False otherwise.

    def isEmpty(self):
        return len(self._a) == 0

    #-------------------------------------------------------------------

    # Push object item onto the top of self.

    def push(self, item):
        self._a += [item]

    #-------------------------------------------------------------------

    # Pop the top object from self and return it.

    def pop(self):
        return self._a.pop()

    #-------------------------------------------------------------------

    # Return a string representation self.

    def __str__(self):
        s = ''
        for item in self._a:
            s = str(item) + ' ' + s
        #for item in reversed(self._a):
        #    s += str(item) + ' '
        return s
