class Table:
    def __init__(self):
        pass
    



class Row:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

r = Row()


#c.x = 10
#print(c.x)
#del c.x