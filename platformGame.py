

import pgzrun




# Variables
TITLE = "Platform Game"
WIDTH = 800
HEIGHT = 500
player = Rect((100, 400), (40, 40))
velocity_y = 0
gravity = 1
on_ground = False

#Platforms
platforms = [
    Rect((0, 470), (800, 30)),
    Rect((100, 380), (150, 20)),
    Rect((150, 250), (150, 20)),
    Rect((300, 150), (20, 1000)),
    Rect((415, 150), (20, 1000)),
    Rect((650, 375), (100, 20))

]

#Coins
coins = [
    Rect((150, 340), (20, 20)),
    Rect((500, 260), (20, 20)),
    Rect((690, 340), (20, 20))
]

#Hazards
lava = Rect((315, 170), (100, 970))

#Win conditions
goal = Rect((730, 420), (40, 50))
game_won = False


score = 0

#Draw
def draw():
    screen.clear()
    screen.draw.filled_rect(player, "blue")

    for platform in platforms:
        screen.draw.filled_rect(platform, "green")

    for coin in coins:
        screen.draw.filled_rect(coin, "yellow")

    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")

    screen.draw.filled_rect(lava, "red")

    screen.draw.filled_rect(goal, "purple")

    if game_won:
        screen.draw.text("You Win!", center=(400, 250), fontsize=60, color="yellow")


#Code
def update():
    global velocity_y, on_ground

    velocity_y += gravity
    player.y += velocity_y

    global score

    for coin in coins[:]:
        if player.colliderect(coin):
            coins.remove(coin)
            score += 1

    if player.colliderect(lava):
        player.x = 100
        player.y = 400
        velocity_y = 0

    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
        velocity_y = 0
        on_ground = True

    on_ground = False

    for platform in platforms:
        if player.colliderect(platform) and velocity_y > 0:
            player.bottom = platform.top
            velocity_y = 0
            on_ground = True

    if player.right > WIDTH:
        player.right = WIDTH

    if keyboard.space and on_ground:
        velocity_y = -15
        on_ground = False

    
    if keyboard.left and player.left != platform.right:
        player.x -= 5
    else:
        player.x -= 0

    if keyboard.right and player.right != platform.left:
        player.x += 5
    else:
        player.x += 0


    if player.left < 0:
        player.left = 0




    global game_won

    if player.colliderect(goal) and score == 3:
        game_won = True



pgzrun.go()
