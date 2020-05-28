class Cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.occupied = False

    def __str__(self):
        return f'(x:{self.x} y:{self.y})'

class Space:
    def __init__(self,size):
        self.size = size
        self.matrix = self.create_world()

    def create_world(self):
        return [[ Cell(x,y) for x in range(self.size)] for y in range(self.size)]

    def show(self):
        for row in self.matrix:
            row_str = '-'.join(str(cell) for cell in row)
            print(row_str)

if __name__ == '__main__':
    space = Space(3)
    space.show()
