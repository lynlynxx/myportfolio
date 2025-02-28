import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((470,553))
pygame.display.set_caption("Jerlyn Game")
clock = pygame.time.Clock()
testfonts = pygame.font.Font(None, 30)


bg = pygame.image.load('Pacpac.jpg')
playerImg = pygame.image.load('player.png').convert_alpha()
playerImg_rect = playerImg.get_rect(topleft = (45,68))


enemy1 = pygame.image.load('enemy1.jpg')
enemy2 = pygame.image.load('enemy2.png').convert_alpha()
enemy3 = pygame.image.load('enemy3.jpg')

texttSurface = testfonts.render('PACMAN',False,'purple')

running = True

while running:

    screen.fill(('purple')) 


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(bg,(1,0))
    screen.blit(playerImg, playerImg_rect)
    screen.blit(enemy1,(200,259))
    screen.blit(enemy2,(230,259))
    screen.blit(enemy3,(258,259))
    screen.blit(texttSurface,(198,527))


#pacman move
    for event in pygame.event.get():
        run = False

    keys = pygame.key.get_pressed()
   
    if keys[pygame.K_LEFT]:
       playerImg_rect.x -= 2
    if keys[pygame.K_RIGHT]:
       playerImg_rect.x += 1
    if keys[pygame.K_UP]:
       playerImg_rect.y -= 1
    if keys[pygame.K_DOWN]:            
       playerImg_rect.y += 1

#enemy move   
# Randomly choose a direction for the ghost
    direction = randomn .choice(["up", "down", "left", "right"])

# Update ghost's position based on the chosen direction
    if direction == "up":
        enemy1_y -= enemy1_Speed
    if direction == "down":
        enemy1_y += enemy1_speed
    if direction == "left":
        enemy2_x -= enemy2_speed
    if direction == "right":
        enemy2_x += enemy2_speed






pygame.display.update()
clock.tick(60)
