import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Repeating Explosion Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Explosion properties
explosion_radius = 10
explosion_strength = 5
explosion_color = RED
explosion_duration = 700  # 2 seconds in milliseconds
last_explosion_time = 0

# Small block properties
num_small_blocks = 250
small_block_size = 5
small_blocks = []

# Function to create explosion
def create_explosion():
    small_blocks.clear()
    place = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
    for _ in range(num_small_blocks):
        angle = random.uniform(0, 2*math.pi)
        speed = random.uniform(5, 10)
        small_blocks.append({
            "x": place[0],
            "y": place[1],
            "dx": speed * math.cos(angle),
            "dy": speed * math.sin(angle),
            "color": (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        })

# Main loop
while True:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Check if it's time to create a new explosion
    if current_time - last_explosion_time >= explosion_duration:
        create_explosion()
        last_explosion_time = current_time

    # Draw small blocks
    for small_block in small_blocks:
        pygame.draw.rect(screen, small_block["color"], (small_block["x"], small_block["y"], small_block_size, small_block_size))
        small_block["x"] += small_block["dx"]
        small_block["y"] += small_block["dy"]

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
