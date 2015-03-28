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
