import pygame
import sys

class Button():
    def __init__(self, elm):
        self.elm = elm
    def update(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h

def draw_map(screen, map, blockSize):
    ground = pygame.image.load(".\\Ground.png")
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

def invertoryMenu(screen, size, monPerso):
    taille, elem = 60, list()
    white, dark = (250, 250, 250), (60, 60, 60)
    titleFont = pygame.font.SysFont('Comic Sans MS', 50)
    statusFont, status = pygame.font.SysFont('Comic Sans MS', 30), ""
    title = (statusFont.render("Objet", False, dark), statusFont.render("Acces Rapide", False, dark), statusFont.render("Description", False, dark))
    old = screen.copy()
    back = Button(pygame.Surface((size[0] * 7 // 10, size[1] * 7 // 10), pygame.SRCALPHA))
    back.update(size[0] * 5 // 10 - (size[0] * 7 // 20), size[1] * 5 // 10 - (size[1] * 7 // 20), size[0] * 7 // 10, size[1] * 7 // 10)
    mainTitle = Button(titleFont.render("INVENTAIRE", False, white))
    mainTitle.update(size[0] * 5 // 10 - (mainTitle.elm.get_width() / 2), back.y + (back.h * 7 // 100), mainTitle.elm.get_width(), mainTitle.elm.get_height())
    for i in range(20):
        elem.append(pygame.Rect((i % 5) * (back.w * 2 // 100) + ((i % 5) * taille) + (back.x + (back.w * 6 // 100)), (i // 5) * (back.h * 3 // 100) + ((i // 5) * taille) + (back.y + (back.h * 40 // 100)), taille, taille))
    hand = pygame.Rect(size[0] / 2, size[1] / 2, taille, taille)
    back.elm.fill((0, 0, 0, 190))
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

def pauseMenu(screen, size, monPerso):
    global iPressed
    titleFont = pygame.font.SysFont('Comic Sans MS', 50)
    buttonFont = pygame.font.SysFont('Comic Sans MS', 40)
    white = (250, 250, 250)
    back = pygame.Surface((size[0] * 5 // 10, size[1] * 4 // 10), pygame.SRCALPHA)
    old = screen.copy()
    x, y = size[0] * 5 // 10 - (size[0] * 4 // 20), size[1] * 5 // 10 - (size[1] * 4 // 20)
    title = titleFont.render("PAUSE", False, white)
    resume = buttonFont.render("Reprendre", False, white)
    quit = buttonFont.render("Quitter", False, white)
    back.fill((0, 0, 0, 190))
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
