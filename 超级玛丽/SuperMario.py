import os
import sys
import pygame

import config
import sprites
import camera
from basetypes import Vector2
import game_function as gf

def run_game():
    pygame.init()
    config.screen = pygame.display.set_mode((config.SCREEN_SIZE.x, config.SCREEN_SIZE.y))
    pygame.display.set_caption(config.CAPTION)
    
    config.clock = pygame.time.Clock()
    config.camera = camera.Camera(Vector2(), config.SCREEN_SIZE.x, config.SCREEN_SIZE.y)
    
    while True:
        config.delta_time = config.clock.tick() #设置帧率
        gf.check_keyboard()
        config.screen.fill(config.BACKGROUND_COLOR)
        config.screen.blit(sprites.background, (0,0),
                (config.camera.pos.x,config.camera.pos.y,config.SCREEN_SIZE.x, config.SCREEN_SIZE.y))
        pygame.display.update()

if __name__ == '__main__':
    run_game()