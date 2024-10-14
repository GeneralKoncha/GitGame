import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("GitGame")
#icon = pygame.image.load("")
#pygame.display.set_icon(icon)


run = True
while run:

    screen.fill((197, 252, 252))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()