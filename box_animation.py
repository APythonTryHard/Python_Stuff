import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1000, 1000))

board = []
for x in range(60):
    small = []
    for z in range(60):
        small.append([0, z])
    board.append(small)

rect_list = []
walls = []


def update():
    global rect_list, board, walls
    updated_cells = [[False for _ in range(60)] for _ in range(60)]  # Track which cells have been updated
    for x in range(60):
        for z in range(60):
            if board[x][z][0] == 1 and not updated_cells[x][z]:
                if z < 59 and not board[x][z + 1][0] == 1 and random.randint(1,16)==1:
                    board[x][z + 1][0] = 1
                    updated_cells[x][z + 1] = True
                if z > 0 and not board[x][z - 1][0] == 1 and random.randint(1,16)==1:
                    board[x][z - 1][0] = 1
                    updated_cells[x][z - 1] = True
                if x < 59 and not board[x + 1][z][0] == 1 and random.randint(1,16)==1:
                    board[x + 1][z][0] = 1
                    updated_cells[x + 1][z] = True
                if x > 0 and not board[x - 1][z][0] == 1 and random.randint(1,16)==1:
                    board[x - 1][z][0] = 1
                    updated_cells[x - 1][z] = True
                if x < 59 and z < 59 and not board[x + 1][z + 1][0] == 1 and random.randint(1,16)==1:
                    board[x + 1][z + 1][0] = 1
                    updated_cells[x + 1][z + 1] = True
                if x > 0 and z > 0 and not board[x - 1][z - 1][0] == 1 and random.randint(1,16)==1:
                    board[x - 1][z - 1][0] = 1
                    updated_cells[x - 1][z - 1] = True
                if x < 59 and z > 0 and not board[x + 1][z - 1][0] == 1 and random.randint(1,16)==1:
                    board[x + 1][z - 1][0] = 1
                    updated_cells[x + 1][z - 1] = True
                if x > 0 and z < 59 and not board[x - 1][z + 1][0] == 1 and random.randint(1,16)==1:
                    board[x - 1][z + 1][0] = 1
                    updated_cells[x - 1][z + 1] = True
    rect_list = []
    walls = []
    for x in range(60):
        for z in range(60):
            if board[x][z][0] == 1:
                rect_list.append(pygame.Rect(z * 20, x * 20, 20, 20))
            if board[x][z][0] == 2:
                walls.append(pygame.Rect(z * 20, x * 20, 20, 20))


def draw():
    for rect in rect_list:
        pygame.draw.rect(screen, (0,0,0), rect)
    for rect in walls:
        pygame.draw.rect(screen, (0, 255, 0), rect)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255,0,0))
    update()
    draw()
    pygame.display.update()
    clock.tick(100)  # Limit the frame rate
