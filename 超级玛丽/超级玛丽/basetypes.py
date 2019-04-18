import pygame
import math

import sprites

class Vector2():#二维向量
    """Vector class for 2D positions and velocities"""
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __mul__(self, other):
        """Overload multiplication"""
        return Vector2(self.x * other, self.y * other)

    def __add__(self, other):
        """Overload Addition"""
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Overload Addition"""
        return Vector2(self.x - other.x, self.y - other.y)

class Game_Object():
    '''所有的对象'''
    def __init__(self, pos, w, h):
        self.pos = pos
        self.w = w
        self.h = h

    def iscollided(self, other, dx, dy):
        #这个函数判断有没有碰撞
        #设self 为A ，other为B
        #设A的左上角坐标为p1，右下角坐标为p2，B的左上角坐标为p3，右下角坐标为p4，假设边重叠不算重叠
        #则没有重叠可以有四种情况
        #B在A上，p1.y >= p4.y
        #B在A下，p3.y >= p2.y
        #B在A左，p1.x >= p4.x
        #B在A右，p3.x >= p2.x
        #对上式取反，即为结果
        if (self.pos.y + dy < other.pos.y+other.h) and (other.pos.y < self.pos.y+self.h+dy) \
               and (self.pos.x +dx < other.pos.x+other.w ) and (other.pos.x < self.pos.x+self.w +dx):
            return other
        else:
            return None

    def iscollidedbywhichdir(self, other):
        # 已经判定移动后会撞到，判断撞到的方向是垂直还是水平还是斜着
        '''设self为A(mario)，other为B'''
        '''这个函数用来判断，B有哪几个点在A内
            借此来判断，是哪个方向撞到了
            A的四个点，逆时针旋转，分别命名为A1,A2,A3,A4
            B的四个点，逆时针旋转，分别命名为B1,B2,B3,B4
            将B的外围分为8个区域讨论
        '''
        if self.pos.y+self.h <= other.pos.y:#上面三个区域
            return 'up' #A在B上面
        elif  self.pos.y>=other.pos.y+other.h:#下面三个区域
            return  'down'#A在B下面
        elif self.pos.x+self.w <=other.pos.x:#左边一个区域
            return 'left'
        elif self.pos.x>=other.pos.x+other.w:#右边一个区域
            return 'right'

class DynamicCollision(Game_Object):
    '''会动的碰撞体'''
    def __init__(self, pos, w, h, vel):
        super().__init__(pos, w, h)
        self.vel = vel

class StaticCollision(Game_Object):
    '''静态碰撞体'''
    def __init__(self, pos, w, h):
        super().__init__(pos, w, h)

class State_Machine():
    """状态机,用来控制物体的状态，播放动画和调整速度等"""
    def __init__(self, initial_state):
        self.state = initial_state

    def change_state(self, newstate):
        self.state = newstate

    def get_state(self):
        return self.state