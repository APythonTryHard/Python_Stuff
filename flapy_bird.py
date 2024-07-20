import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

player = pygame.Rect(100, 100, 10, 10)
velocity = 1
DEATH = False

pipe_list = [pygame.Rect(300, 0, 30, 300)]


def gen_pipes():
    y = random.randint(150, 500)
    pipe_list.append(pygame.Rect(800, 0, 25, y))
    y2 = random.randint(max(500, y + 200), 800)
    pipe_list.append(pygame.Rect(800, y2, 25, 600))


def update():
    pygame.draw.rect(screen, (0, 0, 255), player)

    for rect in pipe_list:
        pygame.draw.rect(screen, (0, 0, 255), rect)


def phyisics():
    global player, velocity, DEATH
    player.y -= velocity
    if velocity > -15:
        velocity -= 2

    for rect in pipe_list:
        rect.x -= 5


def collisions():
    global DEATH
    for rect in pipe_list:
        if player.colliderect(rect):
            DEATH = True


def starting_screen():

    started = False
    while not started:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE:
                    pass

        pygame.display.update()
        clock.tick(30)


TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 1000)

while not DEATH:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == TIMER_EVENT:
            gen_pipes()
        elif event.type == pygame.KEYDOWN:  # Ensure this is a key event
            if event.key == pygame.K_SPACE:
                velocity = 20

    update()
    phyisics()
    collisions()
    pygame.display.update()
    clock.tick(30)
