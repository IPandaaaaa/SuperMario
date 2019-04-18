import pygame
import config
import sys
import sprites


def check_keyboard(level):
    for event in pygame.event.get():
        if event.type == sys.exit:
            exit()
 
    config.KEYS = pygame.key.get_pressed()#获取键盘输入
    if config.KEYS[pygame.K_q]:
        exit()
    config.mario.responce_to_keyboard(level)#马里奥根据键盘输入执行响应动作
    config.camera.update(config.mario)#camera跟着马里奥走

def update_time():
    """处理时间相关的事件"""
    config.timer += config.delta_time

def update_screen():
    '''刷新屏幕'''
    config.screen.fill(config.BACKGROUND_COLOR)#刷新背景
    config.screen.blit(sprites.background, (0, 0), #根据摄像头的位置绘制背景图
                       (config.camera.pos.x, config.camera.pos.y, config.SCREEN_SIZE.x, config.SCREEN_SIZE.y))
    for collider in config.dynamic_colliders:
        collider.blitme(config.screen)
    config.mario.blitme(config.camera)#画马里奥
