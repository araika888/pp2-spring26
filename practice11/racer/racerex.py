import pygame
import sys
import random 
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer")

blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

score = 0
speed = 4
coins = 0

width = 400
height = 600

#Font
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

pygame.mixer.init()

background = pygame.image.load("AnimatedStreet.png")
player = pygame.transform.scale(pygame.image.load("Player.png"), (60,100))
enemy = pygame.transform.scale(pygame.image.load("Enemy.png"),(60,100))
coin_bronze = pygame.transform.scale(pygame.image.load("coiin.png"), (25,25))  # маленькая
coin_silver = pygame.transform.scale(pygame.image.load("coiin.png"), (35,35))  # средняя
coin_gold   = pygame.transform.scale(pygame.image.load("coiin.png"), (45,45))  # большая
crash = pygame.mixer.Sound("crash.mp3")

playerrect = player.get_rect()
playerrect.center = (160,520)

enemyrect = enemy.get_rect()
enemyrect.center = (random.randint(40, width - 40),0)
coin_type=1 # Начальный тип монеты (1=бронза, 2=серебро, 3=золото)

coinrect = coin_bronze.get_rect()
coinrect.center = (random.randint(40, width - 40), -100)

inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

def move_player():
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT] and playerrect.left > 0:
        playerrect.move_ip(-5,0)

    if pressed_keys[K_RIGHT] and playerrect.right < width:
        playerrect.move_ip(5,0)

def move_enemy():
    global score
    enemyrect.move_ip(0, speed)

    if enemyrect.top > height:
        score += 1
        enemyrect.center = (random.randint(40, width - 40), 0)

def move_coin():
    # Если монета вышла за экран — появляется сверху со случайным типом
    global coins, coin_type ,speed
    coinrect.move_ip(0, speed-2)

    if coinrect.top > height:
        coinrect.center = (random.randint(40, width - 40), -50)
        coin_type = random.choices([1, 2, 3], weights=[60, 30, 10])[0]  # бронза чаще, золото реже

    if playerrect.colliderect(coinrect):
        # Начисляем очки в зависимости от типа монеты
        if coin_type == 1:
            coins += 1   # бронза +1
        elif coin_type == 2:
            coins += 3   # серебро +3
        elif coin_type == 3:
            coins += 5   # золото +5
        if coins % 5 == 0:
            speed+=1 #если каждый раз очко больше чем 5 то скорость умножается
        coinrect.center = (random.randint(40, width - 40), -50)
        coin_type = random.choices([1, 2, 3], weights=[60, 30, 10])[0]

backgroundsound = pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == inc_speed:
            speed += 0.5
        
    screen.blit(background, (0,0))

    scoretext = font_small.render("Score: " + str(score), True, black)
    screen.blit(scoretext, (10,10))

    coin_text = font_small.render("Coins: " + str(coins), True, black)
    screen.blit(coin_text, (280,10))

    move_player()
    move_enemy()
    move_coin()

    screen.blit(player, playerrect)
    screen.blit(enemy, enemyrect)
    # Отображаем монету нужного типа
    if coin_type==1:
        screen.blit(coin_bronze,coinrect)
    elif coin_type==2:
        screen.blit(coin_silver,coinrect)
    elif coin_type==3:
        screen.blit(coin_gold,coinrect)

    if playerrect.colliderect(enemyrect):
        pygame.mixer.music.pause()
        crash.play()

        screen.fill(red)
        screen.blit(game_over, (30,250))
        pygame.display.update()
        
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(60)     