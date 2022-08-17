import pygame, copy, random

pygame.init()

# Screen size
screen = pygame.display.set_mode((1000, 1000))

# RGB Background color
backgroundColor = (100, 100, 100)
screen.fill(backgroundColor)

# Title
pygame.display.set_caption('Snake')

# Update whole display using flip
pygame.display.flip()

# Var to keep game running
running = True

# Starting Cords, Size, and Direction
player = [[500, 500, 20, 20], [500, 480, 20, 20], [500, 460, 20, 20], [500, 440, 20, 20]]
playerDir = 'NORTH'
playerColor = (255, 0, 255)

# Size of grid objects
cubeSize = 20

# Starting Food
food = (220, 240, 20, 20)
foodColor = (50, 255, 50)
pygame.draw.rect(screen, foodColor, food)
pygame.display.update(food)

# Time Vars
FPS = 12
clock = pygame.time.Clock()
deltaTime = clock.tick(FPS)

# See if cube was added during tick, and cubeScore
addedCube = False
cubeScore = 0

# Allow first cubes to load
warmUp = 0

# Game Loop
while running:

    clock.tick(FPS)
    # Loop through event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

    # Saves key pressed
    keys = pygame.key.get_pressed()

    if keys[ord('a')]:
        playerDir = 'WEST'
    if keys[ord('d')]:
        playerDir = 'EAST'
    if keys[ord('w')]:
        playerDir = 'NORTH'
    if keys[ord('s')]:
        playerDir = 'SOUTH'
    if keys[ord('c')]:
        addedCube = True

    # Move player [0][1] is the heads x, [0][0] is the heads y
    if playerDir == 'NORTH':
        player[0][1] -= cubeSize
    elif playerDir == 'SOUTH':
        player[0][1] += cubeSize
    elif playerDir == 'WEST':
        player[0][0] -= cubeSize
    elif playerDir == 'EAST':
        player[0][0] += cubeSize

    # Check food collision
    if player[0][0] == food[0]:
        if player[0][1] == food[1]:
            addedCube = True
            food = (random.randint(1, 49) * 20, random.randint(1, 49) * 20, 20, 20)
            cubeScore += 1
            pygame.display.set_caption(f'Snake     Score:{cubeScore}')

    # Check loss condition
    if warmUp > 2:
        for i in range(len(player)):
            if i == 0:
                continue
            if player[i][0] == player[0][0]:
                if player[i][1] == player[0][1]:
                    FPS = 0
    else:
        warmUp += 1

    # Copy of old player for moving
    oldPlayer = copy.deepcopy(player)

    # Color and move all blocks
    for i in range(len(player)):
        if i == 0:
            pygame.draw.rect(screen, playerColor, player[i])
            pygame.display.update(player[i])
            continue
        player[i] = oldPlayer[player.index(player[i]) - 1]
        pygame.draw.rect(screen, playerColor, player[i])
        pygame.display.update(player[i])

    if not addedCube:
        # Color old tail the same as the background
        pygame.draw.rect(screen, backgroundColor, oldPlayer[len(oldPlayer) - 1])
        pygame.display.update(oldPlayer[len(oldPlayer) - 1])
    else:
        player.append(oldPlayer[len(oldPlayer) - 1])
        pygame.display.update(player[len(player) - 1])
        addedCube = False

    # Draw Food
    pygame.draw.rect(screen, foodColor, food)
    pygame.display.update(food)
