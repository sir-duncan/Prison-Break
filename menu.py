import sys
import pygame

class Button():
    def __init__(self, elm):
        self.elm = elm
    def update(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h

def updatePnj(dumb):
    if dumb.dir == 2: dumb.coor[1] += 1
    elif dumb.dir == 0: dumb.coor[1] -= 1
    if dumb.coor[1] >= 300: dumb.dir = 0
    elif dumb.coor[1] <= 120: dumb.dir = 2
    dumb.update()

def animatePnj(dumb):
    dumb.it += 1
    if dumb.it > 8 : dumb.it = 1 # PNJ animation
    dumb.update()

def displayPerso(perso, screen, image, heroPic, size_perso, color):
    black = (0, 0, 0)
    x, y = 16 + (perso.it * 64), 526 + (perso.dir * 64)
    heroPic.fill(black)
    heroPic.set_colorkey(black)
    heroPic.blit(image, (0, 0), (x, y, size_perso[0], size_perso[1]))
    #pygame.draw.rect(screen, color, perso.rect)
    screen.blit(heroPic, (perso.rect[0], perso.rect[1] - (heroPic.get_size()[1] - perso.size[1])))
    return screen

def draw_map(screen, map, blockSize):
    ground = pygame.image.load(".\\Data\\Ground.png")
    hw, hh = blockSize[0], blockSize[1]
    for idy, inty in enumerate(map):
        for idx, intx in enumerate(inty):
            if intx == 1:
                pygame.draw.rect(screen, (50, 50, 50), ((idx * hw), (idy * hh), hw, hh))
            elif intx == 2:
                pygame.draw.rect(screen, (50, 10, 10), ((idx * hw), (idy * hh), hw, hh))
            elif intx == 0:
                screen.blit(ground, (idx * hw, idy * hh), (0, 0, hw, hh))
                #pygame.draw.rect(screen, (10, 50, 10), ((idx * hw), (idy * hh), hw, hh))

def mainMenu(screen, size):
    pygame.mouse.set_visible(True)
    white = (240, 240, 240)
    wallpaper = pygame.image.load(".\\Data\\wallpaper.jpg")
    titleFont = pygame.font.Font('.\\Data\\font.ttf', 180)
    buttonFont = pygame.font.Font('.\\Data\\font.ttf', 100)
    title = Button(titleFont.render("Prison Break", False, (60, 60, 200)))
    newGame = Button(buttonFont.render("Nouvelle Partie", False, white))
    quit = Button(buttonFont.render("Quitter", False, white))
    boxNewGame = Button(pygame.Surface((size[0] * 6 // 10, size[1] * 15 // 100), pygame.SRCALPHA))
    boxNewGame.update((size[0] / 2) - (boxNewGame.elm.get_width() / 2), size[1] * 45 // 100, boxNewGame.elm.get_width(), boxNewGame.elm.get_height())
    boxQuit = Button(pygame.Surface((size[0] * 6 // 10, size[1] * 15 // 100), pygame.SRCALPHA))
    boxQuit.update((size[0] / 2) - (boxQuit.elm.get_width() / 2), size[1] * 65 // 100, boxQuit.elm.get_width(), boxQuit.elm.get_height())
    boxNewGame.elm.fill((5, 5, 5, 190))
    boxQuit.elm.fill((5, 5, 5, 190))
    title.update((size[0] / 2) - (title.elm.get_width() / 2), size[1] * 5 // 100, title.elm.get_width(), title.elm.get_height())
    newGame.update((size[0] / 2) - (newGame.elm.get_width() / 2), boxNewGame.y + (boxNewGame.h // 2) - (newGame.elm.get_height() // 2), newGame.elm.get_width(), newGame.elm.get_height())
    quit.update((size[0] / 2) - (quit.elm.get_width() / 2), boxQuit.y + (boxQuit.h // 2) - (quit.elm.get_height() // 2), quit.elm.get_width(), quit.elm.get_height())
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_pos = (int(pygame.mouse.get_pos()[0]), int(pygame.mouse.get_pos()[1]))
                if m_pos[0] > boxNewGame.x and m_pos[0] < boxNewGame.x + boxNewGame.w and m_pos[1] > boxNewGame.y and m_pos[1] < boxNewGame.y + boxNewGame.h:
                    pygame.mouse.set_visible(False)
                    return
                elif m_pos[0] > boxQuit.x and m_pos[0] < boxQuit.x + boxQuit.w and m_pos[1] > boxQuit.y and m_pos[1] < boxQuit.y + boxQuit.h: sys.exit()

        screen.blit(wallpaper, (0, 0))
        screen.blit(title.elm, (title.x, title.y))
        screen.blit(boxNewGame.elm, (boxNewGame.x, boxNewGame.y))
        screen.blit(boxQuit.elm, (boxQuit.x, boxQuit.y))
        pygame.draw.rect(screen, white, pygame.Rect((boxNewGame.x, boxNewGame.y), (boxNewGame.w, boxNewGame.h)), 2)
        pygame.draw.rect(screen, white, pygame.Rect((boxQuit.x, boxQuit.y), (boxQuit.w, boxQuit.h)), 2)
        screen.blit(newGame.elm, (newGame.x, newGame.y))
        screen.blit(quit.elm, (quit.x, quit.y))
        pygame.display.update()

def invertoryMenu(screen, size, monPerso):
    taille, elem = 60, list()
    white, dark = (250, 250, 250), (80, 80, 80)
    titleFont = pygame.font.SysFont('.\\Data\\font.ttf', 50)
    statusFont, status = pygame.font.SysFont('Comic Sans MS', 30), ""
    title = (statusFont.render("Objet", False, dark), statusFont.render("Acces Rapide", False, dark), statusFont.render("Description", False, dark))
    old = screen.copy()
    back = Button(pygame.Surface((size[0] * 7 // 10, size[1] * 7 // 10), pygame.SRCALPHA))
    back.update(size[0] * 5 // 10 - (size[0] * 7 // 20), size[1] * 5 // 10 - (size[1] * 7 // 20), size[0] * 7 // 10, size[1] * 7 // 10)
    mainTitle = Button(titleFont.render("Inventaire", False, white))
    mainTitle.update(size[0] * 5 // 10 - (mainTitle.elm.get_width() / 2), back.y + (back.h * 7 // 100), mainTitle.elm.get_width(), mainTitle.elm.get_height())
    for i in range(20):
        elem.append(pygame.Rect((i % 5) * (back.w * 2 // 100) + ((i % 5) * taille) + (back.x + (back.w * 6 // 100)), (i // 5) * (back.h * 3 // 100) + ((i // 5) * taille) + (back.y + (back.h * 40 // 100)), taille, taille))
    hand = pygame.Rect(size[0] / 2, size[1] / 2, taille, taille)
    back.elm.fill((5, 5, 5, 190))
    pygame.mouse.set_visible(True)
    while True:
        for event in pygame.event.get():
            #if event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_i:
                    monPerso.state, iPressed = "AFK", True
                    pygame.mouse.set_visible(False)
                    return True
        m_pos = pygame.mouse.get_pos()
        for cell in elem:
            if m_pos[0] > cell.x and m_pos[0] < cell.x + cell.w and m_pos[1] > cell.y and m_pos[1] < cell.y + cell.h:
                status = statusFont.render("Cellule Vide", False, white)
                break
        else: status = statusFont.render("Seléctionnez un objet", False, white)
        screen.blit(old, (0, 0))
        screen.blit(back.elm, (back.x, back.y)) # put in the center
        screen.blit(mainTitle.elm, (mainTitle.x, mainTitle.y))
        screen.blit(title[0], (back.x + back.w * 19 // 100, back.y + back.h * 26 // 100))
        screen.blit(title[1], (back.x + back.w * 46 // 100, back.y + back.h * 26 // 100))
        screen.blit(title[2], (back.x + back.w * 70 // 100, back.y + back.h * 26 // 100))
        screen.blit(status, (back.x + (back.w * 70 // 100), size[1] * 5 // 10))
        pygame.draw.rect(screen, (0, 0, 0), hand)
        for rect in elem: pygame.draw.rect(screen, (0, 0, 0), rect)
        pygame.draw.rect(screen, dark, pygame.Rect(back.x + back.w * 43 // 100, back.y + back.h * 35 // 100, 2, back.h * 55 // 100))
        pygame.draw.rect(screen, dark, pygame.Rect(back.x + back.w * 62 // 100, back.y + back.h * 35 // 100, 2, back.h * 55 // 100))
        pygame.display.flip()

def detection(monPerso, map, blockSize, movingKey, iPressed): # key detection
    speed = 1
    #movingKey = [pygame.K_s, pygame.K_w, pygame.K_d, pygame.K_a]#[pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT]
    hw, hh = blockSize[0], blockSize[1]
    x = [monPerso.coor[0] - (monPerso.size[0] / 2), monPerso.coor[0] + (monPerso.size[0] / 2)]
    y = [monPerso.coor[1] - (monPerso.size[1] / 2), monPerso.coor[1] + (monPerso.size[1] / 2)]
    tmpx, tmpy = int((monPerso.coor[0]) // hw), int((monPerso.coor[1]) // hh)
    key = pygame.key.get_pressed()
    if key[movingKey[0]] and monPerso.state != "Inventory":
        monPerso.dir = 2
        tmpy += 1
        tmp = [ [(tmpx - 1) * hh, tmpx * hh - 1], [tmpx * hh, (tmpx + 1) * hh - 1], [(tmpx + 1) * hh, (tmpx + 2) * hh - 1] ]
        z = tmpy * hh
        if (map[tmpy][tmpx] == 0 or y[1] < z) \
            and (not (x[1] > tmp[0][0] and x[0] < tmp[0][1] and y[1] >= z and map[tmpy][tmpx - 1] > 0) \
            and not (x[1] > tmp[2][0] and x[0] < tmp[2][1] and y[1] >= z and map[tmpy][tmpx + 1] > 0)):
            monPerso.coor[1] += speed

    if key[movingKey[1]] and monPerso.state != "Inventory":
        monPerso.dir = 0
        tmp = [ [(tmpx - 1) * hh, tmpx * hh - 1], [tmpx * hh, (tmpx + 1) * hh - 1], [(tmpx + 1) * hh, (tmpx + 2) * hh - 1] ]
        z = tmpy * hh
        if (map[tmpy - 1][tmpx] == 0 or y[0] > z) \
            and (not (x[1] > tmp[0][0] and x[0] < tmp[0][1] and y[0] <= z and map[tmpy - 1][tmpx - 1] > 0) \
            and not (x[1] > tmp[2][0] and x[0] < tmp[2][1] and y[0] <= z and map[tmpy - 1][tmpx + 1] > 0)):
            monPerso.coor[1] -= speed

    if key[movingKey[2]] and monPerso.state != "Inventory":
        monPerso.dir = 3
        tmp = [ [(tmpy - 1) * hh, tmpy * hh - 1], [tmpy * hh, (tmpy + 1) * hh - 1], [(tmpy + 1) * hh, (tmpy + 2) * hh - 1] ]
        z = (tmpx + 1) * hh
        if (map[tmpy][tmpx + 1] == 0 or x[1] < z) \
            and (not (y[1] > tmp[0][0] and y[0] < tmp[0][1] and x[1] >= z and map[tmpy - 1][tmpx + 1] > 0) \
            and not (y[1] > tmp[2][0] and y[0] < tmp[2][1] and x[1] >= z and map[tmpy + 1][tmpx + 1] > 0)):
            monPerso.coor[0] += speed

    if key[movingKey[3]] and monPerso.state != "Inventory":
        monPerso.dir = 1
        tmp = [ [(tmpy - 1) * hh, tmpy * hh - 1], [tmpy * hh, (tmpy + 1) * hh - 1], [(tmpy + 1) * hh, (tmpy + 2) * hh - 1] ]
        z = tmpx * hh
        if (map[tmpy][tmpx - 1] == 0 or x[0] > z) \
            and (not (y[1] > tmp[0][0] and y[0] < tmp[0][1] and x[0] <= z and map[tmpy - 1][tmpx - 1] > 0) \
            and not (y[1] > tmp[2][0] and y[0] < tmp[2][1] and x[0] <= z and map[tmpy + 1][tmpx - 1] > 0)):
            monPerso.coor[0] -= speed

    if key[pygame.K_e] and iPressed == False:
        if monPerso.dir == 0: tmpy -= 1 # N
        if monPerso.dir == 2: tmpy += 1 # S
        if monPerso.dir == 1: tmpx -= 1 # E
        if monPerso.dir == 3: tmpx += 1 # O
        if map[tmpy][tmpx] == 2:
            monPerso.state = "Inventory"

    if key[pygame.K_i]: monPerso.state = "Inventory"

    if key[pygame.K_ESCAPE] and iPressed == False:
        #sys.exit()
        iPressed = True
        monPerso.state = "Pause"
    elif not key[pygame.K_ESCAPE]: iPressed = False

    monPerso.update()
    return iPressed

def pauseMenu(screen, size, monPerso):
    global iPressed
    titleFont = pygame.font.SysFont('.\\Data\\font.ttf', 60)
    buttonFont = pygame.font.SysFont('.\\Data\\font.ttf', 48)
    white = (250, 250, 250)
    back = pygame.Surface((size[0] * 5 // 10, size[1] * 4 // 10), pygame.SRCALPHA)
    old = screen.copy()
    x, y = size[0] * 5 // 10 - (size[0] * 4 // 20), size[1] * 5 // 10 - (size[1] * 4 // 20)
    title = titleFont.render("Pause", False, white)
    resume = buttonFont.render("Reprendre", False, white)
    quit = buttonFont.render("Quitter", False, white)
    back.fill((5, 5, 5, 190))
    pygame.mouse.set_visible(True)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_pos = (int(pygame.mouse.get_pos()[0]), int(pygame.mouse.get_pos()[1]))
                if m_pos[0] > (x + (back.get_width() / 2) - (back.get_width() * 6 // 20)) and m_pos[0] < (x + (back.get_width() / 2) + (back.get_width() * 6 // 20)):
                    if m_pos[1] > y + (back.get_height() * 45 // 100) and m_pos[1] < y + (back.get_height() * 65 // 100):
                        monPerso.state = "AFK"
                        pygame.mouse.set_visible(False)
                        return
                    elif m_pos[1] > y + (back.get_height() * 70 // 100) and m_pos[1] < y + (back.get_height() * 90 // 100): sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    monPerso.state, iPressed = "AFK", True
                    pygame.mouse.set_visible(False)
                    return
        screen.blit(old, (0, 0))
        screen.blit(back, [x, y])
        pygame.draw.rect(screen, white, pygame.Rect((x + (back.get_width() / 2) - (back.get_width() * 6 // 20), y + (back.get_height() * 45 // 100)), (back.get_width() * 6 // 10, back.get_height() * 2 // 10)), 1)
        pygame.draw.rect(screen, white, pygame.Rect((x + (back.get_width() / 2) - (back.get_width() * 6 // 20), y + (back.get_height() * 7 // 10)), (back.get_width() * 6 // 10, back.get_height() * 2 // 10)), 1)
        screen.blit(title, (x + (back.get_width() / 2) - (title.get_width() / 2), y + (back.get_height() // 10)))
        screen.blit(resume, (x + (back.get_width() / 2) - (resume.get_width() / 2), y + (back.get_height() * 55 // 100) - (resume.get_height() * 5 // 10)))
        screen.blit(quit, (x + (back.get_width() / 2) - (quit.get_width() / 2), y + (back.get_height() * 80 // 100) - (quit.get_height() * 5 // 10)))
        pygame.display.flip()
