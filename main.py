
import pygame as py
from random import choice
from time import time

from world import Space
from snake import Snake
from saver import Saver

class MainDisplay:
    start = time()
    def __init__(self):
        self.size = (550,int(550*1.12))

        self.display_window = py.display.set_mode((self.size))
        self.background = py.Surface(self.display_window.get_size()).convert()
        self.background.fill((0,100,0))
        self.myfont = py.font.SysFont('monospace',16)

        self.space = Space(self.size)
        self.snake = Snake(self.space)
        self.saver = Saver()

        self.options = self.get_inside_options()
        self.snake.start(self.get_random_cell())

        self.food_cell = self.get_random_cell()
        self.food_cell.occupied = True

        self.fps_start = 15                #set frame rate, may change later
        self.fps = self.fps_start
        self.clock = py.time.Clock()
        self.delay = False      #trying to keep snake from running into itself

        self.mirage = []
        self._time = 0

        self.running = True
        self.paused = False

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
            if not self.paused:
                if time() - self.start > 2:     #give player time to get ready
                    self.snake.move()
            if not self.snake.alive:
                break
            self.fps = self.fps_start + int((time() - self.start)/7)    #gradually speeding up the snake
        self.end_game()

    def end_game(self):         #what happens in the end game
        score = len(self.snake.body_queue)-1
        ind = self.saver.check_if_highscore(score)
        if ind != None:
            self.create_input_scene()
        self.saver.end_game(score)
        self.create_final_scene()
        finished = False
        while not finished:
            for event in py.event.get(): 
                if event.type == py.QUIT:
                    finished = True
                    py.quit()
    
    def create_input_scene(self):
        self.background.fill((255,255,255))
        self.display_window.blit(self.background,(0,0))
        title = self.myfont.render(f'CONGRATUALATIONS!!! Input your score',1,(255,0,0))
        self.display_window.blit(title,(self.size[0]/2-200,self.size[1]/2-20))
        py.display.flip()

    def create_final_scene(self):
        self.background.fill((255,255,255))
        self.display_window.blit(self.background,(0,0))
        tote_high = self.size[1]
        tab = tote_high/8
        spacing = tote_high/15
        i = 0
        title = self.myfont.render(f'*** HIGHSCORES ***',1,(255,0,0))
        self.display_window.blit(title,(self.size[0]/2-100,tab/2))
        for data_line in self.saver.data:
            name,score = data_line
            score_line = self.myfont.render(f'{name}...{score}',1,(255,0,0))
            self.display_window.blit(score_line,(self.size[0]/2-40,tab+spacing*i))
            i += 1
        py.display.flip()

    def new_mirage(self):
        self.mirage = []
        for _ in range(self.snake.stoned):
            self.mirage.append(self.get_random_cell())   

    def update_objects(self):
        self.display_window.blit(self.background,(0,0))
        for cell in self.snake.body_queue:
            cell.colour_it()
            self.display_window.blit(cell.image,cell.pos)
        self.display_window.blit(self.food_cell.image,self.food_cell.pos)
        if self.food_cell in self.snake.body_queue:
            self.food_cell = self.get_random_cell()
            self.food_cell.occupied = True
        if time() - self._time > 0.25:
           self.new_mirage()
           self._time = time()
        for cell in self.mirage:
            self.display_window.blit(cell.image,cell.pos)
        scoretext = self.myfont.render(f'Score: {len(self.snake.body_queue)-1}',1,(255,0,0))
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
                    elif event.key == py.K_p:
                        self.paused = not self.paused
                    
if __name__ == '__main__':
    py.init()
    game = MainDisplay()
    game.run()
