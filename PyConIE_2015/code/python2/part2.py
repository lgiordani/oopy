## Dive into Object-oriented Python - Part 2 - Classes and members

### Slides 43-44

class Door(object):
    def __init__(self, number, status):
        self.number = number
        self.status = status
    def open(self):
        self.status = 'open'
    def close(self):
        self.status = 'closed'

door1 = Door(1, 'closed')
door2 = Door(1, 'closed')

hex(id(door1))
hex(id(door2))

hex(id(door1.__class__))
hex(id(door2.__class__))


### Slide 41

class Door:
    colour = 'brown'
    def __init__(self, number, status):
        self.number = number
        self.status = status
    def open(self):
        self.status = 'open'
    def close(self):
        self.status = 'closed'

### Slides 47-51

door1 = Door(1, 'closed')
door2 = Door(2, 'closed')

Door.colour
door1.colour
door2.colour

Door.colour = 'white'

Door.colour
door1.colour
door2.colour

hex(id(Door.colour))
hex(id(door1.colour))
hex(id(door2.colour))


### Slides 52-55

door1 = Door(1, 'closed')
door2 = Door(2, 'closed')
print(type(Door.__dict__))
Door.__dict__

print(type(door1.__dict__))
door1.__dict__

try:
    door1.__dict__['colour']
except KeyError as e:
    print("Cannot find key {}".format(e))

door1.__class__.__dict__['colour']

door1.colour is Door.colour


### Slides 57-60

door1 = Door(1, 'closed')
door1.colour = 'white'

door1.__dict__['colour']
door1.__class__.__dict__['colour']

door1.colour
Door.colour

Door.colour = 'red'
door1.__dict__['colour']
door1.__class__.__dict__['colour']


### Slides 65-68

door1 = Door(1, 'closed')
Door.__dict__
door1.__dict__

door1.colour is Door.colour
door1.open is Door.open

print(Door.__dict__['open'])
print(Door.open)
door1.open


### Slides 70-76

try:
    Door.open()
except TypeError as e:
    print(e)

Door.open(door1)
door1.status

print(door1.__class__.__dict__['open'])
dir(door1.__class__.__dict__['open'])

door1.__class__.__dict__['open'].__get__
door1.__class__.__dict__['open'].__get__(door1)
door1.__class__.__dict__['open'].__get__(door1, Door)


### Slides 78-79

class Door:
    colour = 'brown'
    def __init__(self, number, status):
        self.number = number
        self.status = status
    @classmethod
    def knock(cls):
        print("Knock!")
    def open(self):
        self.status = 'open'
    def close(self):
        self.status = 'closed'

door1 = Door(1, 'closed')
door1.knock()

Door.knock()
