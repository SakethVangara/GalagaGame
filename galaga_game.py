# Names: Saketh Vangara, Hudson Alther
# Computing IDs: ssc2ry, dvu7jh

import uvage

walls = [
    uvage.from_color(300, 0, "black", 1000, 20),
    uvage.from_color(400, 600, "black", 1000, 20),

]

screen_width = 800
screen_height = 600
camera = uvage.Camera(screen_width, screen_height)
#game_images = uvage.load_sprite_sheet("Arcade - Galaga - General Sprites.png",11,25) backup code
#player = uvage.from_image(400,300,game_images[6]) backup code
player = uvage.from_image(400,550,"ship.png")
player.scale_by(0.1)

game_on = True
class Game:
    global camera
    def __init__(self):
        #placeholder
        pass

    def run(self):
        camera.display()

def tick():
    player.xspeed = 400
    player.x = player.xspeed
    game = Game()
    if game_on:
        game.run()
    if uvage.is_pressing("a"):
        player.x += -7
    if uvage.is_pressing("d"):
        player.x += 7




    camera.draw(player)
    camera.display()
uvage.timer_loop(30, tick)
