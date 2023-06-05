import pygame
from pygame import init, display, time, font, mixer, image, key
from random import randrange

init()

screen = display.set_mode((500, 1000))
clock = time.Clock()

scoreFont = font.Font("fonts/Rubik-weight.ttf", 25)
gameoverFont = font.Font("fonts/Rubik-weight.ttf", 75)
restartFont = font.Font("fonts/Rubik-weight.ttf", 30)
keyboardcommandFont = font.Font("fonts/Rubik-weight.ttf", 20)

mixer.music.load("music/Music.wav")
mixer.music.play(-1)
mixer.music.set_volume(0.5)

background = image.load("images/Background.png")

score, highscore = 0, 0
gameover = False
can_move = True

playerImage = image.load("images/Player.png")
playerX, playerY = 225, 475
playerWidth, playerHeight = 50, 50
playerSpeed = 10

enemyImage = image.load("images/Enemy.png")
enemyX, enemyY = 0, randrange(1000)
enemyWidth, enemyHeight = 30, 30
enemySpeed = 20

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pressed = key.get_pressed()
    if can_move:
        if pressed[pygame.K_LEFT]: # Move Left
            playerX -= playerSpeed
        elif pressed[pygame.K_RIGHT]: # Move Right
            playerX += playerSpeed

    if pressed[pygame.K_SPACE] and gameover: # Restart
        playerX, playerY = 225, 475
        can_move = True

    if pressed[pygame.K_ESCAPE]: # Quit
        pygame.quit()

    enemyY += enemySpeed # Spawn-Random-Enemy
    if enemyY >= 1000:
        enemyX, enemyY = randrange(480), 0

    if score % 200 == 0: # Enemy-Speed-Increase
        enemySpeed += 0.5

    playerX = max(0, min(playerX, 450)) # Player-Screen-Barrier

    screen.blit(background, (0, 0))
    enemy = screen.blit(enemyImage, (enemyX, enemyY, enemyWidth, enemyHeight))
    player = screen.blit(playerImage, (playerX, playerY, playerWidth, playerHeight))

    scoretext = scoreFont.render("Score: " + str(score), 1, (255, 255, 255))
    screen.blit(scoretext, (20, 20))
    highscoretext = scoreFont.render("Highscore: " + str(highscore), 1, (255, 255, 255))
    screen.blit(highscoretext, (20, 60))
    score += 1

    keyboardlefttext = keyboardcommandFont.render("Movement-Left = Key LEFT", 1, (255, 255, 255))
    screen.blit(keyboardlefttext, (20, 930))
    keyboardrighttext = keyboardcommandFont.render("Movement-Right = Key RIGHT", 1, (255, 255, 255))
    screen.blit(keyboardrighttext, (20, 960))

    if player.colliderect(enemy): # Player-Enemy-Collide
        gameover = True
        can_move = False
        playerX, playerY = 225, 515
        enemyX, enemyY = 235, 510
        enemySpeed = 20

        if score > highscore: # Set Highscore
            highscore = score
        score = 0

        gameovertext = gameoverFont.render("Game Over", 1, (255, 75, 75))
        screen.blit(gameovertext, (60, 375))
        restarttext = restartFont.render("Press Space to restart", 1, (255, 255, 255))
        screen.blit(restarttext, (95, 450))

    display.update()
    clock.tick(60)
