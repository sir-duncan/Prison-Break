import os
import sys
import time
import pygame
import ctypes
from menu import *

blockSize = (48, 48)

class Perso():
    def __init__(self, pos, name):
        self.it = 0
        self.dir = 2 # N:0  E:1  S:2  O:3
        self.size = [30, 40]
        self.coor = [pos[0], pos[1]] # life etc...
        self.name = name
        self.state = "AFK"
        self.pocket = None
        self.rect = pygame.Rect(self.coor[0] - (self.size[0] / 2), self.coor[1] - (self.size[1] / 2), self.size[0], self.size[1])
    def update(self):
        self.rect = pygame.Rect(self.coor[0] - (self.size[0] / 2), self.coor[1] - (self.size[1] / 2), self.size[0], self.size[1])

def objectDetection(screen, monPerso, bjets):
    distance, taille = 35, 25
    pseudo = None
    if monPerso.dir == 0:
        if monPerso.coor[0] - (taille // 2) < objets.elm.x + objets.elm.width and monPerso.coor[0] + (taille // 2) > objets.elm.x  and monPerso.coor[1] - distance - (taille // 2) < objets.elm.y + objets.elm.height and monPerso.coor[1] - distance + (taille // 2) > objets.elm.y:
            pseudo = objets.name
            #pygame.draw.rect(screen, color, pygame.Rect((monPerso.coor[0] - (taille // 2), monPerso.coor[1] - distance - (taille // 2)), (taille, taille)))
    elif monPerso.dir == 1:
        if monPerso.coor[0] - distance - (taille // 2) < objets.elm.x + objets.elm.width and monPerso.coor[0] - distance + (taille // 2) > objets.elm.x and monPerso.coor[1] - (taille // 2) < objets.elm.y + objets.elm.height and monPerso.coor[1] + (taille // 2) > objets.elm.y:
            pseudo = objets.name
            #pygame.draw.rect(screen, color, pygame.Rect((monPerso.coor[0] - distance - (taille // 2), monPerso.coor[1] - (taille // 2)), (taille, taille)))
    elif monPerso.dir == 2:
        if monPerso.coor[0] - (taille // 2) < objets.elm.x + objets.elm.width and monPerso.coor[0] + (taille // 2) > objets.elm.x and monPerso.coor[1] + distance - (taille // 2) < objets.elm.y + objets.elm.height and monPerso.coor[1] + distance + (taille // 2) > objets.elm.y:
            pseudo = objets.name
            #pygame.draw.rect(screen, (200, 0, 0), pygame.Rect((monPerso.coor[0] - (taille // 2), monPerso.coor[1] + distance - (taille // 2)), (taille, taille)))
    elif monPerso.dir == 3:
        if monPerso.coor[0] + distance - (taille // 2) < objets.elm.x + objets.elm.width and monPerso.coor[0] + distance + (taille // 2) > objets.elm.x and monPerso.coor[1] - (taille // 2) < objets.elm.y + objets.elm.height and monPerso.coor[1] + (taille // 2) > objets.elm.y:
            pseudo = objets.name
            #pygame.draw.rect(screen, (200, 0, 0), pygame.Rect((monPerso.coor[0] + distance - (taille // 2), monPerso.coor[1] - (taille // 2)), (taille, taille)))
    if pseudo is not None:
        if pygame.key.get_pressed()[pygame.K_e]:
            monPerso.pocket = [objets]
            objets.update(False, (0, 0))

pygame.init() # Program initiats
infoObject = pygame.display.Info()
ctypes.windll.user32.SetProcessDPIAware()
true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
print(true_res)#infoObject.current_w)
screen = pygame.display.set_mode(true_res, pygame.FULLSCREEN)
#screen = pygame.display.set_mode((0, 0))
size = width, height = screen.get_width(), screen.get_height()#1920, 1080#1500, 700
print("size =", size)
pygame.font.init()
pygame.mouse.set_visible(False)

black = 0, 0, 0
red = 255, 0, 0
blue = 0, 0, 255
white = 255, 255, 255

map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

pygame.display.set_caption("Prison Break")

movingKey = [pygame.K_s, pygame.K_w, pygame.K_d, pygame.K_a]
size_perso = w, h = 31, 48
x, y = 16, 526
move = False


monPerso = Perso((120, 120), "Tim")
pnj = (Perso((500, 120), "John"), Perso((700, 120), "Jerome"))
pnj[1].state = "Moving"
iPressed = False
objets = Object("Objet Mystère", "Objet à donner à John", (400, 300))

# Loading images
images = {monPerso.name : pygame.image.load(".\\Data\\Tim.png")}
for dumb in pnj: images[dumb.name] = pygame.image.load(".\\Data\\" + dumb.name + ".png")

heroPic = pygame.Surface(size_perso)
color = (0, 0, 240)
background = pygame.Surface(size)
draw_map(background, map, blockSize)

mainMenu(screen, size)

#Loading Font
timer = time.time()
font = pygame.font.SysFont('Comic Sans MS', 20)
message, itMessage = "Salut, moi je m'appelle John, et je suis ici depuis longtemps ! Trouve l'objet mystère et je te donnerai un indice pour t'échapper", 0
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
        if monPerso.state is not "Speaking":
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
    #if monPerso.state is not "Speaking":
    speak = playerDetection(screen, monPerso, pnj)
    objectDetection(screen, monPerso, objets)
    if objets.display: pygame.draw.rect(screen, (240, 240, 240), objets.elm)
    for dumb in pnj:
        if monPerso.rect.x < dumb.rect.x + dumb.rect.width and monPerso.rect.x + monPerso.rect.width > dumb.rect.x and monPerso.rect.y < dumb.rect.y + dumb.rect.height and monPerso.rect.y + monPerso.rect.height > dumb.rect.y:
            #display lower y first -> collision with dumb
            for dumb2 in pnj:
                if dumb2 != dumb: screen = displayPerso(dumb2, screen, images, heroPic, size_perso, color)
                if dumb2 == dumb:
                    if dumb.rect.y > monPerso.rect.y:
                        screen = displayPerso(monPerso, screen, images, heroPic, size_perso, color)
                        screen = displayPerso(dumb, screen, images, heroPic, size_perso, color)
                    else:
                        screen = displayPerso(dumb, screen, images, heroPic, size_perso, color)
                        screen = displayPerso(monPerso, screen, images, heroPic, size_perso, color)
            break
    else: #whatever
        color = (0, 0, 240)
        screen = displayPerso(monPerso, screen, images, heroPic, size_perso, color)
        for dumb in pnj: displayPerso(dumb, screen, images, heroPic, size_perso, color)
    if monPerso.state is "Speaking":
        pygame.draw.rect(screen, white, pygame.Rect((size[0] // 10, size[1] * 92 // 100), (size[0] * 8 // 10, size[1] * 4 // 100))) #background
        paint = font.render(message[:itMessage], False, (15, 15, 15))
        if itMessage < len(message) and time.time() - timer > 0.03: itMessage, timer = itMessage + 1, time.time()
        screen.blit(paint, ((size[0] // 10) + 20, (size[1] * 92 // 100) + (size[1] * 4 // 200) - (paint.get_height() // 2)))
        if pygame.mouse.get_pressed()[0]:
            monPerso.state, itMessage = "AFK", 0
    #pygame.transform.scale(screen, (width, height), screen)
    if monPerso.state == "Inventory": iPressed = invertoryMenu(screen, size, monPerso)
    if monPerso.state == "Pause": pauseMenu(screen, size, monPerso)
    pygame.display.flip()
