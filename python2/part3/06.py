class Door(object):
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

class SecurityDoor(object):
    colour = 'grey'
    locked = True
    def __init__(self, number, status):
        self.door = Door(number, status)
    def open(self):
        if self.locked:
            return
        self.door.open()
    def close(self):
        self.door.close()
    def __getattr__(self, attr):
        return getattr(self.door, attr)
