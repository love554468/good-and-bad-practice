# Python allows dèining getter and setter methods similarly
# as C++ and Java

class C:
    def get_x(self):
        return self.__x 
    def set_x(self, value):
        self.__x=value

c = C()
c.set_x(3)
c.get_x()

class B():
    @property
    def x(self):
        return self.__x 
    @x.setter
    def x(self, value):
        self.__x = value

b = B()
b.x = 2
b.x #get ra
