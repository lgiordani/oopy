## Object-oriented Python from scratch - Part 1 - Objects and types

### Slide 8

data = (13, 63, 5, 378, 58, 40)

def avg(d):
    return sum(d)/len(d)

avg(data)


### Slide 9

door1 = [1, 'closed']
door2 = [2, 'closed']

def open_door(door):
    door[1] = 'open'

open_door(door1)
door1


### Slides 10-11

door1 = [1, 'closed']
door2 = [2, 'closed']

ldoor1 = [1, 'closed', 'unlocked']

def open_door(door):
    door[1] = 'open'

def open_ldoor(door):
    if door[2] == 'unlocked':
        door[1] = 'open'

open_door(door1)
door1

open_ldoor(ldoor1)
ldoor1


### Slide 20

a = 6
a

print(type(a))

a = int(6)
a

print(a.__class__)


### Slide 26

class Door(object):
    def __init__(self, number, status):
        self.number = number
        self.status = status
    def open(self):
        self.status = 'open'
    def close(self):
        self.status = 'closed'


### Slides 29-33

door1 = Door(1, 'closed')
print(type(door1))

door1.number

door1.status

door1.open()
door1.number

door1.status
