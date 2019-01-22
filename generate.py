# -*- coding: utf-8 -*-
from maze import *
from random import *

#вспомогательный класс
class Wall:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0


#класс алгоритмов генерации лабиринтов
class GenMaze:

    def __init__(self):
        return

    def BreakWall(self, maze, x, y, dx, dy):
        if (dx == -1):
            maze.SetLocLeftWall(x, y, False)
        elif (dx == 1):
            maze.SetLocLeftWall(x + 1, y, False)
        elif (dy == -1):
            maze.SetLocUpWall(x, y, False)
        else:
            maze.SetLocUpWall(x, y + 1, False)

    #генерация лабиринта методом Прима
    def GenPrime(self, maze):

        w = maze.GetWidth()
        h = maze.GetHeight()

        #изначально все стены существуют
        for i in range(w):
            for j in range(h):
                maze.SetLoc(i, j, True, True)

        #изначально все атрибуты - O (Outside)
        AtribLocs = [[ "O" for x in range(h)] for y in range (w)]

        #выбираем начальную локацию и присваиваем ей атрибут I (Inside)
        x = randint(1,w-1);
        y = randint(1,h-1);
        AtribLocs[x][y] = "I";

        #локациям, граничным с начальной, присваиваем атрибут B (Border)
        xc = 0
        yc = 0
        dx = [ 1, 0, -1, 0 ]
        dy = [ 0, -1, 0, 1 ]
        for i in range(4):
            xc = x + dx[i]
            yc = y + dy[i]
            if ((xc >= 0) and (yc >= 0) and (xc < w) and (yc < h)):
                AtribLocs[xc][yc] = "B";

        IsEnd = False
        counter = 0
        xloc = 0
        yloc = 0

        while (IsEnd == False):
            IsEnd = True
            counter = 0
            for i in range(w):
                for j in range(h):
                    if (AtribLocs[i][j] == "B"):
                        counter += 1

            counter = randint(1, counter)

            for i in range(w):
                for j in range(h):
                     if (AtribLocs[i][j] == "B"):
                         counter -= 1
                         if (counter == 0):
                                xloc = i
                                yloc = j
                                break
                if (counter == 0):
                    break

            AtribLocs[xloc][yloc] = "I"

            counter = 0;

            for i in range(4):
                xc = xloc + dx[i]
                yc = yloc + dy[i]
                if ((xc >= 0) and (yc >= 0) and (xc < w) and (yc < h)):
                    if (AtribLocs[xc][yc] == "I"):
                        counter += 1
                    if (AtribLocs[xc][yc] == "O"):
                        AtribLocs[xc][yc] = "B"

            counter = randint(1,counter)
            for i in range(4):
                xc = xloc + dx[i]
                yc = yloc + dy[i]
                if ((xc >= 0) and (yc >= 0) and (xc < w) and (yc < h) and (AtribLocs[xc][yc] == "I")):
                    counter -= 1;
                    if (counter == 0):
                        self.BreakWall(maze, xloc, yloc, dx[i], dy[i])
                        break

            for i in range(w):
                for j in range(h):
                     if (AtribLocs[i][j] == "B"):
                         IsEnd = False
                         break
                if (IsEnd == False):
                    break
                 

        maze.PrintToConsole();

    #можно ли пройти из локации (x,y) в локацию (x+dx,y+dy)
    def CanGo(self, maze, x, y, dx, dy):
        if (dx == -1):
            return not maze.GetLoc(x, y).left_wall
        elif (dx == 1):
            return not maze.GetLoc(x + 1, y).left_wall
        elif (dy == -1):
            return not maze.GetLoc(x, y).up_wall
        else:
            return not maze.GetLoc(x, y + 1).up_wall


    #ответ на вопрос - существует ли путь между локациями (xs, ys) и (xf, yf) 
    #методом волновой трассировки (необходмо для генерации лабиринта методом Краскала)
    def WaveTracingSolve(self, maze, xs, ys, xf, yf):
        dx = [ 1, 0, -1, 0 ]
        dy = [ 0, -1, 0, 1 ]

        N = 1;

        w = maze.GetWidth()
        h = maze.GetHeight()

        Mark = [[ 0 for x in range(h)] for y in range (w)]
        
        Mark[xs][ys] = 1
            
        no_sol = False
        while (no_sol == False):
            no_sol = True;
            for i in range(w):
                for j in range(h):
                    if (Mark[i][j] == N):
                        for k in range(4):
                            if ((self.CanGo(maze, i, j, dx[k], dy[k])) and 
                                    (Mark[i + dx[k]][j + dy[k]] == 0)):
                                no_sol = False
                                Mark[i + dx[k]][j + dy[k]] = N + 1
                                if (((i + dx[k]) == xf) and ((j + dy[k])==yf)):
                                    return True;
            N += 1
        return False;

    #генерация лабиринта методом Краскала
    def GenKruskal(self, maze):

        w = maze.GetWidth()
        h = maze.GetHeight()
        n = (w - 1) * h + w * (h - 1)
        
        Walls = [Wall() for x in range(n)]

        #изначально все стены существуют
        for i in range(w):
            for j in range(h):
                maze.SetLoc(i, j, True, True)

        counter = 0;
        for i in range(1,w):
            for j in range(h):
                Walls[counter].x = i
                Walls[counter].y = j
                Walls[counter].dx = -1
                Walls[counter].dy = 0
                counter += 1

        for i in range(w):
            for j in range(1, h):
                Walls[counter].x = i
                Walls[counter].y = j
                Walls[counter].dx = 0
                Walls[counter].dy = -1
                counter += 1

        tempw = Wall();
        for k in range(10*n):
            i = randint(0,n-1)
            j = randint(0,n-1)
            tempw = Walls[i]
            Walls[i] = Walls[j]
            Walls[j] = tempw

        locations = w * h
        ii = 0
        while (locations > 1):
            tempw = Walls[ii]
            ii += 1
            if (self.WaveTracingSolve(maze, tempw.x, tempw.y, tempw.x + tempw.dx, tempw.y + tempw.dy)==False):
                self.BreakWall(maze, tempw.x, tempw.y, tempw.dx, tempw.dy)
                locations -= 1

        maze.PrintToConsole();