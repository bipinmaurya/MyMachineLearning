class Base:
    def __init__(self):
        self.a = "Bipin Maurya"
        self.__c = "Bipin Maurya"
class Derived(Base):
    def __init__(self):
        #calling base constructor
        Base.__init__(self)
        print("Calling private member of the base class")
        print(self.__c)

obj = Base()
print(obj.a)

obj1 = Derived()
print(obj1.__c)