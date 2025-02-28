import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

screen_width = 1200
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('endless scroll')

#load image
bg = pygame.image.load('Forest.jpg')
bg_width = bg.get_width()

tiles = (screen_width / bg_width)
print(tiles)

#game loop
run = True
while run:

    clock.tick(FPS)

    #draw scrolling bg
    screen.blit(bg, (0, 0))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.display.update()

pygame.quit()