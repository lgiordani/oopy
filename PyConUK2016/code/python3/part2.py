## Dive into Object-oriented Python - Part 2 - Class and instance

### Slides 39-41

class Door:
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


### Slide 42

class Door:
    colour = 'brown'
    def __init__(self, number, status):
        self.number = number
        self.status = status
    def open(self):
        self.status = 'open'
    def close(self):
        self.status = 'closed'

### Slides 43-47

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


### Slides 48-51

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


### Slides 53-56

door1 = Door(1, 'closed')
door1.colour = 'white'

door1.__dict__['colour']
door1.__class__.__dict__['colour']

door1.colour
Door.colour

Door.colour = 'red'
door1.__dict__['colour']
door1.__class__.__dict__['colour']


### Slides 61-63

door1 = Door(1, 'closed')
Door.__dict__
door1.__dict__

door1.colour is Door.colour
door1.open is Door.open

print(Door.__dict__['open'])
print(Door.open)
door1.open


### Slides 65-67

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


### Slides 68-72

class Door:
    colour = 'brown'
    def __init__(self, number, status):
        self.number = number
        self.status = status
    @classmethod
    def knock(cls):
        print("Knock!")
    @classmethod
    def paint(cls, colour):
        cls.colour = colour
    def open(self):
        self.status = 'open'
    def close(self):
        self.status = 'closed'

door1 = Door(1, 'closed')
door2 = Door(2, 'closed')

Door.colour
door1.colour
door2.colour

Door.paint('white')
Door.colour
door1.colour
door2.colour

door1.paint('yellow')
Door.colour
door1.colour
door2.colour
