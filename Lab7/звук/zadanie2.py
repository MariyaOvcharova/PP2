import pygame 
pygame.init()

Grenade = pygame.mixer.Sound("Bruno_Mars_-_Grenade_899818.mp3")
Eminem = pygame.mixer.Sound("Eminem_Rihanna_-_Love_The_Way_You_Lie_47965688.mp3")
Hold = pygame.mixer.Sound("Macklemore_-_Cant_Hold_Us_48376720.mp3")

screen = pygame.display.set_mode((315, 290))

done = False

playing = Grenade
playing.play()
c=1
z=0
t=0

white = (255, 255, 255)

black = (0, 0, 0)
grey = (78,87,84)


while not done:
    pygame.draw.polygon(screen, white, [[210, 110], [240, 130], [210, 150]])
    pygame.draw.polygon(screen, white, [[240, 110], [270, 130], [240, 150]])
    pygame.draw.polygon(screen, white, [[100, 110], [70, 130], [100, 150]])
    pygame.draw.polygon(screen, white, [[70, 110], [40, 130], [70, 150]])

    if c==1:
        pygame.draw.polygon(screen, white, [[140, 110], [170, 130], [140, 150]]) 
     
         
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    
        if event.type == pygame.KEYDOWN:
                  
            if event.key == pygame.K_SPACE:
                c+=1
               
                if c%2==0:
                    pygame.draw.polygon(screen, black, [[140, 110], [170, 130], [140, 150]])
                    pygame.draw.rect(screen, white, pygame.Rect(135, 110, 15, 40))
                    pygame.draw.rect(screen, white, pygame.Rect(160, 110, 15, 40))
                    
                    pygame.mixer.pause()
                  
                else:
                    pygame.draw.rect(screen, black, pygame.Rect(135, 110, 15, 40))
                    pygame.draw.rect(screen, black, pygame.Rect(160, 110, 15, 40))
                    pygame.draw.polygon(screen, white, [[140, 110], [170, 130], [140, 150]])
                    pygame.mixer.unpause()
               

            if event.key == pygame.K_RIGHT:
                
                z+=1
                if z==1:
                    
                    pygame.mixer.stop()
                    playing = Eminem.play()
                elif z==2:
                    
                    pygame.mixer.stop()
                    playing = Hold.play()
                elif z==3:
                    
                    pygame.mixer.stop()
                    playing = Grenade.play()
                    z=0


            if event.key == pygame.K_LEFT:
                t+=1
   
                if t==1:
                   
                    pygame.mixer.stop()
                    playing = Eminem.play()
                    
                elif t==2:
                    
                    pygame.mixer.stop()
                    playing = Hold.play()
                    
                elif t==3:
                    
                    pygame.mixer.stop()
                    playing = Grenade.play()
                  
                    t=0


    pygame.display.flip()
  
   