from sense_hat import SenseHat
import time
import random
    
senseHat = SenseHat()
senseHat.low_light = True

GREEN = (0, 255, 0)
RED = (255, 0, 0)
START_DELAY = 3
MIN_VALUE = 0
MAX_VALUE = 7
SIZE = 8

while True:
    # variables:
    gameOver = False
    growSnake = False
    generateRandomFood = False
    snakeMovementDelay = 0.5
    snakeMovementDelayDecrease = -0.02

    # start delay:
    time.sleep(START_DELAY)

    # set default snake starting position (values are chosen by preference):
    snakePosX = [3]
    snakePosY = [6]

    # generate random food position:
    while True:
        foodPosX = random.randint(0, 7)
        foodPosY = random.randint(0, 7)
        if foodPosX != snakePosX[0] or foodPosY != snakePosY[0]:
            break

    # set default snake starting direction (values are chosen by preference):
    movementX = 0
    movementY = -1

    # -----------------------------------
    #             game loop
    # -----------------------------------
    while not gameOver:
        # check if snake eats food:
        if foodPosX == snakePosX[0] and foodPosY == snakePosY[0]:
            growSnake = True
            generateRandomFood = True
            snakeMovementDelay += snakeMovementDelayDecrease

        # check if snake bites itself:
        for i in range(1, len(snakePosX)):
            if snakePosX[i] == snakePosX[0] and snakePosY[i] == snakePosY[0]:
                gameOver = True

        # check if game-over:
        if gameOver:
            break

        # check joystick events:
        events = senseHat.stick.get_events()
        for event in events:
            if event.direction == "left" and movementX != 1:
                movementX = -1
                movementY = 0
            elif event.direction == "right" and movementX != -1:
                movementX = 1
                movementY = 0
            elif event.direction == "up" and movementY != 1:
                movementY = -1
                movementX = 0
            elif event.direction == "down" and movementY != -1:
                movementY = 1
                movementX = 0

        # grow snake:
        if growSnake:
            growSnake = False
            snakePosX.append(0)
            snakePosY.append(0)

        # move snake:
        for i in range((len(snakePosX) - 1), 0, -1):
            snakePosX[i] = snakePosX[i - 1]
            snakePosY[i] = snakePosY[i - 1]

        snakePosX[0] += movementX
        snakePosY[0] += movementY

        # check game borders:
        if snakePosX[0] > MAX_VALUE:
            snakePosX[0] -= SIZE
        elif snakePosX[0] < MIN_VALUE:
            snakePosX[0] += SIZE
        if snakePosY[0] > MAX_VALUE:
            snakePosY[0] -= SIZE
        elif snakePosY[0] < MIN_VALUE:
            snakePosY[0] += SIZE

        # spawn random food:
        if generateRandomFoodFlag:
            generateRandomFoodFlag = False
            retryFlag = True
            while retryFlag:
                foodPosX = random.randint(0, 7)
                foodPosY = random.randint(0, 7)
                retryFlag = False
                for x, y in zip(snakePosX, snakePosY):
                    if x == foodPosX and y == foodPosY:
                        retryFlag = True
                        break

        # update matrix:
        senseHat.clear()
        senseHat.set_pixel(foodPosX, foodPosY, RED)
        for x, y in zip(snakePosX, snakePosY):
            senseHat.set_pixel(x, y, GREEN)

        # snake speed (game loop delay):
        time.sleep(snakeMovementDelay)