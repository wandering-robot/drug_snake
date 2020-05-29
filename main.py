import pygame as py
from random import choice
from time import time

from world import Space
from snake import Snake

class MainDisplay:
    start = time()
    def __init__(self):
        self.size = (760,760)

        self.display_window = py.display.set_mode((self.size))
        self.background = py.Surface(self.display_window.get_size()).convert()
        self.background.fill((0,100,0))
        self.myfont = py.font.SysFont('monospace',16)

        self.space = Space(self.size)
        self.snake = Snake(self.space)

        self.options = self.get_inside_options()
        self.snake.start(self.get_random_cell())

        self.food_cell = self.get_random_cell()
        self.food_cell.occupied = True

        self.fps = 15                #set frame rate, may change later
        self.clock = py.time.Clock()
        self.delay = False      #trying to keep snake from running into itself

        self.running = True

    def get_random_cell(self):              #used to get a randoim cell from the space that isn't being used right now by body
        cell = choice(self.options)
        if cell in self.snake.body_queue:
            cell = choice(choice(self.space.matrix))
        return cell

    def get_inside_options(self):           #mostly so that gameplay sticks around the middle
        options =[]
        for i in range(int(len(self.space.matrix)/10),int(len(self.space.matrix)*9/10)):
            for j in range(int(len(self.space.matrix[0])/10),int(len(self.space.matrix[0])*9/10)):
                options.append(self.space.matrix[i][j])
        return options

    def run(self):
        while self.running:
            self.delay = False
            self.clock.tick(self.fps)
            self.update_objects()           #redraw
            for event in py.event.get():    
                self.handle_event(event)  
            if time() - self.start > 2:     #give player time to get ready
                self.snake.move()
            if not self.snake.alive:
                break 

    def update_objects(self):
        self.display_window.blit(self.background,(0,0))
        for cell in self.snake.body_queue:
            cell.colour_it()
            self.display_window.blit(cell.image,cell.pos)
        self.display_window.blit(self.food_cell.image,self.food_cell.pos)
        if self.food_cell in self.snake.body_queue:
            self.food_cell = self.get_random_cell()
            self.food_cell.occupied = True
        mirage = []
        for _ in range(self.snake.stoned):
            mirage.append(self.get_random_cell())
        for cell in mirage:
            self.display_window.blit(cell.image,cell.pos)
        scoretext = self.myfont.render(f'Score: {len(self.snake.body_queue)}',1,(255,0,0))
        self.display_window.blit(scoretext,(10,10))
        py.display.flip()

    def handle_event(self,event):
            if event.type == py.QUIT:
                self.running = False
                py.quit()
            elif event.type == py.KEYDOWN:
                if not self.delay:
                    if event.key == py.K_w:
                        if self.snake.dir != [0,1]:
                            self.snake.dir = [0,-1]
                            self.delay = True
                    elif event.key == py.K_s:
                        if self.snake.dir != [0,-1]:
                            self.snake.dir = [0,1]
                            self.delay = True
                    elif event.key == py.K_d:
                        if self.snake.dir != [-1,0]:
                            self.snake.dir = [1,0]
                            self.delay = True
                    elif event.key == py.K_a:
                        if self.snake.dir != [1,0]:
                            self.snake.dir = [-1,0]
                            self.delay = True
if __name__ == '__main__':
    py.init()
    game = MainDisplay()
    game.run()
