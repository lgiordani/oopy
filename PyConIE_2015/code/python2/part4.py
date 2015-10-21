## Dive into Object-oriented Python - Part 4 - Polymorphism

### Slides 129-134

a = 5
print(a)

print(type(a))
print(hex(id(a)))

a = 'five'
print(a)

print(type(a))
print(hex(id(a)))


### Slides 135-136

def echo(a):
    return a

print(echo(5))
print(echo('five'))


### Slides 137-143

print(5 + 6)
print(5.5 + 6.6)
print("just a" + " string")
print([1,2,3] + [4,5,6])
print((1,2,3) + (4,5,6))

try:
    print({'a':4, 'b':5} + {'c':7})
except TypeError as e:
    print(e)

s = "Just a sentence"
print(len(s))
l = [1, 2, 3]
print(len(l))
d = {'a': 1, 'b': 2}
print(len(d))
i = 5

try:
    print(len(i))
except TypeError as e:
    print(e)


### Slides 144-145

print(s.__len__())
print(l.__len__())
print(d.__len__())

try:
    print(i.__len__())
except AttributeError as e:
    print(e)


### Slides 146-149

print([1,2,3].__add__([4,5,6]))

dir([1,2,3])
1 in [1,2,3]
[1,2,3].__contains__(1)

6 in [1,2,3]
[1,2,3].__contains__(6)


### Slides 150-152

def sum(a, b):
    return a + b

sum(5,6)
sum("Being ", "polymorphic")
sum([1,2,3], [4,5,6])

try:
    sum([1,2,3], 8)
except TypeError as e:
    print(e)


### Slides 157-163

class Room:
    def __init__(self, door):
        self.door = door      
    def open(self):
        self.door.open()
    def close(self):
        self.door.close()
    def is_open(self):
        return self.door.is_open()  

class Door:
    def __init__(self):
        self.status = "closed"
    def open(self):
        self.status = "open"
    def close(self):
        self.status = "closed"
    def is_open(self):
        return self.status == "open"

class BooleanDoor:
    def __init__(self):
        self.status = True
    def open(self):
        self.status = True
    def close(self):
        self.status = False
    def is_open(self):
        return self.status

door = Door()
bool_door = BooleanDoor()
room = Room(door)
bool_room = Room(bool_door)

room.open()
print(room.is_open())

room.close()
print(room.is_open())

bool_room.open()
print(bool_room.is_open())

bool_room.close()
print(bool_room.is_open())
