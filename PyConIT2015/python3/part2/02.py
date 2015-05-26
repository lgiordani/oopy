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
