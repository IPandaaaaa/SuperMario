import pygame
import config
import sys

def check_keyboard():
    for event in pygame.event.get():
        if event.type == sys.exit:
            exit()
 
    pressed_keys = pygame.key.get_pressed()
    
    if pressed_keys[pygame.K_RIGHT]:
        config.camera.pos.x += 1
    elif pressed_keys[pygame.K_LEFT]:
        config.camera.pos.x -= 1
    elif pressed_keys[pygame.K_q]:
        exit()