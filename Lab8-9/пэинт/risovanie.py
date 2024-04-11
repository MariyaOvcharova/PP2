import pygame as pg 
import math 
 
pg.init() 
 
screen = pg.display.set_mode((500, 500)) 
clock = pg.time.Clock() 
 
done = False 
orange = (255, 144, 10) 
red = (255, 0, 0) 
green = (15, 200, 40) 
blue = (30, 90, 200) 
white = (255, 255, 255) 
black = (0, 0, 0) 
 
LMBpressed = False 
 
screen.fill(white) 
 
base_layer = pg.Surface((500, 500)) 
base_layer.fill(white) 
 
brush = orange 
 
x = 0 
y = 0  
x1 = 0 
y1 = 0 
 
color = black 
 
drawing_mode = "brush"   
rect_size = 0 
circle_radius = 0 
draw_shape = False 
 
while not done: 
    mouse = pg.mouse.get_pos() 
 
    # Buttons 
    rectOrange = pg.draw.rect(base_layer, orange, pg.Rect(20, 20, 20, 20)) 
    rectRed = pg.draw.rect(base_layer, red, pg.Rect(50, 20, 20, 20)) 
    rectGreen = pg.draw.rect(base_layer, green, pg.Rect(80, 20, 20, 20)) 
    rectBlue = pg.draw.rect(base_layer, blue, pg.Rect(110, 20, 20, 20)) 
    Eraser = pg.draw.rect(base_layer, black, pg.Rect(140, 20, 20, 20), 2) 
    DrawRect = pg.draw.rect(base_layer, black, pg.Rect(170, 20, 20, 20)) 
    DrawCircle = pg.draw.rect(base_layer, black, pg.Rect(200, 20, 20, 20)) 
    DrawSquare = pg.draw.rect(base_layer, black, pg.Rect(230, 20, 20, 20)) 
    DrawRightTriangle = pg.draw.rect(base_layer, black, pg.Rect(260, 20, 20, 20)) 
    DrawEquilateralTriangle = pg.draw.rect(base_layer, black, pg.Rect(290, 20, 20, 20)) 
    DrawRhombus = pg.draw.rect(base_layer, black, pg.Rect(320, 20, 20, 20)) 
 
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            done = True 
 
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1: 
            LMBpressed = True 
            x, y = event.pos 

            # Check which button was pressed 
            if rectOrange.collidepoint(*mouse): 
                drawing_mode = "brush"  
                brush = orange 
            elif rectBlue.collidepoint(*mouse): 
                drawing_mode = "brush"  
                brush = blue 
            elif rectGreen.collidepoint(*mouse): 
                drawing_mode = "brush"  
                brush = green 
            elif rectRed.collidepoint(*mouse): 
                drawing_mode = "brush"  
                brush = red 
            elif Eraser.collidepoint(*mouse): 
                drawing_mode = "brush"  
                brush = white 
            elif DrawRect.collidepoint(*mouse): 
                drawing_mode = "rect" 
                print("AAAAA") 
                rect_size = 0   
                x, y = event.pos   
                x1, y1 = event.pos 
            elif DrawCircle.collidepoint(*mouse): 
                drawing_mode = "circle" 
                circle_radius = 0  
                x1, y1 = event.pos   
            elif DrawSquare.collidepoint(*mouse): 
                drawing_mode = "square" 
                draw_shape = True 
                x1, y1 = event.pos 
            elif DrawRightTriangle.collidepoint(*mouse): 
                drawing_mode = "right_triangle" 
                draw_shape = True 
                x1, y1 = event.pos 
            elif DrawEquilateralTriangle.collidepoint(*mouse): 
                drawing_mode = "equilateral_triangle" 
                draw_shape = True 
                x1, y1 = event.pos 
            elif DrawRhombus.collidepoint(*mouse): 
                drawing_mode = "rhombus" 
                draw_shape = True 
                x1, y1 = event.pos 
 
        if event.type == pg.MOUSEMOTION  and LMBpressed: 
            if drawing_mode == "brush":
                if x != 0 and y != 0: 
                    x1, y1 = event.pos 
                    if brush != white:  # not eraser 
                        pg.draw.line(base_layer, brush, (x, y), (x1, y1), 2) 
                        x, y = x1, y1 
                    else:  # eraser 
                        pg.draw.line(base_layer, brush, (x, y), (x1, y1), 20) 
                        x, y = x1, y1 
 
        if event.type == pg.MOUSEMOTION and LMBpressed and draw_shape: 
            if x != 0 and y != 0: 
                x1, y1 = event.pos 
 
        if event.type == pg.MOUSEBUTTONUP: 
            LMBpressed = False 
            x1 , y1 = event.pos 
             
            if drawing_mode == "rect": 
                    print("DSAD") 
                    size = max(abs(x - x1), abs(y - y1)) 
                    pg.draw.rect(base_layer, black, pg.Rect(x, y, abs(x - x1), abs(y - y1)), 5) 

            if drawing_mode == "circle":
                radius = int(math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2))
                pg.draw.circle(base_layer, black, (x, y), radius, 2)

            if drawing_mode == "square":
                size = max(abs(x - x1), abs(y - y1)) 
                pg.draw.rect(base_layer, black, pg.Rect(x, y, abs(x - x1), abs(x - x1)), 3) 

            if drawing_mode == "right_triangle":
                print("K")
                size = max(abs(x - x1), abs(y - y1))
                pg.draw.polygon(base_layer, black, ((x, y+(y-y1)), (x+(x-x1), y), (x, y)), 3)

            if drawing_mode == "equilateral_triangle":
                pg.draw.polygon(base_layer, black, ((x, y), (x+(max(abs(x1-x), abs(y1-y))/math.sqrt(3)), y+max(abs(x1-x), abs(y1-y))), (x-(max(abs(x1-x), abs(y1-y))/math.sqrt(3)), y+max(abs(x1-x), abs(y1-y)))), 2)

            if drawing_mode == "rhombus":
                pg.draw.polygon(base_layer, black, ((x, y), (x+(max(abs(x1-x), abs(y1-y))/math.sqrt(3))/2, y+(max(abs(x1-x), abs(y1-y)))/2), (x, y + max(abs(x1-x), abs(y1-y))), (x-(max(abs(x1-x), abs(y1-y))/math.sqrt(3))/2, y+max(abs(x1-x), abs(y1-y))/2)), 3)


    screen.blit(base_layer, (0, 0)) 
    pg.display.flip() 
    clock.tick(60)