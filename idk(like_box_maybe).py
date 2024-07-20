import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiple Simultaneous Explosions")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Explosion properties
explosion_radius = 5
explosion_strength = 5
explosion_color = RED
explosion_duration = 50
explosions = []

# Small block properties
num_small_blocks = 100
small_block_size = 20

# Function to create a new explosion
def create_explosion(x, y):
    small_blocks = []
    for _ in range(num_small_blocks):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(5, 10)
        small_blocks.append({
            "x": x,
            "y": y,
            "dx": speed * math.cos(angle),
            "dy": speed * math.sin(angle),
            "color": (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        })
    explosions.append(small_blocks)


create_explosion(WIDTH / 2, HEIGHT / 2)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    create_explosion(WIDTH / 2, HEIGHT / 2)
    # Update and draw explosions
    for explosion in explosions:
        for block in explosion[:]:  # Iterate over a copy of the list
            pygame.draw.rect(screen, block["color"], (block["x"], block["y"], small_block_size, small_block_size))
            block["x"] += block["dx"]
            block["y"] += block["dy"]

            # Remove block if it goes off screen
            if block["x"] < 0 or block["x"] > WIDTH or block["y"] < 0 or block["y"] > HEIGHT:
                explosion.remove(block)

    # Remove empty explosions
    explosions = [explosion for explosion in explosions if explosion]

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
