from os import path
import pygame as pg
from PIL import Image

graphics_folder = path.join(path.dirname(__file__), 
'resources', 'graphics')

#加载资源
tile_set = pg.image.load(path.join(graphics_folder, 'tile_set.png'))
tile_set_flipped = pg.image.load(path.join(graphics_folder, 'tile_set_flipped.png'))
text_image = pg.image.load(path.join(graphics_folder, 'text_image.png'))
background = pg.image.load(path.join(graphics_folder, 'background.png'))
foreground = pg.image.load(path.join(graphics_folder, 'foreground.png'))
menu = pg.image.load(path.join(graphics_folder, 'menu.png'))
digits = pg.image.load(path.join(graphics_folder, 'digits.png'))
level_1_img = Image.open(path.join(graphics_folder, 'map.png'))

#提取坐标
#第一行
BRICK = (0, 0, 48, 48)#普通砖头
Q_BLOCK_OPEN = (48, 0, 48, 48)#问号砖头被撞完
Q_BLOCK_CLOSED = [#问好砖头被撞动画
    (96, 0, 48, 48),
    (144, 0, 48, 48),
    (192, 0, 48, 48)
]
BRICK_FRAGMENT = [#砖头被撞碎
    (252, 12, 24, 24),
    (300, 12, 24, 24)
]
FLAG = (336, 0, 48, 48)#旗
SELECTOR = (394, 12, 24, 24)#选择图标

#第二行
GOOMBA_RUN = [#GOOMRA
    (0, 48, 48, 48),
    (48, 48, 48, 48)
]
GOOMBA_SQUISHED = (96, 48, 48, 48)
GOOMBA_KNOCKED = (144, 48, 48, 48)
SUPER_MUSHROOM = (192, 48, 48, 48)#变大的蘑菇
EMPTY_SPRITE = (240, 48, 48, 48)

#第三行
TURTLE = [
    (0, 96, 48, 72),
    (48, 96, 48, 72)
]
TURTLE_SHELL = (96, 126, 48, 42)
COIN = [
    (144, 126, 48, 42),
    (192, 126, 48, 42),
    (240, 126, 48, 42),
    (288, 126, 48, 42)
]

#第四行
SMALL_MARIO_RUN = [
    (0, 168, 48, 48),
    (48, 168, 48, 48),
    (96, 168, 48, 48)
]
SMALL_MARIO_BRAKE = (150, 168, 40, 48)
SMALL_MARIO_JUMP = (192, 168, 48, 48)
DEAD_MARIO = (243, 168, 42, 42)
SMALL_MARIO_IDLE = (294, 168, 36, 48)
SMALL_MARIO_POLE = [
    (342 ,168, 39, 48),
    (380, 168, 39, 48)
]

#第五行
BIG_MARIO_RUN = [
    (0, 216, 48, 96),
    (48, 216, 48, 96),
    (96, 216, 48, 96)
]
BIG_MARIO_BRAKE = (144, 216, 48, 96)
BIG_MARIO_JUMP = (192, 216, 48, 96)
MARIO_CROUCH = (240, 246, 48, 66)
BIG_MARIO_IDLE = (289, 216, 48, 96)
WIN_SPRITES_BIG = [
    (339, 216, 48, 96),
    (387, 216, 48, 96)
]
WIN_SPRITES_SMALL = [
    (339, 168, 42, 48),
    (390, 168, 42, 48)
]#？？

#第六行
MARIO_SWIM = (0, 311, 48, 88)
MIDDLE_MARIO_IDLE = (48, 327, 48, 72)

GROW_SPRITES = [#变大的过程
    SMALL_MARIO_IDLE,
    MIDDLE_MARIO_IDLE,
    BIG_MARIO_IDLE
]

SHRINK_SPRITES = [#变小的过程
    MARIO_SWIM,
    EMPTY_SPRITE,
    SMALL_MARIO_IDLE
]









    