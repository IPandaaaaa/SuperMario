from basetypes import Vector2
import pygame as pg

#共享变量
screen = None
clock = None
camera = None
delta_time = None 
mario = None

#颜色
BLACK = (0, 0, 0, 255)
RED = (255, 0, 0, 255)
GRAY = (100, 100, 100, 255)
YELLOW = (255, 255, 0, 255)
GREEN = (100, 255, 100, 255)
BROWN = (124, 66, 0, 255)
PURPLE = (124, 0, 255, 255)

#背景色
BACKGROUND_COLOR = (107, 140, 255)

#窗口设置
SCREEN_SIZE = Vector2(744, 672)
CAPTION = 'Mario Bros'

#开始位置
MARIO_START_POSITION = Vector2(138, 552)
FOREGROUND_POS = Vector2(9840, 505)
TILE_SIZE = 48
