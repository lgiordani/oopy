class MyType(type):
    pass

class MySpecialClass(object):
	__metaclass__ = MyType
