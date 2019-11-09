import os
import sys
import time
import pygame

hw, hh = 50, 50

class Perso():
    def __init__(self):
        self.dir = 0
        self.size = [40, 40]
        self.coor = [120, 120] # life etc...
        self.rect = pygame.Rect(self.coor[0] - (self.size[0] / 2), self.coor[1] - (self.size[1] / 2), self.size[0], self.size[1])
    def update(self):
        self.rect = pygame.Rect(self.coor[0] - (self.size[0] / 2), self.coor[1] - (self.size[1] / 2), self.size[0], self.size[1])

def draw_map(screen, map):
    for idy, inty in enumerate(map):
        for idx, intx in enumerate(inty):
            if intx == 1:
                pygame.draw.rect(screen, (50, 50, 50), ((idx * hw), (idy * hh), hw, hh))
            elif intx == 2:
                pygame.draw.rect(screen, (50, 10, 10), ((idx * hw), (idy * hh), hw, hh))

def detection(monPerso, map): # key detection
    speed = 1
    x = [monPerso.coor[0] - (monPerso.size[0] / 2), monPerso.coor[0] + (monPerso.size[0] / 2)]
    y = [monPerso.coor[1] - (monPerso.size[1] / 2), monPerso.coor[1] + (monPerso.size[1] / 2)]

    if pygame.key.get_pressed()[pygame.K_DOWN] == 1:

        monPerso.dir = 'S'
        tmpx, tmpy = int((monPerso.coor[0]) // hw), int((monPerso.coor[1]) // hh) + 1
        tmp = [ [(tmpx - 1) * hh, tmpx * hh - 1], [tmpx * hh, (tmpx + 1) * hh - 1], [(tmpx + 1) * hh, (tmpx + 2) * hh - 1] ]
        z = tmpy * hh
        if (map[tmpy][tmpx] == 0 or y[1] < z) \
            and (not (x[1] > tmp[0][0] and x[0] < tmp[0][1] and y[1] >= z and map[tmpy][tmpx - 1] > 0) \
            and not (x[1] > tmp[2][0] and x[0] < tmp[2][1] and y[1] >= z and map[tmpy][tmpx + 1] > 0)):
            monPerso.coor[1] += speed

    if pygame.key.get_pressed()[pygame.K_UP] == 1:

        monPerso.dir = 'N'
        tmpx, tmpy = int((monPerso.coor[0]) // hw), int((monPerso.coor[1]) // hh)
        tmp = [ [(tmpx - 1) * hh, tmpx * hh - 1], [tmpx * hh, (tmpx + 1) * hh - 1], [(tmpx + 1) * hh, (tmpx + 2) * hh - 1] ]
        z = tmpy * hh
        if (map[tmpy - 1][tmpx] == 0 or y[0] > z) \
            and (not (x[1] > tmp[0][0] and x[0] < tmp[0][1] and y[0] <= z and map[tmpy - 1][tmpx - 1] > 0) \
            and not (x[1] > tmp[2][0] and x[0] < tmp[2][1] and y[0] <= z and map[tmpy - 1][tmpx + 1] > 0)):
            monPerso.coor[1] -= speed

    if pygame.key.get_pressed()[pygame.K_RIGHT] == 1:

        monPerso.dir = 'O'
        tmpx, tmpy = int((monPerso.coor[0]) // hw), int((monPerso.coor[1]) // hh)
        tmp = [ [(tmpy - 1) * hh, tmpy * hh - 1], [tmpy * hh, (tmpy + 1) * hh - 1], [(tmpy + 1) * hh, (tmpy + 2) * hh - 1] ]
        z = (tmpx + 1) * hh
        if (map[tmpy][tmpx + 1] == 0 or x[1] < z) \
            and (not (y[1] > tmp[0][0] and y[0] < tmp[0][1] and x[1] >= z and map[tmpy - 1][tmpx + 1] > 0) \
            and not (y[1] > tmp[2][0] and y[0] < tmp[2][1] and x[1] >= z and map[tmpy + 1][tmpx + 1] > 0)):
            monPerso.coor[0] += speed

    if pygame.key.get_pressed()[pygame.K_LEFT] == 1:

        monPerso.dir = 'E'
        tmpx, tmpy = int((monPerso.coor[0]) // hw), int((monPerso.coor[1]) // hh)
        tmp = [ [(tmpy - 1) * hh, tmpy * hh - 1], [tmpy * hh, (tmpy + 1) * hh - 1], [(tmpy + 1) * hh, (tmpy + 2) * hh - 1] ]
        z = tmpx * hh
        if (map[tmpy][tmpx - 1] == 0 or x[0] > z) \
            and (not (y[1] > tmp[0][0] and y[0] < tmp[0][1] and x[0] <= z and map[tmpy - 1][tmpx - 1] > 0) \
            and not (y[1] > tmp[2][0] and y[0] < tmp[2][1] and x[0] <= z and map[tmpy + 1][tmpx - 1] > 0)):
            monPerso.coor[0] -= speed

    if pygame.key.get_pressed()[pygame.K_e] == 1:
        tmpx, tmpy = int((monPerso.coor[0]) // hw), int((monPerso.coor[1]) // hh)
        if monPerso.dir == 'N': tmpy -= 1
        if monPerso.dir == 'S': tmpy += 1
        if monPerso.dir == 'E': tmpx -= 1
        if monPerso.dir == 'O': tmpx += 1

        if map[tmpy][tmpx] == 2:
            print("Interaction sur coffre")
            # test() modularité en python ...

    monPerso.update()


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
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1], # Map hard on the code !
    [1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

pygame.mouse.set_visible(False)
monPerso = Perso()

secondPos = [int((monPerso.coor[0]) // (hw * 2)), int((monPerso.coor[1]) // (hh * 2))]
temps = time.time()
while 1:
    screen.fill(black)
    draw_map(screen, map)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Detection to close the window
                sys.exit()

    if time.time() - temps > 0.003:
        detection(monPerso, map)
        temps = time.time()

    pygame.draw.rect(screen, (0, 0, 240), monPerso.rect)

    pygame.display.flip()
