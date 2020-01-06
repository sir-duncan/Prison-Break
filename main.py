import os
import sys
import time
import pygame
from menu import *

blockSize = (48, 48)

class Perso():
    def __init__(self, pos):
        self.it = 0
        self.dir = 2 # N:0  E:1  S:2  O:3
        self.size = [30, 40]
        self.coor = [pos[0], pos[1]] # life etc...
        self.state = "AFK"
        self.rect = pygame.Rect(self.coor[0] - (self.size[0] / 2), self.coor[1] - (self.size[1] / 2), self.size[0], self.size[1])
    def update(self):
        self.rect = pygame.Rect(self.coor[0] - (self.size[0] / 2), self.coor[1] - (self.size[1] / 2), self.size[0], self.size[1])

pygame.init() # Program initiats
size = width, height = 1920, 1080#1500, 700
<<<<<<< HEAD
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 60)
screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)
=======
#infoObject = pygame.display.Info()
#pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
>>>>>>> fab3b18eb77d46baa8ed342b1227217b11853b4c
pygame.font.init()
pygame.mouse.set_visible(False)

black = 0, 0, 0
red = 255, 0, 0
blue = 0, 0, 255
white = 255, 255, 255

map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # A refaire sans attendre
    [1, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

pygame.display.set_caption("Prison Break")

movingKey = [pygame.K_s, pygame.K_w, pygame.K_d, pygame.K_a]
size_perso = w, h = 31, 48
x, y = 16, 526
move = False
# Loading image
image = pygame.image.load(".\\Data\\Perso_test.png")
heroPic = pygame.Surface(size_perso)
color = (0, 0, 240)
background = pygame.Surface(size)
draw_map(background, map, blockSize)

monPerso = Perso((120, 120))
pnj = (Perso((500, 120)), Perso((700, 120)))
pnj[1].state = "Moving"
iPressed = False

mainMenu(screen, size)

movement = time.time()
timerAnimation = time.time()
while True:
    screen.blit(background, (0, 0), (0, 0, width, height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in movingKey and monPerso.state == "AFK": monPerso.state = "Moving"

    if time.time() - movement > 0.004:
        updatePnj(pnj[1])
        iPressed = detection(monPerso, map, blockSize, movingKey, iPressed)
        movement = time.time()

    if (time.time() - timerAnimation) > 0.07:
        timerAnimation = time.time()
        animatePnj(pnj[1])
        if monPerso.state == "Moving":
            key = pygame.key.get_pressed()
            if (key[movingKey[0]] or key[movingKey[1]] or key[movingKey[2]] or key[movingKey[3]]):
                monPerso.it += 1
                if monPerso.it > 8 : monPerso.it = 1
            else: monPerso.state, monPerso.it = "AFK", 0

    #pygame.draw.rect(screen, (0, 0, 240), monPerso.rect)
    for dumb in pnj:
        if monPerso.rect.x < dumb.rect.x + dumb.rect.width and monPerso.rect.x + monPerso.rect.width > dumb.rect.x and monPerso.rect.y < dumb.rect.y + dumb.rect.height and monPerso.rect.y + monPerso.rect.height > dumb.rect.y:
            #display lower y first -> collision with dumb
            for dumb2 in pnj:
                if dumb2 != dumb: screen = displayPerso(dumb2, screen, image, heroPic, size_perso, color)
                if dumb2 == dumb:
                    if dumb.rect.y > monPerso.rect.y:
                        screen = displayPerso(monPerso, screen, image, heroPic, size_perso, color)
                        screen = displayPerso(dumb, screen, image, heroPic, size_perso, color)
                    else:
                        screen = displayPerso(dumb, screen, image, heroPic, size_perso, color)
                        screen = displayPerso(monPerso, screen, image, heroPic, size_perso, color)
            break
    else: #whatever
        color = (0, 0, 240)
        screen = displayPerso(monPerso, screen, image, heroPic, size_perso, color)
        for dumb in pnj: displayPerso(dumb, screen, image, heroPic, size_perso, color)
    #pygame.transform.scale(screen, (width, height), screen)
    if monPerso.state == "Inventory": iPressed = invertoryMenu(screen, size, monPerso)
    if monPerso.state == "Pause": pauseMenu(screen, size, monPerso)
    pygame.display.flip()
