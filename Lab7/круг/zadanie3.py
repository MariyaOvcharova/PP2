import pygame
pygame.init()

screen = pygame.display.set_mode((415, 415))

red = (255, 0, 0)
white = (255, 255, 255)


x = 25
y = 25

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True        

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x + 25 < 410: 
        x += 20
    if keys[pygame.K_LEFT] and x - 25 > 0: 
        x -= 20
    if keys[pygame.K_UP] and y - 25 > 0: 
        y -= 20
    if keys[pygame.K_DOWN] and y + 25 < 410: 
        y += 20
    screen.fill(white)
    pygame.draw.circle(screen, red, (x, y), 25)

    pygame.display.flip()
    clock.tick(60)