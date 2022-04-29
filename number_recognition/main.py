from tensorflow.keras.models import load_model
import pygame
import numpy as np

import pickle
import matplotlib.pyplot as plt
pygame.init()
clock = pygame.time.Clock()
WIN = pygame.display.set_mode((421, 500))
pygame.display.set_caption('number gusser')
FPS = 20
def PYtxt(txt: str, fontSize: int = 28, font: str = 'freesansbold.ttf', fontColour: tuple = (0, 0, 0)):
    return (pygame.font.Font(font, fontSize)).render(txt, True, fontColour)

WHITE = (215, 215, 215)
GREAY = (70, 70, 70)
BLACK = (0, 0, 0)
BLUE = (10, 40, 100)

checksClr = BLUE
boardClr = WHITE
txtClr = GREAY

def predict(board):
    image = []

    for row in board.cubes:
        for cube in row:
            if cube.colour == (0,0,0):
                image.append(1)
            else:
                image.append(0)

    # loading the model 
    # with open('model','rb') as f:
    #     model = pickle.load(f)

    # print(model.predict_proba([image]))
    # print(model.predict([image]))

    model = load_model('model.h5')
    print(np.argmax(model.predict([image])))

    


class Grid():
    def __init__(self, cols: int = 4, rows: int = 4, width: int = 400, height: int = 400,WIN = None):
        self.rows = cols
        self.cols = rows
        self.cubes = [
            [Cube(i, j, width, height, self.cols, self.rows,WIN)
             for j in range(self.cols)]
            for i in range(self.rows)
        ]
        self.width = width
        self.height = height
        self.win = WIN
        self.surface = pygame.Surface((self.width,self.height))
        self.surface.fill((255,255,255))
        self.draw()

    def draw(self):
        self.win.blit(self.surface,(0,0))
        rowGap = self.height / self.rows
        colGap = self.width / self.cols
        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw()
                
        for i in range(self.rows+1):
            pygame.draw.line(self.win, BLACK, (0, i*rowGap),(self.height, rowGap*i))
        for i in range(self.cols+1):
            pygame.draw.line(self.win, BLACK, (i*colGap, 0), (colGap*i, self.width))

        pygame.display.update()

    def clicked(self,pos):
        x,y = pos 
        if x >= self.rows or y >= self.cols or x < 0 or y< 0:
            return 0
        self.cubes[x][y].clicked()
        return 1
    def delete(self,pos):
        x,y = pos
        if x >= self.rows or y >= self.cols or x < 0 or y< 0:
            return 0

        self.cubes[x][y].delete()
        
        return 1
        

class Cube():
    def __init__(self, row, col, width, height, cols, rows,win):
        self.row,self.col = row,col

        self.width,self.height = width,height

        self.cols = cols
        self.rows = rows

        self.win = win
        global WHITE
        self.colour = WHITE

    def draw(self):
        rowGap = self.height / self.rows
        colGap = self.width / self.cols
        x = self.col * colGap
        y = self.row * rowGap
        pygame.draw.rect(self.win, self.colour, pygame.Rect(x+1, y+1, colGap-1, rowGap-1))
    
    def clicked(self):
        global BLACK
        self.colour = BLACK
        self.draw()
        pygame.display.update()

    def delete(self):
        self.colour = WHITE
        self.draw()
        pygame.display.update()


# 28 x 28
grid = Grid(cols = 28 , rows = 28,width = 420,height=420,WIN = WIN)

run = True
while run:
    clock.tick(FPS)
    if pygame.mouse.get_pressed()[0]:
        y,x = pygame.mouse.get_pos()
        gap = grid.width // grid.rows
        y //= gap
        x //= gap
        grid.clicked((x,y))
    elif pygame.mouse.get_pressed()[2]:
        y,x = pygame.mouse.get_pos()
        gap = grid.width // grid.rows
        y //= gap
        x //= gap
        grid.delete((x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                predict(grid)
pygame.quit()