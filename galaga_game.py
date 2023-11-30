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
bullets = [uvage.from_image(player.x, player.y, "galaga_bullet.png")]

for each in bullets:
    each.scale_by(0.5)
player.scale_by(0.1)
background.scale_by(5)
player_velocity = 8
bullet_velocity = 40

current_frame = 0
game_on = True

enemy_type1 = uvage.load_sprite_sheet("galaga_enemy1_sprite.png", 1, 8)
enemy_type1_list = [
    uvage.from_image(200, 200, enemy_type1[7]),
    uvage.from_image(300, 200, enemy_type1[7]),
    uvage.from_image(400, 200, enemy_type1[7]),
    uvage.from_image(500, 200, enemy_type1[7]),
    uvage.from_image(600, 200, enemy_type1[7])
]
for each in enemy_type1_list:
    each.scale_by(0.5)

def tick():
    global bullet_velocity
    global current_frame
    player.xspeed = player_velocity
    if game_on:
        if uvage.is_pressing("left arrow"):
            player.x -= player.xspeed
            #bullet.x -= player.xspeed
        elif uvage.is_pressing("right arrow"):
            player.x += player.xspeed
            #bullet.x += player.xspeed

        background.yspeed = 2
        background.y -= background.yspeed
        if background.y <= 0:
            background.y = 600

        if player.touches(walls[0]):
            player.move_to_stop_overlapping(walls[0])
        elif player.touches(walls[1]):
            player.move_to_stop_overlapping(walls[1])

        for i in range(0, len(bullets)):
            if uvage.is_pressing("space"):
                bullets.append(uvage.from_image(player.x, player.y, "galaga_bullet.png"))
                #for each in bullets:
                    #each.scale_by(0.05)
            bullets[i].yspeed = 10
            bullets[i].y -= bullets[i].yspeed
            #if bullets[i].y >= 0:
                #bullets.remove(bullets[i])
        for enemy in enemy_type1_list:
            enemy.speedx = 2
            enemy.speedy = 2
            current_frame += 0.3
            if current_frame >= 8:
                current_frame = 0
            enemy.image = enemy_type1[int(current_frame)]
            enemy.move_speed()
            #if enemy.x >= 400:
                #enemy.flip()
                #enemy.move_speed()

    camera.draw(background)
    camera.draw(player)
    for wall in walls:
        camera.draw(wall)
    for i in enemy_type1_list:
        camera.draw(i)
    for bullet in bullets:
        camera.draw(bullet)
    camera.display()

uvage.timer_loop(30, tick)
