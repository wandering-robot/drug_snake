class Snake:
    def __init__(self,space):
        self.space = space
        
        self.alive = True
        self.dir = [1,0]
        self.stoned = 0

        self.body_queue = []

    def move(self):
        new_cell = self.check_next_cell()
        if new_cell == None:
            self.alive = False
        elif new_cell in self.body_queue:
            self.alive = False
        elif new_cell.occupied:
            self.eat(new_cell)
            self.stoned += 25*int(1+len(self.body_queue)//5)
        else:
            self._move(new_cell)
            if self.stoned > 1:
                self.stoned -= 1

    def eat(self,cell):
        self.body_queue.append(cell) 

    def check_next_cell(self):
        head = self.body_queue[-1]
        new_cell_x, new_cell_y = head.x+self.dir[0], head.y+self.dir[1]
        if new_cell_x < len(self.space.matrix) and new_cell_x >=0:
            if new_cell_y < len(self.space.matrix[0]) and new_cell_y >= 0:
                return (self.space.matrix[new_cell_x][new_cell_y])

    def _move(self, new_cell):
        self.body_queue.append(new_cell)
        new_cell.occupied = True
        old_cell = self.body_queue.pop(0)
        old_cell.occupied = False
        old_cell.colour_it() 

    def start(self,cell):
        self.body_queue.append(cell)
        cell.occupied = True
        if cell.x > self.space.size[0]*3/5:
            self.dir = [-1,0]
