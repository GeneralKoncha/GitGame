import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("GitGame")
icon = pygame.image.load("textures/icon.png")
pygame.display.set_icon(icon)


run = True
while run:

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()