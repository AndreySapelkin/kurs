# -*- coding: utf-8 -*-
import codecs


# класс локации лабиринта
class Location(object):
    def __init__(self, lw, uw):
        self.left_wall = lw
        self.up_wall = uw;


# класс лабиринта
class Maze(object):
    # конструктор по умолчанию
    def __init__(self):
        # высота лабиринта
        self.Height = 10
        # ширина лабиринта
        self.Width = 15
        # локации лабиринта
        self.Locs = [[Location for x in range(self.Height + 1)]
                     for y in range(self.Width + 1)]

    # вспомогательный метод, анализирующий наличие заданной комбинации
    # стен у левого верхнего угла локации
    def IsCombWalls(self, f1, f2, f3, f4, i, j):
        if (self.Locs[j - 1][i].up_wall == f1) and \
                (self.Locs[j][i - 1].left_wall == f2) and \
                (self.Locs[j][i].up_wall == f3) and \
                (self.Locs[j][i].left_wall == f4):
            return True
        else:
            return False

    # метод, генерирующий набор строк с текстовым представлением
    # лабиринта
    def GetLinesMaze(self):
        g = ["\u2500\u2500\u2500\u2500", "    "]
        v = ["\u2502   ", "\u2502   "]

        lt = ["\u250c\u2500\u2500\u2500", "\u2502   "]
        lc = ["\u251c\u2500\u2500\u2500", "\u2502   "]
        lb = ["\u2514\u2500\u2500\u2500", "    "]

        ct = ["\u252c\u2500\u2500\u2500", "\u2502   "]
        cc = ["\u253c\u2500\u2500\u2500", "\u2502   "]
        cb = ["\u2534\u2500\u2500\u2500", "    "]

        rt = ["\u2510   ", "\u2502   "]
        rc = ["\u2524   ", "\u2502   "]
        rb = ["\u2518   ", "    "]

        # создаем массив представления (на экране консоли) локаций лабиринта
        # для каждой локации - две строчки и еще дополнительные строка и
        # столбец для нижней и правой границ лабиринта
        c = [["    " for x in range(self.Width + 1)]
             for y in range((self.Height + 1) * 2)]

        # левый верхний угол лабиринта
        c[0][0] = lt[0]
        c[1][0] = lt[1]

        # верхняя строка лабиринта
        for j in range(1, self.Width):
            if (self.Locs[j][0].left_wall == True):
                c[0][j] = ct[0]
                c[1][j] = ct[1]
            else:
                c[0][j] = g[0]
                c[1][j] = g[1]

        # правый верхний угол лабиринта
        c[0][self.Width] = rt[0]
        c[1][self.Width] = rt[1]

        # крайний левый столбец лабиринта
        for i in range(1, self.Height):
            if (self.Locs[0][i].up_wall == True):
                c[2 * i][0] = lc[0]
                c[2 * i + 1][0] = lc[1]
            else:
                c[2 * i][0] = v[0]
                c[2 * i + 1][0] = v[1]

        # левый нижний угол лабиринта
        c[2 * self.Height][0] = lb[0]
        c[2 * self.Height + 1][0] = lb[1]

        # вывод основных локаций лабиринта
        for i in range(1, self.Height):
            for j in range(1, self.Width):
                if self.IsCombWalls(False, False, False, True, i, j) == True:
                    c[2 * i][j] = v[0];
                    c[2 * i + 1][j] = v[1]
                elif self.IsCombWalls(False, False, True, False, i, j) == True:
                    c[2 * i][j] = g[0];
                    c[2 * i + 1][j] = g[1]
                elif self.IsCombWalls(False, False, True, True, i, j) == True:
                    c[2 * i][j] = lt[0];
                    c[2 * i + 1][j] = lt[1]
                elif self.IsCombWalls(True, True, False, False, i, j) == True:
                    c[2 * i][j] = rb[0];
                    c[2 * i + 1][j] = rb[1]
                elif self.IsCombWalls(True, False, False, True, i, j) == True:
                    c[2 * i][j] = rt[0];
                    c[2 * i + 1][j] = rt[1]
                elif self.IsCombWalls(True, False, True, False, i, j) == True:
                    c[2 * i][j] = g[0];
                    c[2 * i + 1][j] = g[1]
                elif self.IsCombWalls(False, True, True, False, i, j) == True:
                    c[2 * i][j] = lb[0];
                    c[2 * i + 1][j] = lb[1]
                elif self.IsCombWalls(False, True, False, True, i, j) == True:
                    c[2 * i][j] = v[0];
                    c[2 * i + 1][j] = v[1]
                elif self.IsCombWalls(False, True, True, True, i, j) == True:
                    c[2 * i][j] = lc[0];
                    c[2 * i + 1][j] = lc[1]
                elif self.IsCombWalls(True, False, True, True, i, j) == True:
                    c[2 * i][j] = ct[0];
                    c[2 * i + 1][j] = ct[1]
                elif self.IsCombWalls(True, True, False, True, i, j) == True:
                    c[2 * i][j] = rc[0];
                    c[2 * i + 1][j] = rc[1]
                elif self.IsCombWalls(True, True, True, False, i, j) == True:
                    c[2 * i][j] = cb[0];
                    c[2 * i + 1][j] = cb[1]
                elif self.IsCombWalls(True, True, True, True, i, j) == True:
                    c[2 * i][j] = cc[0];
                    c[2 * i + 1][j] = cc[1]

        # вывод нижней строки лабиринта
        for i in range(1, self.Width):
            if (self.Locs[i][self.Height - 1].left_wall == True):
                c[2 * self.Height][i] = cb[0]
                c[2 * self.Height + 1][i] = cb[1]
            else:
                c[2 * self.Height][i] = g[0]
                c[2 * self.Height + 1][i] = g[1]

        # вывод крайнего правого столбца лабиринта
        for i in range(1, self.Height):
            if (self.Locs[self.Width - 1][i].up_wall == True):
                c[2 * i][self.Width] = rc[0]
                c[2 * i + 1][self.Width] = rc[1]
            else:
                c[2 * i][self.Width] = v[0]
                c[2 * i + 1][self.Width] = v[1]

        # правый нижний угол лабиринта
        c[2 * self.Height][self.Width] = rb[0]
        c[2 * self.Height + 1][self.Width] = rb[1]

        # формирование строк лабиринта
        s = ["" for x in range((self.Height + 1) * 2)]
        for i in range(self.Height + 1):
            for j in range(self.Width + 1):
                s[2 * i] += c[2 * i][j]
                s[2 * i + 1] += c[2 * i + 1][j]

        return s

    # напечатать лабиринт
    def PrintToConsole(self):
        s = self.GetLinesMaze()

        for i in range(self.Height + 1):
            print(s[2 * i])
            print(s[2 * i + 1])

    def GetLoc(self, i, j):
        return self.Locs[i][j];

    def SetLoc(self, i, j, lw, uw):
        self.Locs[i][j].left_wall = lw
        self.Locs[i][j].up_wall = uw

    def SetLocLeftWall(self, i, j, lw):
        self.Locs[i][j].left_wall = lw

    def SetLocUpWall(self, i, j, uw):
        self.Locs[i][j].up_wall = uw

    def GetWidth(self):
        return self.Width

    def GetHeight(self):
        return self.Height

    def SetSizes(self, w, h):
        self.Width = w
        self.Height = h

        self.Locs = [[Location(False, False) for x in range(self.Height + 1)]
                     for y in range(self.Width + 1)]

        for i in range(self.Width + 1):
            self.Locs[i][self.Height] = Location(False, True);

        for j in range(self.Height + 1):
            self.Locs[self.Width][j] = Location(True, False);

        self.Locs[self.Width][self.Height] = Location(False, False);











