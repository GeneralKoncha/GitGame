import pygame

pygame.init()

bottom_panel = 240

screen = pygame.display.set_mode((1280, 720 + bottom_panel))
pygame.display.set_caption("GitGame")
icon = pygame.image.load("textures/icon.png")
pygame.display.set_icon(icon)

textm = ('пуки каки какащульки, пуки... д|н')

mainfont = pygame.font.Font('fonts/determinationmonorusbylyajk.otf', 30)
text_surface = mainfont.render(textm, False, (255, 255, 255))

textRect = text_surface.get_rect()
textRect.center = (270, 740)

bg_img = pygame.image.load('textures/bg.jpg')
def draw_bg():
    screen.blit(bg_img, (0,0))
def draw_text():
    screen.fill((0, 0, 0))
    screen.blit (text_surface, textRect)


run = True
while run:

    draw_text()
    draw_bg()


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()