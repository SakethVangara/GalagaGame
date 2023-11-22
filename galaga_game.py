# Names: Saketh Vangara, Hudson Alther
# Computing IDs: ssc2ry, dvu7jh

import uvage

screen_width = 800
screen_height = 600
camera = uvage.Camera(screen_width, screen_height)

game_on = True
class Game:
    global camera
    def __init__(self):
        #placeholder
        pass

    def run(self):
        camera.display()

def tick():
    game = Game()
    if game_on:
        game.run()

uvage.timer_loop(30, tick)
