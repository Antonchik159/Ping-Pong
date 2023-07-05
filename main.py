import pygame
from pygame import *
from random import randint
from PyQt5.QtGui import QIcon
pygame.init()
font.init()
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
icon = pygame.image.load('pong.png')
pygame.display.set_icon(icon)
display.set_caption("Shuter")
background = image.load('background.jpg')

class GameSprite(sprite.Sprite):
    def __init__(self, pic, x, y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(pic), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > self.speed:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_o] and self.rect.y > self.speed:
            self.rect.y -= self.speed
        if keys[K_l] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed
        
left_rocket = Player('platform.png', 10, 100, 20, 80, 10)
right_rocket = Player('platform2.png', 670, 100, 20, 80, 10)
ball = GameSprite('ball.png', 255, 255, 30, 30, 10)

game = True
clock = time.Clock()
FPS = 30
# font1 = font.SysFont('Arial', 80)

# score_text = font1.render("You won!", True, (0, 255, 0))
# lose_text = font1.render("You lose!", True, (255, 0, 0))

finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        if finish != True:
            background = pygame.transform.scale(background, (win_width, win_height))
            window.blit(background, (0, 0))
            left_rocket.update_l()
            left_rocket.reset()
            right_rocket.update_r()
            right_rocket.reset()
            ball.reset()
            display.update()
        time.delay(FPS)