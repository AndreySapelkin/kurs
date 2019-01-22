# -*- coding: utf-8 -*-

from maze import *
from generate import *

maze = Maze()
gm = GenMaze()

while (True):
    print("Главное меню:")
    print("Выберите действие из списка(введите одну из буквенных команд):")
    print("gp  - генерация лабиринта методом Прима")
    print("gk  - генерация лабиринта методом Краскала")
    print("q   - выход из программы")
    c = input()

    if (c == "gp"):
        print("Введите длину лабиринта:")
        w = int(input())
        print("Введите ширину лабиринта:")
        h = int(input())
        maze.SetSizes(w, h)
        gm.GenPrime(maze)
        print("Лабиринт сгенирирован методом Прима!")

    if (c == "gk"):
        print("Введите длину лабиринта:")
        w = int(input())
        print("Введите ширину лабиринта:")
        h = int(input())
        maze.SetSizes(w, h)
        gm.GenKruskal(maze)
        print("Лабиринт сгенирирован методом Краскала!")

    if (c == "q"):
        print("Выход из программы!")
        break
