from basetypes import Vector2
import pygame as pg

#共享变量
screen = None
clock = None
camera = None
delta_time = None #两次刷新之间的时间差
mario = None
timer = 0 #计时器，单位为秒

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

#摄像头和马里奥的最大距离
MAX_DIS_CAMERA_TO_MARIO = 300
#摄像头能达到的最远距离
MAXIMUM_CAMERA_SCROLL = 9300

#获取所有的键盘输入信息
KEYS = None

#物理引擎设置
MAX_MARIO_SPEED = 0.35
MARIO_ACCELERATION = 0.0005
FRICTION = 0.7#摩擦加速度系数
BRAKE_FRICTION = 1.2#刹车加速度系数
MAX_MARIO_JUMP_VEL = 0.3 #马里奥能达到的最大上升速度
MARIO_JUMP_START_ACCELERATION=0.05#马里奥跳跃的初始加速度
MARIO_JUMP_ACCELERATION = 0.0005 #马里奥跳跃持续加速度
GRAVITYACCELERATION = 0.002 #马里奥重力加速度

#不会动的碰撞体
static_colliders = []

#会动的碰撞体
dynamic_colliders = []




