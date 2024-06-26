#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SPEED1 = 3
SPEED2 = 4
SCORE = 0
COINS = 0
#for every 30 coins speed make faster
n = 10 

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#class make cars at random places 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

      
#class make coins at random places 
class Coins(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load("coin.png"), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
      def money(self):
        self.rect.move_ip(0,SPEED1)
        
      def move(self):
        global COINS
        self.rect.move_ip(0,SPEED1)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#class make dollar at random places 
class Dollar(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load("купюра.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
      def money(self):
        self.rect.move_ip(0,SPEED2)
        
      def move(self):
        global COINS
        self.rect.move_ip(0,SPEED2)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


#make player and check pressed keys
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
       
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
M1 = Coins()
M2 = Dollar()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(M1)
coins1 = pygame.sprite.Group()
coins1.add(M2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(M1)
all_sprites.add(M2)


#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              # SPEED += 0.5 for lab 8
              SPEED1 += 0.2    
              SPEED2 += 0.1  
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    #num of cars and scores of coins
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (65,10))
    coin = font_small.render(str(COINS), True, BLACK)

    Koshelek = font_small.render("Coins:", True, BLACK)
    Cars = font_small.render("Cars:", True, BLACK)
    DISPLAYSURF.blit(Cars, (10, 8))
    DISPLAYSURF.blit(Koshelek, (100, 8))
    DISPLAYSURF.blit(coin, (165, 10))

    #total scorses after game ower
    total = font_small.render("Total score:", True, BLACK)
    total1 = font_small.render( str(SCORE) , True, BLACK)
    total2 = font_small.render("Total coins:", True, BLACK)
    total3 = font_small.render(str(COINS), True, BLACK)
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    #check that player take coin or not 
    if pygame.sprite.spritecollideany(P1, coins1):
        COINS += 2
        #for every 10 coin make car faster
        if COINS % n == 0 and COINS!=0:
          SPEED += 1.5

        for coin in coins1:
            coin.rect.top = 0
            coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    if pygame.sprite.spritecollideany(P1, coins):
        COINS += 1
        #for every 10 coin make car faster
        if COINS % n == 0 and COINS!=0:
          SPEED += 1.5

        for coin in coins:
            coin.rect.top = 0
            coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

  
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)

          #show total scorses after game ower
          DISPLAYSURF.blit(game_over, (30,250))
          DISPLAYSURF.blit(total, (130,355))
          DISPLAYSURF.blit(total1, (250,355))
          DISPLAYSURF.blit(total2, (130,380))
          DISPLAYSURF.blit(total3, (250,380))


          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit() 
 
    pygame.display.update()
    FramePerSec.tick(FPS)