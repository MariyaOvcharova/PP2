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

def calculate_rect(x0, y0, x01, y01):
    return pg.Rect(min(x0, x01), min(y0, y01), abs(x0 - x01), abs(y0 - y01))

def draw_circle(surface, color, center, radius):
    pg.draw.circle(surface, color, center, radius, 2)

def draw_ellipse(surface, color, rect):
    pg.draw.ellipse(surface, color, rect, 2)

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
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            x, y = event.pos

            # Check which button was pressed
            if rectOrange.collidepoint(*mouse):
                brush = orange
            elif rectBlue.collidepoint(*mouse):
                brush = blue
            elif rectGreen.collidepoint(*mouse):
                brush = green
            elif rectRed.collidepoint(*mouse):
                brush = red
            elif Eraser.collidepoint(*mouse):
                brush = white
            elif DrawRect.collidepoint(*mouse):
                brush = black
            elif DrawCircle.collidepoint(*mouse):
                brush = black

        if event.type == pg.MOUSEMOTION and LMBpressed:
            if x != 0 and y != 0:
                x1, y1 = event.pos
                if brush != white:  # If not eraser, draw normally
                    pg.draw.line(base_layer, brush, (x, y), (x1, y1), 2)
                else:  # If eraser, draw white line to simulate erasing
                    pg.draw.line(base_layer, brush, (x, y), (x1, y1), 20)
                x, y = x1, y1

        if event.type == pg.MOUSEBUTTONUP:
            LMBpressed = False
            if brush == black and (DrawRect.collidepoint(*mouse) or DrawCircle.collidepoint(*mouse)):
                if DrawRect.collidepoint(*mouse):
                    pg.draw.rect(base_layer, brush, calculate_rect(x1, y1, x, y), 2)
                elif DrawCircle.collidepoint(*mouse):
                    radius = int(math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2))
                    draw_circle(base_layer, brush, (x, y), radius)
  
    screen.blit(base_layer, (0, 0))
    pg.display.flip()
    clock.tick(60)
