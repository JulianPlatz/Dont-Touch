import pygame
from random import randrange

pygame.init()

# Screen
screenWidth = 500
screenHeight = 1000

screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

# Window-Design
pygame.display.set_caption("Touch Not The Square")
icon = pygame.image.load("images/Icon.ico")
pygame.display.set_icon(icon)


# Fonts
scoreFont = pygame.font.Font("fonts/Rubik-VariableFont_wght.ttf", 25)
gameoverFont = pygame.font.Font("fonts/Rubik-VariableFont_wght.ttf", 75)
restartFont = pygame.font.Font("fonts/Rubik-VariableFont_wght.ttf", 30)
keyboardcommandFont = pygame.font.Font("fonts/Rubik-VariableFont_wght.ttf", 20)


# Music
mp3File = "music/Music.mp3"
pygame.mixer.music.load(mp3)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

# Player
playerImage = pygame.image.load("images/Player.png")
playerX = 475
playerY = 475
playerWidth = 50
playerHeight = 50
playerSpeed = 10

# Enemy
enemyImage = pygame.image.load("images/Enemy.png")
enemyX = 0
enemyY = randrange(screenHeight)
enemyWidth = 30
enemyHeight = 30
enemySpeed = 20

# Score
score = 0
highscore = 0

gameover = False

can_move = True

background = pygame.image.load("images/Background.png")

is_running = True
# Programm loop
while is_running:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # Player Movement
    pressed = pygame.key.get_pressed()
    if can_move:
        if pressed[pygame.K_RIGHT]:
            playerX += playerSpeed
        elif pressed[pygame.K_d]:
            playerX += playerSpeed

        if pressed[pygame.K_LEFT]:
            playerX -= playerSpeed
        elif pressed[pygame.K_a]:
            playerX -= playerSpeed

    # Restart Game
    if pressed[pygame.K_SPACE] and gameover:
        playerX = 475
        playerY = 475
        can_move = True

    # Quit Game
    if pressed[pygame.K_ESCAPE]:
        pygame.quit()

        enemyX = 0
        enemyY = randrange(screenHeight)

        gameover = False

    # Enemy Spawn
    enemyY += enemySpeed
    if enemyY >= screenHeight:
        enemyY = 0
        enemyX = randrange(480)

    # Enemy Speed
    if score % 200 == 0:
        enemySpeed += 0.5

    # Barriere rechts/links
    if playerX <= 0:
        playerX = 0
    elif playerX >= 450:
        playerX = 450

    # Barriere oben/unten
    if playerY <= 0:
        playerY = 0
    elif playerY >= 950:
        playerY = 950

    screen.blit(background, (0, 0))

    # Player and Enemy
    enemy = screen.blit(enemyImage, (enemyX, enemyY, enemyWidth, enemyHeight))
    player = screen.blit(playerImage, (playerX, playerY, playerWidth, playerHeight))

    # Collider
    if player.colliderect(enemy):
        playerX = 225
        playerY = 515
        enemyX = 235
        enemyY = 510
        can_move = False

        if score > highscore:
            highscore = score
        score = 0

        # Gameover
        gameovertext = gameoverFont.render("Game Over", 1, (255, 75, 75))
        screen.blit(gameovertext, (60, 375))

        restarttext = restartFont.render("Press Space to restart", 1, (255, 255, 255))
        screen.blit(restarttext, (95, 450))
        score = score + 0
        enemySpeed = 20
        gameover = True

    # Score
    scoretext = scoreFont.render("Score: " + str(score), 1, (255, 255, 255))
    screen.blit(scoretext, (20, 20))
    highscoretext = scoreFont.render("Highscore: " + str(highscore), 1, (255, 255, 255))
    screen.blit(highscoretext, (20, 60))
    score = score + 1

    # Keyboard Commands
    keyboardlefttext = keyboardcommandFont.render("Movement-Left = Key a", 1, (255, 255, 255))
    screen.blit(keyboardlefttext, (20, 930))
    keyboardrighttext = keyboardcommandFont.render("Movement-Right = Key d", 1, (255, 255, 255))
    screen.blit(keyboardrighttext, (20, 960))

    pygame.display.update()
    clock.tick(60)
