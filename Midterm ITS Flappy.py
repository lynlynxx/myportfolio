import pygame
import random
from sys import exit

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("FLAPPY")
screen = pygame.display.set_mode((288,512))
test_font  = pygame.font.Font(None, 50)

# background and ground
game_active = True
bg = pygame.image.load('flappy day bg.png').convert()
player_gravity = 0

groundSurf = pygame.image.load('ground flappy.png').convert()
ground_rect = groundSurf.get_rect(bottomleft=(0,540))
pipePos_y= 630
pipePos_x= 420

# Bird player
bird_fly1 = pygame.image.load('yellowbird-upflap.png').convert_alpha()
bird_fly2 = pygame.image.load('yellowbird-midflap.png').convert_alpha()
bird_fly3 = pygame.image.load('yellowbird-downflap.png').convert_alpha()

bird_fly = [bird_fly1,bird_fly2,bird_fly3]
bird_index = 0
bird_surf = bird_fly[bird_index]
bird_rect = bird_surf.get_rect(bottomleft=(100,200))


# Pipe Flapppy
pipeSurf = pygame.image.load('pipe red.png').convert()
pipe_rect = pipeSurf.get_rect(bottomleft=(pipePos_x,pipePos_y))

pipeSurf2 = pygame.image.load('pipe red rotate.png').convert()
pipe_rect2 = pipeSurf.get_rect(bottomleft=(pipePos_x,pipePos_y-480))
bird_rotation = 20


pipeSurf3 = pygame.image.load('pipe small red.png').convert()
pipe_rect3 = pipeSurf.get_rect(bottomleft=(700,2000))

player_gravity = 1


#Start Game display message
start_image = pygame.image.load('Get Ready Start.png').convert_alpha()
start_rect = start_image.get_rect(topleft =(50,100))

 
 

#Score
def display_score(score):
    
    score_surf = test_font.render(f'{score}' ,False,(232,235,230))
    score_rect = score_surf.get_rect(center = (150,30))
    screen.blit(score_surf,score_rect)


#Bird movement
def player_anim():
    
    global bird_surf, bird_index, bird_rotation

    bird_index += 0.1
    if bird_index >= len(bird_fly):
        bird_index = 0
    bird_surf = bird_fly[int(bird_index)]

    if player_gravity > 1:
        bird_rotation -=3 
        if bird_rotation <= -60: 
            bird_rotation = -60  
    else:

        bird_rotation = 30 
        

    
score=0  

# Load the sound effects
wings_sound = pygame.mixer.Sound('wings.wav')
hit_sound = pygame.mixer.Sound('hit.wav')
point_sound = pygame.mixer.Sound('point.wav')



while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_gravity = -9 

                    #looping sound wings when the space bar hit
                    wings_sound.play()   

        else:

            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active=True
                    
    if game_active:
            

        screen.blit(bg,(0,1))  

        pipe_rect.x -= 3
        pipe_rect2.x -= 3
        
        if pipe_rect.right < 1:
            pipe_rect.left = 299
            pipe_rect2.left = 299
            pipe_rect.bottom = random.randint(560, 750)
            pipe_rect2.bottom = pipe_rect.bottom -480
           
             
        print(score)
             
        screen.blit(pipeSurf,pipe_rect)
        screen.blit(pipeSurf2,pipe_rect2)

        ground_rect.x -= 1
        if ground_rect.right < 299 :
            ground_rect.left = 1

        player_gravity+= .5
        bird_rect.y +=player_gravity
        
        screen.blit(groundSurf,ground_rect)

        display_score(score)
        if pipe_rect.left==bird_rect.right:
            score +=1
            #when flappy pass through with pipe 
            point_sound.play() 

        
        if bird_rect.bottom >= ground_rect.top: bird_rect.bottom = ground_rect.top
        player_anim()
        rotated_bird_surf = pygame.transform.rotozoom(bird_surf, bird_rotation, 1)
        rotated_bird_rect = rotated_bird_surf.get_rect(center=bird_rect.center)

        screen.blit(rotated_bird_surf, rotated_bird_rect)



        #collision
        if bird_rect.colliderect(pipe_rect) or bird_rect.colliderect(pipe_rect2):
            
            game_active = False

            pipe_rect.left = 500
            pipe_rect2.left = 500
            pipe_rect3.left = 300
            bird_rect.bottom = 300
            screen.blit(start_image, start_rect)
            player_gravity=-9
            # When flappy die 
            hit_sound.play() 

            score = 0

    pygame.display.update()
    clock.tick(60)
    