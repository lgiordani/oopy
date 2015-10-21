## Dive into Object-oriented Python - Part 3 - Delegation

### Slides 92-94

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

class SecurityDoor(Door):
    pass

sdoor = SecurityDoor(1, 'closed')

SecurityDoor.colour is Door.colour

sdoor.colour is Door.colour


### Slides 96-99

sdoor.__dict__
sdoor.__class__.__dict__
Door.__dict__

print(SecurityDoor.__bases__)

sdoor.knock
sdoor.__class__.__bases__[0].__dict__['knock'].__get__(sdoor)


### Slides 100-101

class SecurityDoor(Door):
    colour = 'grey'
    locked = True
    def open(self):
        if not self.locked:
            self.status = 'open'

SecurityDoor.__dict__


### Slides 106-109

class SecurityDoor(Door):
    colour = 'grey'
    locked = True
    def open(self):
        if self.locked:
            return
        Door.open(self)

sdoor = SecurityDoor(1, 'closed')
sdoor.status

sdoor.open()
sdoor.status

sdoor.locked = False
sdoor.open()
sdoor.status


### Slide 110

class SecurityDoor(Door):
    colour = 'grey'
    def __init__(self, number, status, locked=True):
        super().__init__(number, status)
        self.locked = locked
    def open(self):
        if self.locked:
            return
        super().open()

sdoor = SecurityDoor(1, 'closed')
sdoor.status

sdoor.open()
sdoor.status

sdoor.locked = False
sdoor.open()
sdoor.status


### Slide 112-113

class SecurityDoor:
    colour = 'grey'
    def __init__(self, number, status, locked=True):
        self.door = Door(number, status)
        self.locked = locked
    def open(self):
        if self.locked:
            return
        self.door.open()
    def close(self):
        self.door.close()

s = SecurityDoor(1, 'closed')
try:
    s.status
except AttributeError as e:
    print(e)


### Slide 114

class SecurityDoor:
    colour = 'grey'
    def __init__(self, number, status, locked=True):
        self.door = Door(number, status)
        self.locked = locked
    def open(self):
        if self.locked:
            return
        self.door.open()
    def close(self):
        self.door.close()
    def get_status(self):
        return self.door.status
    status = property(get_status)

s = SecurityDoor(1, 'closed')
s.status


### Slide 115

class SecurityDoor:
    colour = 'grey'
    def __init__(self, number, status, locked=True):
        self.door = Door(number, status)
        self.locked = locked
    def open(self):
        if self.locked:
            return
        self.door.open()
    def close(self):
        self.door.close()
    def __getattr__(self, attr):
        return getattr(self.door, attr)

s = SecurityDoor(1, 'closed')
s.status


### Slide 116

class SecurityDoor:
    colour = 'grey'
    def __init__(self, number, status, locked=True):
        self.door = Door(number, status)
        self.locked = locked
    def open(self):
        if self.locked:
            return
        self.door.open()
    def __getattr__(self, attr):
        return getattr(self.door, attr)

s = SecurityDoor(1, 'closed')
s.status


### Slide 117

class ComposedDoor:
    def __init__(self, number, status):
        self.door = Door(number, status)
    def __getattr__(self, attr):
        return getattr(self.door, attr)


### Slides 123-127

l = [1,2,3]
dir(l)

print(l.append)

a = l.append
print(a)

b = getattr(l, 'append')
print(b)

print(a == b)

print(a is b)
