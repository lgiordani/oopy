class MyType(type):
    pass

class MySpecialClass(metaclass=MyType):
    pass
