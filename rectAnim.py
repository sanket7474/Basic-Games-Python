import pygame

# Init
pygame.init()
window = pygame.display.set_mode((500, 500))
exit_game = False

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# setup

rectX = 100;
rectY = 50;
xVel = 0.12;
yVel = 0.21;

sizeX = 10
sizeY = 10

sizeFactor = 0.02;

window.fill(white)

# Game Loop
while not exit_game:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit_game = True
    window.fill(white)
    pygame.draw.rect(window, black, (rectX, rectY, sizeX, sizeY))

    if rectX <= 0 or rectX + sizeX >= 500:
        xVel = -xVel
        sizeFactor = -sizeFactor
    if rectY <= 0 or rectY + sizeY >= 500:
        yVel = -yVel
        sizeFactor = -sizeFactor

    rectX += xVel
    rectY += yVel

    sizeX += sizeFactor

    sizeY += sizeFactor
    pygame.display.update()

pygame.quit()
quit()
