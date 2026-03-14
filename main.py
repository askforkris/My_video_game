import pygame
import random
import game_economy  # Ensure this file is in the same folder

# Setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()

# Game Objects
player_rect = pygame.Rect(400, 300, 50, 50)
treasure_rect = pygame.Rect(200, 200, 30, 30)
player_balance = 500

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_rect.x -= 5
    if keys[pygame.K_RIGHT]: player_rect.x += 5
    if keys[pygame.K_UP]: player_rect.y -= 5
    if keys[pygame.K_DOWN]: player_rect.y += 5

    # Collision (Economic Trigger)
    if player_rect.colliderect(treasure_rect):
        # Trigger the math!
        treasure_val = 100
        player_balance += game_economy.calculate_realized_money(treasure_val, player_balance)
        # Respawn treasure
        treasure_rect.x = random.randint(0, 750)
        treasure_rect.y = random.randint(0, 550)

    # Drawing
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player_rect) # Player
    pygame.draw.rect(screen, (255, 215, 0), treasure_rect) # Treasure
    
    # UI Counter
    text = font.render(f"Balance: {player_balance:.2f}", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
