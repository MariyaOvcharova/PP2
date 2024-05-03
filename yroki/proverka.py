import pg
import math

pg.init()

WIDTH = 800
HEIGHT = 600

screen = pg.display.set_mode((WIDTH, HEIGHT))
add_screen = pg.Surface((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

clock = pg.time.Clock()

LMBpressed = False
THICKNESS = 5
i = 0
lst = [colorRED, colorBLUE, colorWHITE]
font = pg.font.SysFont("Verdana", 20)

currX = 0
currY = 0

x = 0
prevY = 0
fig = 0

done = False
Eveeent = pg.USEREVENT #event for title of color

def calculate_rect(x1, y1, x2, y2):
    return pg.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

while not done:
    for event in pg.event.get():
        if (fig != 0 and fig != 3) and LMBpressed:
            screen.blit(add_screen, (0,0))
        if event.type == pg.QUIT:
            done = True
        if event.type == Eveeent:
            pg.draw.rect(screen, colorBLACK, pg.Rect(10, 570, 130, 50))
            pg.time.set_timer(Eveeent, 0) # deleting title of color choosed after 1s
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            if fig == 0 or fig == 3 or fig == 5:
                currX = event.pos[0]
                currY = event.pos[1]
                x = event.pos[0]
                prevY = event.pos[1]
            else:
                x = event.pos[0]
                prevY = event.pos[1]
        if event.type == pg.MOUSEMOTION:
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                if fig == 1:
                    pg.draw.rect(screen, lst[i], calculate_rect(x, prevY, currX, currY), THICKNESS)
                if fig == 2:
                    pg.draw.circle(screen, lst[i], (x, prevY), max(abs(currX-x), abs(currY-prevY)), THICKNESS)
                if fig == 4:
                    pg.draw.rect(screen, lst[i], pg.Rect(min(x, currX), min(prevY, currY), abs(x-currX), abs(x-currX)))
                if fig == 5:
                    pg.draw.polygon(screen, lst[i], ((x, prevY+(prevY-currY)), (x+(x-currX), prevY), (x, prevY)))
                if fig == 6:
                    pg.draw.polygon(screen, lst[i], ((x, prevY), (x+(max(abs(currX-x), abs(currY-prevY))/math.sqrt(3)), prevY+max(abs(currX-x), abs(currY-prevY))), (x-(max(abs(currX-x), abs(currY-prevY))/math.sqrt(3)), prevY+max(abs(currX-x), abs(currY-prevY)))))
                if fig == 7:
                    pg.draw.polygon(screen, lst[i], ((x, prevY), (x+(max(abs(currX-x), abs(currY-prevY))/math.sqrt(3))/2, prevY+(max(abs(currX-x), abs(currY-prevY)))/2), (x, prevY + max(abs(currX-x), abs(currY-prevY))), (x-(max(abs(currX-x), abs(currY-prevY))/math.sqrt(3))/2, prevY+max(abs(currX-x), abs(currY-prevY))/2)))
                # drawing figures by indexes not finaly displaying on screen
        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            if fig == 1:
                pg.draw.rect(screen, lst[i], calculate_rect(x, prevY, currX, currY), THICKNESS)
            if fig == 2:
                pg.draw.circle(screen, lst[i], (x, prevY), max(abs(currX-x), abs(currY-prevY)), THICKNESS)
            if fig == 4:
                pg.draw.rect(screen, lst[i], pg.Rect(min(x, currX), min(prevY, currY), abs(x-currX), abs(x-currX)))
            if fig == 5:
                pg.draw.polygon(screen, lst[i], ((x, prevY+(prevY-currY)), (x+(x-currX), prevY), (x, prevY)))
            if fig == 6:
                pg.draw.polygon(screen, lst[i], ((x, prevY), (x+(max(abs(currX-x), abs(currY-prevY))/math.sqrt(3)), prevY+max(abs(currX-x), abs(currY-prevY))), (x-(max(abs(currX-x), abs(currY-prevY))/math.sqrt(3)), prevY+max(abs(currX-x), abs(currY-prevY)))))
            if fig == 7:
                pg.draw.polygon(screen, lst[i], ((x, prevY), (x+(max(abs(currX-x), abs(currY-prevY))/math.sqrt(3))/2, prevY+(max(abs(currX-x), abs(currY-prevY)))/2), (x, prevY + max(abs(currX-x), abs(currY-prevY))), (x-(max(abs(currX-x), abs(currY-prevY))/math.sqrt(3))/2, prevY+max(abs(currX-x), abs(currY-prevY))/2)))
            add_screen.blit(screen, (0,0))
            # final display figures on screen after release mouse button
        if fig == 0:
            pg.draw.line(screen, lst[i], (x, prevY), (currX, currY), THICKNESS)
            # simple line
        if fig == 3:
            pg.draw.line(screen, colorBLACK, (x, prevY), (currX, currY), THICKNESS)
            # eraser
        if event.type == pg.KEYDOWN: 
            if event.key == pg.K_EQUALS:
                THICKNESS += 1
            if event.key == pg.K_MINUS:
                THICKNESS -= 1
            if event.key == pg.K_LEFT:
                i -= 1
                if i < 0: i = 0
                if i == 0:
                    screen.blit(font.render("Color: red",True, (0, 255, 255)), (10, 570))
                    pg.time.set_timer(Eveeent, 1000)
                if i == 1:
                    screen.blit(font.render("Color: blue",True, (0, 255, 255)), (10, 570))
                    pg.time.set_timer(Eveeent, 1000)
            if event.key == pg.K_RIGHT:
                i += 1
                if i > 2: i = 2
                if i == 1:
                    screen.blit(font.render("Color: blue",True, (0, 255, 255)), (10, 570))
                    pg.time.set_timer(Eveeent, 1000)
                if i == 2:
                    screen.blit(font.render("Color: white",True, (0, 255, 255)), (10, 570))
                    pg.time.set_timer(Eveeent, 1000)
            # changing colors
                
    keys = pg.key.get_pressed()
    
    
    if fig == 0 or fig == 3:
        x = currX
        prevY = currY
        
        
    if keys[pg.K_r]: fig = 1
    if keys[pg.K_l]: fig = 0
    if keys[pg.K_c]: fig = 2
    if keys[pg.K_e]: fig = 3
    if keys[pg.K_s]: fig = 4
    if keys[pg.K_t]: fig = 5
    if keys[pg.K_p]: fig = 6
    if keys[pg.K_o]: fig = 7
    # selecting figures

    pg.display.flip()
    clock.tick(60)