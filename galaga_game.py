# Names: Saketh Vangara, Hudson Alther
# Computing IDs: ssc2ry, dvu7jh

                                    # README / HOW TO PLAY THE GAME #
# The game that we made was a variation of the classic Galaga game. To play the game,
# run the "galaga_game.py" file (which you are currently on), and the game will automatically start.
# The player/user controls the ship at the bottom of the screen, and can move left using the left arrow key,
# and right using the right arrow key. The player/user can shoot the enemies (alien-like objects) by pressing the
# space button, and when a bullet collides with an enemy, the enemy disappears and the user's score increases
# by some amount, depending on the enemy type. Eliminating the red enemies awards the user 100 points, the green enemies
# award 200 points, and the purple enemies award 300 points. The goal of the game is to eliminate all of the enenmies
# before the timer hits zero, and without running out of lives. Have fun!


# Importing the UVA Game Engine
import uvage

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
player_bullets = [uvage.from_image(0, 0, "galaga_bullet.png")]

# Scaling the placeholder bullet, as well as the player and background, to make
# their sizes look realistic.
player_bullets[0].scale_by(0.05)
player.scale_by(0.1)
background.scale_by(5)

# Setting the player velocity to 8; this variable is referenced
# later for the player's x speed, or how fast they move in
# the x (horizontal) direction.
player_velocity = 8

# Other important variables that allow the game to function
# properly, such as the frame for sprite animation, a boolean named game_on
# for the game to actually work/run, player lives, timer, score, etc
current_frame = 6
game_on = True
space = False
hit = False
Win = False
lives = 3
timer = 100
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


    def player_enemy_collison():
        global restart, hit
        global game_on, lives
        for enemy in enemy_type1_list:
            if player.touches(enemy):
                enemy.x = 50
                enemy.xspeed = 2
                enemy.y = 200
                if hit == False:
                    lives -= 1
                    hit = True
        for enemy in enemy_type2_list:
            if player.touches(enemy):
                enemy.x = 50
                enemy.xspeed = 2
                enemy.y = 200
                if hit == False:
                    lives -= 1
                    hit = True
        for enemy in enemy_type3_list:
            if player.touches(enemy):
                enemy.x = 50
                enemy.xspeed = 2
                enemy.y = 200
                if hit == False:
                    lives -= 1
                    hit = True
        if hit == True and int(timer) % 5 == 0:
            hit = False





             # draw_stuff() FUNCTION #
# The draw_stuff() function contains every call
# to which the camera draws some variable. Here, the background,
# invisible walls, enemies (of all types), bullets, score, timer,
# and lives (hearts) are drawn on the screen when the function is called.
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

    for i in range(lives):
        heart = uvage.from_image(125, 25, 'heart.png')
        heart.x -= 50 * i
        heart.scale_by(0.2)
        camera.draw(heart)


                                     # RESTART FUNCTION #
# The restart function below houses code which is intended to run if the timer hits zero or if the user
# runs out of lives. If either of the following occur, then the boolean "game_on" is set to false, the camera
# is cleared, and the user will see a game over screen, with their score as well. After this screen appears,
# the user is prompted to press the enter/return key if they would like to restart the game, in which
# all of their progress is reset and the game starts over from the beginning. The other functions that are
# called at the end of the restart function (enemy_movement, player_shooting, and draw_stuff) are explained
# somewhere above or below this function.

# NOTE: The enemy type lists and the code from the enemy setup are found here because they are necessary
# for the enemies to be redrawn on the screen at their original spots. If they were in a function and the function
# was called, this would not work as intended, so instead, the original code is duplicated and seen below.
def restart():
    global game_on, timer, score, lives, space, enemy_type1_list, enemy_type2_list, enemy_type3_list, xpos1, xpos2, xpos3, Win
    # If the timer hits zero, game_on is false and the game over screen appears
    if int(timer) == 0 or lives == 0 or Win == True:
        game_on = False
        Win = False
        camera.clear("black")
        camera.draw(uvage.from_text(screen_width // 2, screen_height // 2, "GAME OVER", 50, "Red"))
        camera.draw(uvage.from_text(screen_width // 2, screen_height // 2 + 30, "Score: " + str(int(score)), 30, "Red"))
        camera.draw(uvage.from_text(screen_width // 2, screen_height // 2 + 60, "To restart, press enter", 50, "Red"))

        # If the return/enter key is pressed after the timer hits zero,
        # the game restarts from the beginning
        if uvage.is_pressing("return"):
            timer = 100
            score = 0
            lives = 3
            game_on = True

            enemy_type1_list = [
                uvage.from_image(xpos1, 200, enemy_type1[6]),
                uvage.from_image(xpos1 + 100, 200, enemy_type1[6]),
                uvage.from_image(xpos1 + 200, 200, enemy_type1[6]),
                uvage.from_image(xpos1 + 300, 200, enemy_type1[6]),
                uvage.from_image(xpos1 + 400, 200, enemy_type1[6])
            ]

            enemy_type2_list = [
                uvage.from_image(xpos2, 100, enemy_type2[6]),
                uvage.from_image(xpos2 + 100, 100, enemy_type2[6]),
                uvage.from_image(xpos2 + 200, 100, enemy_type2[6]),
                uvage.from_image(xpos2 + 300, 100, enemy_type2[6]),
                uvage.from_image(xpos2 + 400, 100, enemy_type2[6])
            ]

            enemy_type3_list = [
                uvage.from_image(xpos3, 300, enemy_type3[6]),
                uvage.from_image(xpos3 + 100, 300, enemy_type3[6]),
                uvage.from_image(xpos3 + 200, 300, enemy_type3[6]),
                uvage.from_image(xpos3 + 300, 300, enemy_type3[6]),
                uvage.from_image(xpos3 + 400, 300, enemy_type3[6])
            ]

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

            enemy_movement()
            player_shooting()
            draw_stuff()

                            # PLAYER_SHOOTING FUNCTION #
# The player_shooting() function below handles what occurs
# when the player/user presses the space buttons. Essentially,
# for each "thing" that is in the range of 0 and the length of the player_bullets
# list, if the user presses the space button and "space" (placeholder term) is false,
# "space" becomes set to true, a bullet is added to the player_bullets list and is scaled down.
# Other critical features, such as the bullet speed and the bullets position, are also included
# in the overarching for loop, in which the y speed is set to 15 and the position of a bullet changes
# by the y speed. Lastly, the final if statement focuses on resetting the bullet if it goes off screen.

def player_shooting():
    global space, score, timer, lives
    for i in range(0, len(player_bullets)):
        if uvage.is_pressing("space") and space == False:
            space = True
            player_bullets.append(uvage.from_image(player.x, player.y, "galaga_bullet.png"))
            for each in player_bullets:
                each.scale_by(0.05)
        player_bullets[i].yspeed = 15
        player_bullets[i].y -= player_bullets[i].yspeed
        if player_bullets[i].y <= 0 and i > 0:
            player_bullets.remove(player_bullets[i])
            space = False

                         # ENEMY MOVEMENT FUNCTION #
# The enemy_movement() function houses three overarching for loops,
# one for the list of each enemy type. Each for loop does the same thing,
# but for the varying enemy types. These features include moving an enemy down and
# in the opposite direction if it touches the invisible wall on the left or
# right side of the screen, (at x = 25 or x = 770), animating each enemy, resetting the current frame
# if it is greater than or equal to 7, and moving the enemies through the use of the move_speed()
# method in uvage.

def enemy_movement():
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

                    # PLAYER BULLET TO ENEMY COLLISIOn FUNCTION #
# This function, again, has three overarching for loops, one for each enemy type's list,
# as the for loops handle what occurs if a bullet were to touch an enemy object. If a
# bullet touches an enemy, then that specific enemy is removed from the list, as well as the bullet,
# "space" (placeholder) becomes false, and the score increases by 100, 200, or 300, depending on the enemy type.
def player_bullet_enemy_collision():
    global space, score, timer, lives, enemy_type_1_eliminated, enemy_type_2_eliminated, enemy_type_3_eliminated
    for bullet in player_bullets:
        for enemy in enemy_type1_list:
            if bullet.touches(enemy):
                enemy_type1_list.remove(enemy)
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

def win():
    global lives, timer, Win
    if len(enemy_type1_list) == 0 and len(enemy_type2_list) == 0 and len(enemy_type3_list) == 0:
         if lives > 0 and timer > 0:
             camera.clear("black")
             camera.draw(uvage.from_text(screen_width // 2, screen_height // 2, "YOU WIN! CONGRATS!", 50, "Red"))
             camera.draw(uvage.from_text(screen_width // 2, screen_height // 2 + 30, "Score: " + str(int(score)),30, "Red"))
             camera.draw(uvage.from_text(screen_width // 2, screen_height // 2 + 60,"To replay the game, press return/enter", 30, "Red"))

    if uvage.is_pressing("return"):
        Win = True
        restart()

                            # TICK FUNCTION #
# Every uvage program generally ends with a tick() function, and our program is no different.
# The tick function houses most of the gameplay, in which if the game_on variable is True, then
# the Galaga-style game will actually run, as the player can move using the left and right arrow keys,
# the background scrolls infinitely, player and wall collision is accounted for, and the functions
# created and described abvoe are all called in the tick function, making the program work as intended.
def tick():
    global bullet_velocity, space, game_on, timer, score, coin_counter, lives
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

        # Calling the player_shooting(), enemy_movement(), and player_bullet_enemy_collision()
        # functions
        player_shooting()
        enemy_movement()
        player_bullet_enemy_collision()

    # Calling the draw_stuff() and restart() functions,
    # and displaying everything on the screen.
    draw_stuff()
    restart()
    win()
    camera.display()
uvage.timer_loop(30, tick)
