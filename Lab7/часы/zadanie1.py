import pygame 
pygame.init()
import datetime

screen = pygame.display.set_mode((768, 768))

done = False

chasi = pygame.image.load("часы.jpg")
minuta = pygame.image.load("минутная.png")
secunda = pygame.image.load("секундная.png")
black = (0, 0, 0)


minuta = pygame.transform.scale(minuta, (45, 550))
secunda = pygame.transform.scale(secunda, (50, 500))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    vremya = datetime.datetime.now().time()
    minYgl = vremya.minute / 60 * 360
    secYgl = vremya.second / 60 * 360
  
    minuta1 = pygame.transform.rotate(minuta, -minYgl)
    secunda1 = pygame.transform.rotate(secunda, -secYgl)
   
    minutaRect = minuta1.get_rect(center=(395, 375))
    secundaRect = secunda1.get_rect(center=(394, 384))
    screen.blit(pygame.transform.scale(chasi, (768, 768)), (0, 0))
    
    screen.blit(minuta1, minutaRect)
    screen.blit(secunda1, secundaRect)
    pygame.draw.circle(screen, black, (392, 386), 20)
    pygame.display.flip()

