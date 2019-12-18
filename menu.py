import pygame

class Inventory:
    def show(self, screen, size, elements):
        back = pygame.Rect((size[0] // 10, size[1] // 10), (size[0] * 8 // 10, size[1] * 8 // 10))
        pygame.draw.rect(screen, pygame.Color(0, 0, 200, 50), back)
