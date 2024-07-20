import noise
import pygame

screen = pygame.display.set_mode((500, 500))
pygame.init()

clock = pygame.time.Clock()

iteration = 0.01
rect = pygame.Rect(250, 250, 50, 50)

x_o = 1
y_o = 1

x_p = 0.1
y_p = 0.1
def update():
    global iteration, x_o, y_o, x_p, y_p
    rect.x = (noise.pnoise1(iteration, octaves = x_o, persistence=x_p)*100)+255
    rect.y = (noise.pnoise1(-iteration, octaves = y_o, persistence=y_p)*100)+255
    iteration += 0.1

    pygame.draw.rect(screen, (0, 255, 0), rect)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    update()
    pygame.display.update()
    clock.tick(30)
