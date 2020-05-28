import pygame as py
from world import Space
from snake import Snake

class MainDisplay:
    def __init__(self):
        self.size = (750,750)
        self.world = Space(20)
        self.snake = Snake()

        self.fps = 2                #set frame rate, may change later
        self.clock = py.time.Clock()

        self.display_window = py.display.set_mode(self.size)
        self.background = py.Surface(self.display_window.get_size()).convert()
        self.background.fill((0,255,0))

        self.running = True

    def run(self):
        self.clock.tick(self.fps)
        while self.running:
            self.update_objects()           #redraw
            for event in py.event.get():    
                self.handle_event(event)    

    def update_objects(self):
        self.display_window.blit(self.background,(0,0))
        py.display.flip()

    def handle_event(self,event):
        if event.type == py.QUIT:
            self.running = False
            py.quit()

if __name__ == '__main__':
    game = MainDisplay()
    game.run()
