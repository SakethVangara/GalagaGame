# Names: Saketh Vangara, Hudson Alther
# Computing IDs: ssc2ry, dvu7jh

# Importing the UVA Game Engine
import uvage
import random
# Initial Setup - creating the camera variable
# with screen width 800 and screen height 600.
screen_width = 800
screen_height = 600
camera = uvage.Camera(screen_width, screen_height)

# Generating the invisible walls which serve as the boundaries
# that the player cannot go beyond.
walls = [
    uvage.from_color(0, 300, "black", 20, 1000),
    uvage.from_color(800, 300, "black", 20, 1000),
]

# Creating the core variables that allow the game to work the way it is intended to.
# These include the background, player, and the bullets that the player shoots, as they are
# all created from the uvage.from_image method.
# Bullets are stored in a list called "bullets" which is later transformed (through an
# addition or removal of a bullet).
background = uvage.from_image(screen_width, screen_height, "galaga_bg.gif")
player = uvage.from_image(400,550,"ship.png")
player_bullets = [uvage.from_image(0, 0, "player_bullet.png")]
coin_list = [
    uvage.from_image(random.randint(200, 400), random.randint(300, 400), "coin.png"),
    uvage.from_image(random.randint(200, 400), random.randint(300, 400), "coin.png"),
    uvage.from_image(random.randint(200, 400), random.randint(300, 400), "coin.png"),
    uvage.from_image(random.randint(200, 400), random.randint(300, 400), "coin.png"),
    uvage.from_image(random.randint(200, 400), random.randint(300, 400),"coin.png"),
    uvage.from_image(random.randint(200, 400), random.randint(300, 400), "coin.png"),
    uvage.from_image(random.randint(200, 400), random.randint(300, 400), "coin.png"),
    uvage.from_image(random.randint(200, 400), random.randint(300, 400), "coin.png")

]
coin_counter = 0

# Scaling the placeholder bullet, as well as the player and background, to make
# their sizes look realistic.
player_bullets[0].scale_by(0.05)
player.scale_by(0.1)
background.scale_by(5)

# Setting the player velocity to 8; this variable is referenced
# later for the player's x speed, or how fast they move in
# the x (horizontal) direction
player_velocity = 8

current_frame = 6
game_on = True
space = False
lives = 3
timer = 10
score = 0
enemy_type_1_eliminated = 0
enemy_type_2_eliminated = 0
enemy_type_3_eliminated = 0

                        # ENEMY CREATION #
# Below, you can find the various enemy types that will be used in the game,
# as they are created (from the image) and stored using the uvage.load_sprite_sheet
# method. Each enemy type has their own list, containing 5 objects of that
# specific enemy type.

xpos1 = 200
xpos2 = 250
xpos3 = 300
enemy_type1 = uvage.load_sprite_sheet("galaga_enemy1_sprite.png", 1, 8)
enemy_type1_list = [
    uvage.from_image(xpos1, 200, enemy_type1[6]),
    uvage.from_image(xpos1 + 100, 200, enemy_type1[6]),
    uvage.from_image(xpos1 + 200, 200, enemy_type1[6]),
    uvage.from_image(xpos1 + 300, 200, enemy_type1[6]),
    uvage.from_image(xpos1 + 400, 200, enemy_type1[6])
]

enemy_type2 = uvage.load_sprite_sheet("galaga_enemy2_sprite.png", 1, 8)
enemy_type2_list = [
    uvage.from_image(xpos2, 100, enemy_type2[6]),
    uvage.from_image(xpos2 + 100, 100, enemy_type2[6]),
    uvage.from_image(xpos2 + 200, 100, enemy_type2[6]),
    uvage.from_image(xpos2 + 300, 100, enemy_type2[6]),
    uvage.from_image(xpos2 + 400, 100, enemy_type2[6])
]

enemy_type3 = uvage.load_sprite_sheet("galaga_enemy3_sprite.png", 1, 8)
enemy_type3_list = [
    uvage.from_image(xpos3, 300, enemy_type3[6]),
    uvage.from_image(xpos3 + 100, 300, enemy_type3[6]),
    uvage.from_image(xpos3 + 200, 300, enemy_type3[6]),
    uvage.from_image(xpos3 + 300, 300, enemy_type3[6]),
    uvage.from_image(xpos3 + 400, 300, enemy_type3[6])
]

                # ENEMY SETUP #
# Below are for loops which traverse through the lists
# of each enemy type, giving each element a certain x and y speed,
# as well as scaling them to be half of their original size.

for i in range(0, len(enemy_type1_list)):
    enemy_type1_list[i].speedx = 2
    enemy_type1_list[i].speedy = 0
    enemy_type1_list[i].scale_by(0.5)

for i in range(0, len(enemy_type2_list)):
    enemy_type2_list[i].speedx = 2
    enemy_type2_list[i].speedy = 0
    enemy_type2_list[i].scale_by(0.5)

for i in range(0, len(enemy_type3_list)):
    enemy_type3_list[i].speedx = 2
    enemy_type3_list[i].speedy = 0
    enemy_type3_list[i].scale_by(0.5)

def handle_coins():
    global coin_counter, lives
    for each in range(len(coin_list)):
        coin_list[each].yspeed = 2
        coin_list[each].y += coin_list[each].yspeed
        if player.touches(coin_list[each]):
            coin_counter += 1
            coin_list.remove(coin_list[each])
        for coin in coin_list:
            camera.draw(coin)

    if coin_counter == 8:
        lives += 1


        # draw_stuff() FUNCTION #
# The draw_stuff() function contains every call
# to which the camera draws some variable. Currently,
# the following is drawn on the screen: background,
# player, walls, enemies, and bullets.
def draw_stuff():
    camera.draw(background)
    camera.draw(player)
    for wall in walls:
        camera.draw(wall)
    for first_enemy in enemy_type1_list:
        camera.draw(first_enemy)
    for second_enemy in enemy_type2_list:
        camera.draw(second_enemy)
    for third_enemy in enemy_type3_list:
        camera.draw(third_enemy)
    for bullet in player_bullets:
        camera.draw(bullet)
    camera.draw(uvage.from_text(50, 550, "TIME: " + str(int(timer)), 40, "red"))
    camera.draw(uvage.from_text(700, 30, "SCORE: " + str(int(score)), 40, "red"))
    camera.draw(uvage.from_text(700, 80, "COINS: " + str(int(coin_counter)), 40, "red"))

    for i in range(lives):
        heart = uvage.from_image(125, 25, 'heart.png')
        heart.x -= 50 * i
        heart.scale_by(0.2)
        camera.draw(heart)
    #restart()

#def restart():
    #global game_on, timer, score, lives, space, enemy_type1_list, enemy_type2_list, enemy_type3_list, xpos1, xpos2, xpos3
    #if int(timer) == 0:
        #game_on = False
        #camera.clear("black")
        #camera.draw(uvage.from_text(screen_width // 2, screen_height // 2, "GAME OVER", 50, "Red"))
        #camera.draw(uvage.from_text(screen_width // 2, screen_height // 2 + 30, "Score: " + str(int(score)), 30, "Red"))
        #camera.draw(uvage.from_text(screen_width // 2, screen_height // 2 + 60, "To restart, press enter", 50, "Red"))

        #if uvage.is_pressing("return"):
            #timer = 10
            #score = 0
            #enemy_setup()
            #player_shooting()
            #draw_stuff()
            #game_on = True

            #for each in range(0, enemy_type_1_eliminated):
                #enemy_type1_list.append(uvage.from_image(xpos1, 200, enemy_type1[6]).scale_by(0.5))

            #enemy_type1_list[0].x = xpos1
            #enemy_type1_list[1].x = xpos1 + 100
            #enemy_type1_list[2].x = xpos1 + 200
            #enemy_type1_list[3].x = xpos1 + 300

            #for enemy in enemy_type1_list:
                #enemy.image = enemy_type1[6]


def player_shooting():
    global space, score, timer, lives
    for i in range(0, len(player_bullets)):
        if uvage.is_pressing("space") and space == False:
            space = True
            player_bullets.append(uvage.from_image(player.x, player.y, "player_bullet.png"))
            for each in player_bullets:
                each.scale_by(0.05)
        player_bullets[i].yspeed = 15
        player_bullets[i].y -= player_bullets[i].yspeed
        if player_bullets[i].y <= 0 and i > 0:
            player_bullets.remove(player_bullets[i])
            space = False
def enemy_setup():
    global current_frame
    for i in range(0, len(enemy_type1_list)):
        if enemy_type1_list[i].x <= 25 or enemy_type1_list[i].x >= 770:
            enemy_type1_list[i].xspeed *= -1
            enemy_type1_list[i].y += 50
        enemy_type1_list[i].image = enemy_type1[current_frame]
        if current_frame >= 7:
            current_frame = 0
        enemy_type1_list[i].move_speed()

    for i in range(0, len(enemy_type2_list)):
        if enemy_type2_list[i].x <= 25 or enemy_type2_list[i].x >= 770:
            enemy_type2_list[i].xspeed *= -1
            enemy_type2_list[i].y += 50
            current_frame += 1
        enemy_type2_list[i].image = enemy_type2[current_frame]
        if current_frame >= 7:
            current_frame = 0
        enemy_type2_list[i].move_speed()

    for i in range(0, len(enemy_type3_list)):
        if enemy_type3_list[i].x <= 25 or enemy_type3_list[i].x >= 770:
            enemy_type3_list[i].xspeed *= -1
            enemy_type3_list[i].y += 50
            current_frame += 1
        enemy_type3_list[i].image = enemy_type3[current_frame]
        if current_frame >= 7:
            current_frame = 0
        enemy_type3_list[i].move_speed()

def player_bullet_enemy_collision():
    global space, score, timer, lives, enemy_type_1_eliminated, enemy_type_2_eliminated, enemy_type_3_eliminated
    for bullet in player_bullets:
        for enemy in enemy_type1_list:
            if bullet.touches(enemy):
                enemy_type1_list.remove(enemy)
                enemy_type_1_eliminated += 1
                player_bullets.remove(bullet)
                space = False
                score += 200

        for enemy in enemy_type2_list:
            if bullet.touches(enemy):
                enemy_type2_list.remove(enemy)
                enemy_type_2_eliminated += 1
                player_bullets.remove(bullet)
                space = False
                score += 300

        for enemy in enemy_type3_list:
            if bullet.touches(enemy):
                enemy_type3_list.remove(enemy)
                enemy_type_3_eliminated += 1
                player_bullets.remove(bullet)
                space = False
                score += 100

def tick():
    global bullet_velocity
    #global current_frame
    global space
    global game_on
    global timer
    global score
    player.xspeed = player_velocity

    if game_on:
        timer -= 0.045
        if uvage.is_pressing("left arrow"):
            player.x -= player.xspeed
        elif uvage.is_pressing("right arrow"):
            player.x += player.xspeed

        background.yspeed = 5
        background.y -= background.yspeed
        if background.y <= 0:
            background.y = 600

                # PLAYER AND BOUNDARY COLLISION #
        # Below one can find the code for collision between
        # a player and the left or right boundary, as we have
        # created invisible walls that the player cannot go beyond.
        # In other words, the player is only confined to move within
        # the two walls.
        if player.touches(walls[0]):
            player.move_to_stop_overlapping(walls[0])
        elif player.touches(walls[1]):
            player.move_to_stop_overlapping(walls[1])

        player_shooting()
        enemy_setup()
        player_bullet_enemy_collision()
        handle_coins()

    draw_stuff()
    #restart()
    camera.display()
uvage.timer_loop(30, tick)
