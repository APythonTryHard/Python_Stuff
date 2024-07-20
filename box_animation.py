import pygame
import random
# import noise

pygame.init()
W, H = 1000, 1000
screen = pygame.display.set_mode((1000, 900))
board = []
rect_list = []
walls = []

size = 10

color = (random.randint(1,255), random.randint(1,255), random.randint(1,255))

def make():
    global board
    board = []
    for x in range(60):
        small = []
        if random.randint(1, 50) == 1:
            wall = True
        for z in range(60):
            small.append([0, z])

        board.append(small)
    number = random.randint(0, len(board)-1)
    board[number][random.randint(0, len(board[number])-1)][0] = 1

# Timer variables
timer_interval = 2500  # Interval in milliseconds (5 seconds)
start_time = pygame.time.get_ticks()  # Get the current time when the timer starts

def update():
    global rect_list, board, walls
    updated_cells = [[False for _ in range(60)] for _ in range(60)]  # Track which cells have been updated
    for x in range(60):
        for z in range(60):
            if board[x][z][0] == 1 and not updated_cells[x][z]:
                if z < 59 and not board[x][z + 1][0] == 1 and board[z][x][0] != 2 and (board[x][z + 1][0] != 2 or board[x][z][0] == 2) and random.randint(1,16)==1:
                    board[x][z + 1][0] = 1
                    updated_cells[x][z + 1] = True
                if z > 0 and not board[x][z - 1][0] == 1 and board[z][x][0] != 2 and (board[x][z - 1][0] != 2 or board[x][z][0] == 2) and random.randint(1,16)==1:
                    board[x][z - 1][0] = 1
                    updated_cells[x][z - 1] = True
                if x < 59 and not board[x + 1][z][0] == 1 and board[z][x][0] != 2 and (board[x + 1][z][0] != 2 or board[x][z][0] == 2) and random.randint(1,16)==1:
                    board[x + 1][z][0] = 1
                    updated_cells[x + 1][z] = True
                if x > 0 and not board[x - 1][z][0] == 1 and board[z][x][0] != 2 and (board[x - 1][z][0] != 2 or board[x][z][0] == 2) and random.randint(1,16)==1:
                    board[x - 1][z][0] = 1
                    updated_cells[x - 1][z] = True
                if x < 59 and z < 59 and not board[x + 1][z + 1][0] == 1 and board[z][x][0] != 2 and (board[x + 1][z + 1][0] != 2 or board[x][z][0] == 2) and random.randint(1,16)==1:
                    board[x + 1][z + 1][0] = 1
                    updated_cells[x + 1][z + 1] = True
                if x > 0 and z > 0 and not board[x - 1][z - 1][0] == 1 and board[z][x][0] != 2 and (board[x - 1][z - 1][0] != 2 or board[x][z][0] == 2) and random.randint(1,16)==1:
                    board[x - 1][z - 1][0] = 1
                    updated_cells[x - 1][z - 1] = True
                if x < 59 and z > 0 and not board[x + 1][z - 1][0] == 1 and board[z][x][0] != 2 and (board[x + 1][z - 1][0] != 2 or board[x][z][0] == 2) and random.randint(1,16)==1:
                    board[x + 1][z - 1][0] = 1
                    updated_cells[x + 1][z - 1] = True
                if x > 0 and z < 59 and not board[x - 1][z + 1][0] == 1 and board[z][x][0] != 2 and (board[x - 1][z + 1][0] != 2 or board[x][z][0] == 2) and random.randint(1,16)==1:
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
    for rect in range(len(rect_list)):
        val = 255*rect/len(rect_list)
        pygame.draw.rect(screen, color, rect_list[rect])
    for rect in walls:
        pygame.draw.rect(screen, (255, 0, 0), rect)


# Main game loop
clock = pygame.time.Clock()
make()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Check if 5 seconds have passed
    elapsed_time = pygame.time.get_ticks() - start_time
    if elapsed_time >= timer_interval:
        make()  # Run the make function
        start_time = pygame.time.get_ticks()  # Reset the timer
        color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))


    screen.fill((0,0,0))
    update()
    draw()
    pygame.display.update()
    clock.tick(100)  # Limit the frame rate
