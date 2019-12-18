import os
import sys
import time
import pygame
from menu import *

hw, hh = 48, 48

class Perso():
    def __init__(self):
        self.dir = 2 # N:0  E:1  S:2  O:3
        self.size = [30, 40]
        self.coor = [120, 120] # life etc...
        self.state = "AFK"
        self.rect = pygame.Rect(self.coor[0] - (self.size[0] / 2), self.coor[1] - (self.size[1] / 2), self.size[0], self.size[1])
    def update(self):
        self.rect = pygame.Rect(self.coor[0] - (self.size[0] / 2), self.coor[1] - (self.size[1] / 2), self.size[0], self.size[1])

def draw_map(screen, map):
    ground = pygame.image.load(".\\Ground.png")
    for idy, inty in enumerate(map):
        for idx, intx in enumerate(inty):
            if intx == 1:
                pygame.draw.rect(screen, (50, 50, 50), ((idx * hw), (idy * hh), hw, hh))
            elif intx == 2:
                pygame.draw.rect(screen, (50, 10, 10), ((idx * hw), (idy * hh), hw, hh))
            elif intx == 0:
                screen.blit(ground, (idx * hw, idy * hh), (0, 0, hw, hh))
                #pygame.draw.rect(screen, (10, 50, 10), ((idx * hw), (idy * hh), hw, hh))

def detection(monPerso, map, iPressed): # key detection
    speed = 1
    x = [monPerso.coor[0] - (monPerso.size[0] / 2), monPerso.coor[0] + (monPerso.size[0] / 2)]
    y = [monPerso.coor[1] - (monPerso.size[1] / 2), monPerso.coor[1] + (monPerso.size[1] / 2)]
    tmpx, tmpy = int((monPerso.coor[0]) // hw), int((monPerso.coor[1]) // hh)
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN] == 1 and monPerso.state != "Inventory":
        monPerso.dir = 2
        tmpy += 1
        tmp = [ [(tmpx - 1) * hh, tmpx * hh - 1], [tmpx * hh, (tmpx + 1) * hh - 1], [(tmpx + 1) * hh, (tmpx + 2) * hh - 1] ]
        z = tmpy * hh
        if (map[tmpy][tmpx] == 0 or y[1] < z) \
            and (not (x[1] > tmp[0][0] and x[0] < tmp[0][1] and y[1] >= z and map[tmpy][tmpx - 1] > 0) \
            and not (x[1] > tmp[2][0] and x[0] < tmp[2][1] and y[1] >= z and map[tmpy][tmpx + 1] > 0)):
            monPerso.coor[1] += speed

    if key[pygame.K_UP] == 1 and monPerso.state != "Inventory":
        monPerso.dir = 0
        tmp = [ [(tmpx - 1) * hh, tmpx * hh - 1], [tmpx * hh, (tmpx + 1) * hh - 1], [(tmpx + 1) * hh, (tmpx + 2) * hh - 1] ]
        z = tmpy * hh
        if (map[tmpy - 1][tmpx] == 0 or y[0] > z) \
            and (not (x[1] > tmp[0][0] and x[0] < tmp[0][1] and y[0] <= z and map[tmpy - 1][tmpx - 1] > 0) \
            and not (x[1] > tmp[2][0] and x[0] < tmp[2][1] and y[0] <= z and map[tmpy - 1][tmpx + 1] > 0)):
            monPerso.coor[1] -= speed

    if key[pygame.K_RIGHT] == 1 and monPerso.state != "Inventory":
        monPerso.dir = 3
        tmp = [ [(tmpy - 1) * hh, tmpy * hh - 1], [tmpy * hh, (tmpy + 1) * hh - 1], [(tmpy + 1) * hh, (tmpy + 2) * hh - 1] ]
        z = (tmpx + 1) * hh
        if (map[tmpy][tmpx + 1] == 0 or x[1] < z) \
            and (not (y[1] > tmp[0][0] and y[0] < tmp[0][1] and x[1] >= z and map[tmpy - 1][tmpx + 1] > 0) \
            and not (y[1] > tmp[2][0] and y[0] < tmp[2][1] and x[1] >= z and map[tmpy + 1][tmpx + 1] > 0)):
            monPerso.coor[0] += speed

    if key[pygame.K_LEFT] == 1 and monPerso.state != "Inventory":
        monPerso.dir = 1
        tmp = [ [(tmpy - 1) * hh, tmpy * hh - 1], [tmpy * hh, (tmpy + 1) * hh - 1], [(tmpy + 1) * hh, (tmpy + 2) * hh - 1] ]
        z = tmpx * hh
        if (map[tmpy][tmpx - 1] == 0 or x[0] > z) \
            and (not (y[1] > tmp[0][0] and y[0] < tmp[0][1] and x[0] <= z and map[tmpy - 1][tmpx - 1] > 0) \
            and not (y[1] > tmp[2][0] and y[0] < tmp[2][1] and x[0] <= z and map[tmpy + 1][tmpx - 1] > 0)):
            monPerso.coor[0] -= speed

    if key[pygame.K_e] == 1 and iPressed == False:
        if monPerso.dir == 0: tmpy -= 1 # N
        if monPerso.dir == 2: tmpy += 1 # S
        if monPerso.dir == 1: tmpx -= 1 # E
        if monPerso.dir == 3: tmpx += 1 # O

        if map[tmpy][tmpx] == 2:
            monPerso.state = "Inventory"

    if key[pygame.K_i] == 1 and iPressed == False:
        iPressed = True
        if monPerso.state == "Inventory":
            monPerso.state = "AFK"
        else: monPerso.state = "Inventory"
    elif not key[pygame.K_i]: iPressed = False

    monPerso.update()
    return iPressed


pygame.init() # Program initiats
size = width, height = 1500, 700
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (10, 80)
screen = pygame.display.set_mode(size)
pygame.font.init()

black = 0, 0, 0
red = 255, 0, 0
blue = 0, 0, 255
white = 255, 255, 255

map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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


size_perso = w, h = 31, 48
x, y = 16, 526
it = 0
move = False
# Loading image
image = pygame.image.load(".\\Perso_test.png")
heroPic = pygame.Surface(size_perso)

background = pygame.Surface(size)
draw_map(background, map)

#pygame.mouse.set_visible(False)
monPerso = Perso()

test = Inventory()

secondPos = [int((monPerso.coor[0]) // (hw * 2)), int((monPerso.coor[1]) // (hh * 2))]
movement = time.time()
timerAnimation = time.time()
iPressed = False
state = "Moving"
while 1:
    screen.blit(background, (0, 0), (0, 0, width, height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT] and monPerso.state != "Inventory": monPerso.state = "Moving"
            if event.key == pygame.K_ESCAPE and monPerso.state == "Inventory": monPerso.state = "AFK"

    if time.time() - movement > 0.004:
        iPressed = detection(monPerso, map, iPressed)
        movement = time.time()

    #if monPerso.state == "Inventory":
    #    inventoryUpdate()
    if monPerso.state == "Moving":
        if (time.time() - timerAnimation) > 0.07:
            key = pygame.key.get_pressed()
            if (key[pygame.K_DOWN] or key[pygame.K_UP] or key[pygame.K_LEFT] or key[pygame.K_RIGHT]):
                timerAnimation, it = time.time(), it + 1
                if it > 8 : it = 0
            else: monPerso.state, it = "AFK", 0

    #if state != monPerso.state:
    #    state = monPerso.state
    #    print("state : {}".format(state))

    #pygame.draw.rect(screen, (0, 0, 240), monPerso.rect)
    x, y = 16 + (it * 64), 526 + (monPerso.dir * 64)
    heroPic.fill(black)
    heroPic.set_colorkey(black)
    heroPic.blit(image, (0, 0), (x, y, w, h))
    screen.blit(heroPic, (monPerso.rect[0], monPerso.rect[1] - (heroPic.get_size()[1] - monPerso.size[1])))
    pygame.transform.scale(screen, (width, height), screen)
    if monPerso.state == "Inventory": test.show(screen, size, ())
    pygame.display.flip()
