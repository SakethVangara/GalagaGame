# Names: Saketh Vangara, Hudson Alther
# Computing IDs: ssc2ry, dvu7jh

import uvage

walls = [
    uvage.from_color(0, 300, "black", 20, 1000),
    uvage.from_color(800, 300, "black", 20, 1000),
]

screen_width = 800
screen_height = 600
camera = uvage.Camera(screen_width, screen_height)

#backup code
#game_images = uvage.load_sprite_sheet("Galaga_Sprites.png",11,25)
#player = uvage.from_image(400,300,game_images[6]) backup code

background = uvage.from_image(screen_width, screen_height, "galaga_bg.gif")
player = uvage.from_image(400,550,"ship.png")
#bullet = uvage.from_image(player.x, player.y, "galaga_bullet.png")

player.scale_by(0.1)
background.scale_by(5)
#bullet.scale_by(0.03)

player_velocity = 8
#bullet_velocity = 50

game_on = True

def tick():
    #global bullet_velocity
    player.xspeed = player_velocity
    if game_on:
        if uvage.is_pressing("left arrow"):
            player.x -= player.xspeed
            #bullet.x -= player.xspeed
        if uvage.is_pressing("right arrow"):
            player.x += player.xspeed
            #bullet.x += player.xspeed
        #if uvage.is_pressing("space"):
            #bullet.yspeed = bullet_velocity
            #bullet.y -= bullet.yspeed

        #if bullet.y <= 0:
            #bullet.x = player.x
            #bullet.y = player.y

        background.yspeed = 2
        background.y -= background.yspeed
        if background.y <= 0:
            background.y = 600

        if player.touches(walls[0]):
            player.move_to_stop_overlapping(walls[0])
        elif player.touches(walls[1]):
            player.move_to_stop_overlapping(walls[1])

    camera.draw(background)
    camera.draw(player)
    for wall in walls:
        camera.draw(wall)
    #camera.draw(bullet)
    camera.display()

uvage.timer_loop(30, tick)
