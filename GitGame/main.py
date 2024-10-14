import pygame
import ctypes

pygame.init()

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ширина = user32.GetSystemMetrics(0)
высота = user32.GetSystemMetrics(1)
screen = pygame.display.set_mode((ширина, высота ))
pygame.display.set_caption("GitGame")
icon = pygame.image.load("textures/icon.png")
pygame.display.set_icon(icon)
pygame.display.toggle_fullscreen()

run = True
while run:

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()