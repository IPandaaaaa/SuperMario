import os
import sys
import pygame

import config
import sprites
import camera
from basetypes import Vector2
import game_function as gf
import mario
import level_1_1

def run_game():
    pygame.init()
    config.screen = pygame.display.set_mode((config.SCREEN_SIZE.x, config.SCREEN_SIZE.y))
    pygame.display.set_caption(config.CAPTION)
    
    config.clock = pygame.time.Clock()
    config.camera = camera.Camera(Vector2(), config.SCREEN_SIZE.x, config.SCREEN_SIZE.y)
    config.mario = mario.Mario(config.MARIO_START_POSITION,36,48,Vector2(0,0))
    level = level_1_1 #从第一关开始
    config.static_colliders = level.static_colliders
    config.dynamic_colliders =level.dynamic_colliders

    while True:
        config.delta_time = config.clock.tick(60) #设置帧率
        gf.check_keyboard(level)#键盘响应
        gf.update_time()#刷新时间相关
        gf.update_screen()#刷新屏幕
        pygame.display.update()

if __name__ == '__main__':
    run_game()

    pygame.quit()