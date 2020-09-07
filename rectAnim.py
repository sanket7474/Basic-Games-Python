import pygame

# Init
pygame.init()
window = pygame.display.set_mode((500, 500))
exit_game = False

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# setup

fps = 60

rectX = 100;
rectY = 150;
xVel = 3;
yVel = 3;

sizeX = 10
sizeY = 10

sizeFactor = 0.5;

window.fill(white)

clock = pygame.time.Clock()
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

    if sizeX < 10 or sizeY < 10:
        sizeFactor = -sizeFactor

    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()

# Sometimes rectangle crosses window border