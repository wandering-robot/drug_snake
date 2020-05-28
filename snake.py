class BodyNode:
    def __init__(self, cell):
        self.cell = cell

class Body:
    def __init__(self):
        self.queue = []

    def move(self, new_cell, ate=False):
        self.queue.append(new_cell)
        if not ate:
            self.queue.pop()

class Snake:
    def __init__(self):
        self.length = 1
        self.dir = [None,None]
        self.stoned = 0

    
