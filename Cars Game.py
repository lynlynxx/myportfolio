import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("CARS")
clock = pygame.time.Clock()

# Load images
road = pygame.image.load('Road.png')
gutter = pygame.image.load('R gutter.png')
gutterflip = pygame.image.load('L gutter.png')
player = pygame.image.load('car player.png')
car1 = pygame.image.load('car1.png').convert_alpha()
car2 = pygame.image.load('car2.png').convert_alpha()
car3 = pygame.image.load('car3.png').convert_alpha()
gameoverimage = pygame.image.load('GameOver.png').convert_alpha()
lives_image = pygame.image.load('Poplife.png').convert_alpha()



car1_x = 250
car1_y = -car1.get_height()
car1_speed = 5


car2_x = 470
car2_y = -car2.get_height()
car2_speed = 5


car3_x = 250
car3_y = -car3.get_height()
car3_speed = 5


road_y = 0

car2_has_crossed = False

player_x = 250
player_y = 500
player_speed = 4

game_over = False
score = 0
start_time = pygame.time.get_ticks()
lives = 2 


last_collision_time = 0
collision_delay = 1000 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if lives > 0:
        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player_x -= player_speed
            if keys[pygame.K_RIGHT]:
                player_x += player_speed


            player_x = max(200, min(player_x, 500))
        
            road_y += 5
            if road_y > 0:
                road_y = -600

    
            car1_y += car1_speed
            if car1_y > 850:
                car1_x = 250
                car1_y = -car1.get_height()


            car2_y += car2_speed
            if car2_y > 600:
                car2_x = 470
                car2_y = -car2.get_height()

            if car2_y > 100:
                car2_has_crossed = True

            if car2_has_crossed:
                car3_y += car3_speed
                if car3_y > 900:
                    car3_x = 250
                    car3_y = -car3.get_height()

        
            player_rect = pygame.Rect(player_x, player_y, player.get_width(), player.get_height())
            car_rect1 = pygame.Rect(car1_x, car1_y, car1.get_width(), car1.get_height())
            car_rect2 = pygame.Rect(car2_x, car2_y, car2.get_width(), car2.get_height())
            car_rect3 = pygame.Rect(car3_x, car3_y, car3.get_width(), car3.get_height())

            if player_rect.colliderect(car_rect1) or player_rect.colliderect(car_rect2) or player_rect.colliderect(car_rect3):
                current_time = pygame.time.get_ticks()
                if current_time - last_collision_time > collision_delay:
                    lives -= 1
                    last_collision_time = current_time
                    if lives == 0:
                        game_over = True


            current_time = pygame.time.get_ticks()
            elapsed_time = (current_time - start_time) // 1000
            score = elapsed_time

        
            screen.fill((0, 0, 0))

            screen.blit(road, (200, road_y))
            screen.blit(road, (1 + 800, 0))
            screen.blit(gutter, (0, 0))
            screen.blit(gutterflip, (600, 0))

            screen.blit(player, (player_x, player_y))

            screen.blit(car1, (car1_x, car1_y))
            screen.blit(car2, (car2_x, car2_y)) 
            screen.blit(car3, (car3_x, car3_y))

    
            font = pygame.font.Font(None, 40)
            score_text = font.render(f"Score: {score}", True, (255, 0, 0))
            screen.blit(score_text, (10, 10))

    
            for i in range(lives):
                screen.blit(lives_image, (750 - i * 40, 10))
        

        else:
            screen.blit(gameoverimage, (0, 0))
            pygame.display.update()

    else:
        screen.blit(gameoverimage, (0, 0)) 
        
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()


    for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:   
                        game_over = False
                        road_y = 0
                        player_x = 250
                        player_y = 500
                        car1_x = 250
                        car1_y = -car1.get_height()
                        car2_x = 470
                        car2_y = -car2.get_height()
                        car2_has_crossed = False
                        car3_x = 250
                        car3_y = -car3.get_height()
                        score = 0
                        start_time = pygame.time.get_ticks()
                        lives = 3
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()





    pygame.display.update()
    clock.tick(60)


