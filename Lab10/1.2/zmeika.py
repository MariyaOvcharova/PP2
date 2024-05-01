import pygame
import sys
import time
import random
import psycopg2

pygame.init()

# color palette
colorBLACK = (0, 0, 0)
colorGRAY = (200, 200, 200)
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 26)
WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.get_ticks()
respawn = 5000

Level = 1
Score = 0
LevelNew = 0

timer1 = pygame.time.get_ticks()
respawn1 = 3000

FPS = 3
clock = pygame.time.Clock()

CELL = 30

LevelN = 1

podcluchenie = psycopg2.connect(
    host='localhost',
    dbname='postgres',
    user='postgres',
    password='1234'
)

cursor = podcluchenie.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
               Nickname VARCHAR(16) PRIMARY KEY,
               Level INT
);""")

podcluchenie.commit()


def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x - self.dx , head.y - self.dy))
            return True
        if head.x == betterfood.pos.x and head.y == betterfood.pos.y:
            self.body.append(Point(head.x - 2*self.dx , head.y - 2*self.dy))
            self.body.append(Point(head.x - 2*self.dx , head.y - 2*self.dy))
            return True
        return False
    
    
    def check_self_collision(self):
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False
    
class Food:
    def __init__(self):
        self.spawn_food()

    def spawn_food(self):
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))

    def move(self):
        pass

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def update(self):
        self.spawn_food()


class FoodBetter:
    def __init__(self):
        self.spawn_betterfood()

    def spawn_betterfood(self):
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))

    def move(self):
        pass

    def draw(self):
        pygame.draw.rect(screen, colorBLUE, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def updatefood(self):
        self.spawn_betterfood()


done = False

snake = Snake()
food = Food()
betterfood = FoodBetter()
TEXT = ""

def menu():
    doone = False
    f = 0
    txt = False
    m = ["Resume", "Save", "Exit"]
    while not doone:
        screen.fill((10, 15, 64))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    doone = True
                elif event.key == pygame.K_DOWN:
                    f += 1
                    if f > 2: f = 2
                elif event.key == pygame.K_UP:
                    f -= 1
                    if f < 0: f = 0
                if event.key == pygame.K_RETURN:
                    if f == 0: doone = True
                    if f == 1:
                        cursor.execute(f"""UPDATE users
                        SET Level = '{Level}'
                        WHERE nickname = '{TEXT}'
                        """)
                        podcluchenie.commit()
                        txt = True
                    if f == 2:
                        pygame.quit()
                        sys.exit()

        for i in range(3):
            if f == i:
                screen.blit(font_big.render('>' + m[i], True, colorWHITE), (100, 60 + 60*i))
            else:
                screen.blit(font_big.render(m[i], True, colorWHITE), (100, 60 + 60*i))
        if txt: screen.blit(font_big.render("Saved", True, colorWHITE), (450,550))
        
        pygame.display.flip()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                TEXT = TEXT[:-1]
            elif event.key == pygame.K_RETURN:
                done = True
            else:
                TEXT += event.unicode
                TEXT = TEXT[:20]
    
    screen.fill((10, 15, 64))
    pygame.draw.rect(screen, colorWHITE, pygame.Rect(100, 275, 400, 50))
    screen.blit(font_big.render("Enter your nickname", True, colorWHITE), (97,230))
    screen.blit(font_small.render(TEXT, True, colorBLACK), (120,285))
    
    pygame.display.flip()
    
cursor.execute(f"SELECT * FROM users WHERE nickname  = '{TEXT}'")
found = cursor.fetchone()
if found:
    loaded_Level = found[1]
    Level = found[1]
else:
    cursor.execute(f"""INSERT INTO users (nickname, Level) VALUES
                ('{TEXT}', 0);
            """)
    podcluchenie.commit()
    
    
done = False

while not done:
    now = pygame.time.get_ticks()
    now1 = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1

    cursor.execute(f"""UPDATE users
                        SET Level = {Level}
                        WHERE nickname = '{TEXT}'
                        """)
    podcluchenie.commit()


    draw_grid_chess()

#check collision with wall and self
    for segment in snake.body[1:]:
        if snake.body[0].x < 0 or snake.body[0].x >= WIDTH // CELL or snake.body[0].y < 0 or snake.body[0].y >= HEIGHT // CELL:
            print("wall")
            pygame.quit()
            sys.exit()
        if snake.body[0].x == segment.x and snake.body[0].y == segment.y:
            print("self")
            pygame.quit()
            sys.exit()



    snake.move()
    snake.draw()

    food.draw()
    betterfood.draw()

    #chech if snake eat food
    if snake.check_collision(food):
        print("Got food!")
        food.update()
        timer = now
        Score+=1

    #respawn food every 5 seconds 
    if now - timer > respawn:
        food.update()
        timer = now
    
    if snake.check_collision(betterfood):
        print("Got food!")
        betterfood.updatefood()
        timer1 = now1
        Score+=2
        Level+=1
        LevelNew = Level
    
    #respawn food every 5 seconds 
    if now1 - timer1 > respawn1:
        betterfood.updatefood()
        timer1 = now1

#change Level
    if Level % LevelN==0:
        LevelN+=2

    if Level > LevelNew/2:
        FPS+=0.1
    
    Levelll = font_small.render(str(Level), True, colorBLACK)
    scoreee = font_small.render(str(Score), True, colorBLACK)

    Levell = font_small.render("Level:", True, colorBLACK)
    scoree = font_small.render("Score:", True, colorBLACK)
    screen.blit(Levell, (10, 8))
    screen.blit(scoree, (100, 8))
    screen.blit(Levelll, (70, 8))
    screen.blit(scoreee, (170, 8))
    
    pygame.display.flip()
    clock.tick(FPS)