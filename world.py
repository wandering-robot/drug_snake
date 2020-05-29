import pygame as py
from random import randint

class Cell:
    def __init__(self,x,y,world):
        self.x = x
        self.y = y
        self.world = world
        self.side_length = self.world.cell_side_length
        self.occupied = False
        self.image = py.Surface((self.side_length,self.side_length)).convert()

        self.colour = self.random_colour()
        self.image.fill(self.colour)

        self.pos = self.calculate_pos()

    def colour_it(self):
        if self.occupied:
            self.image.fill((0,0,0))
        else:
            self.image.fill(self.colour)

    def __repr__(self):
        return repr(f'(x:{self.x} y:{self.y})')

    def __str__(self):
        return f'(x:{self.x} y:{self.y})'

    def calculate_pos(self):
        return (self.x*self.side_length, self.y*self.side_length)

    @staticmethod
    def random_colour():
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        return (r,g,b)

class Space:
    def __init__(self,screen_size):
        self.screen_size = screen_size
        self.cell_side_length = 20
        self.size = (int(self.screen_size[0]/self.cell_side_length), int(self.screen_size[1]/self.cell_side_length))
        self.matrix = self.create_world()

    def create_world(self):
        return [[ Cell(x,y,self) for y in range(self.size[1])] for x in range(self.size[0])]

    def show(self):
        for row in self.matrix:
            row_str = '-'.join(str(cell) for cell in row)
            print(row_str)
