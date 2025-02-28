import pygame
import math
import random

pygame.init()
Timer = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 300

# Game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FINALS")
icon = pygame.image.load('zombieicon.png').convert_alpha()
pygame.display.set_icon(icon)

# Load images
bg = pygame.image.load("bg zombie.jpg")
bg_width = bg.get_width()
player_right = pygame.image.load('player left w.png').convert_alpha()
player_left = pygame.image.load('player right w.png').convert_alpha()

player = player_left  # Set the default player image
player_rect = player.get_rect()
player_rect.center = (100, 250)  # Start position of the player



# Enemy attributes
enemy_image = pygame.image.load('WalkL.png').convert_alpha()
enemy_image2 = pygame.image.load('Walk.png').convert_alpha()
enemy_width = enemy_image.get_width()
enemy_height = enemy_image.get_height()


class Enemy:
    def __init__(self, x, y, speed):
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed
        self.attacking = False  # Flag to indicate if the enemy is attacking
        self.attack_range = 100 

    def update(self):
        self.rect.x -= self.speed

        # Reset enemy position if it goes off-screen
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
            self.rect.y = random.randint(20, SCREEN_HEIGHT - enemy_height - 15)



# Game variables
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
player_speed = 2

# Create an enemy object
enemy = Enemy(SCREEN_WIDTH, random.randint(20, SCREEN_HEIGHT - enemy_height - 10), 4)



# Function to check collision between player and enemy
def check_collision(player_rect, enemy_rect):
    return player_rect.colliderect(enemy_rect)


# Main game loop
run = True
while run:
    Timer.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    # Move player based on key presses
    if keys[pygame.K_LEFT]:
        player = player_left
        if player_rect.left > 0:  
            player_rect.x -= player_speed
    elif keys[pygame.K_RIGHT]:
        player = player_right
        if player_rect.right < SCREEN_WIDTH:  
            player_rect.x += player_speed              

    


# Scroll background
    scroll -= 2

    # Reset scroll
    if abs(scroll) > bg_width:
        scroll = 0


    # Update enemy position
    enemy.update()

# Check collision between player and enemy
    collision = check_collision(player_rect, enemy.rect)


    # Draw background and player
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
        screen.blit(player, player_rect)
        screen.blit(enemy.image, enemy.rect)
    
    if collision:
        # Reset player and enemy positions
        player_rect.center = (100, 250)
        enemy.rect.topleft = (SCREEN_WIDTH, random.randint(50, SCREEN_HEIGHT - enemy_height - 15))
    
    
 
    pygame.display.update()

pygame.quit()
