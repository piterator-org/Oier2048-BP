import os
import sys
import json
import modules.skin
import platform
import pygame
import pygame.locals as PL


## read config file
# read skin
skin = modules.skin.Skin(
    modules.skin.read_cfg()
)


# initial screen
pygame.init()
screen = pygame.display.set_mode((800, 600), 0)
pygame.display.set_caption("Oier2048 by Pygame version 0.0.1")


def check_events():
    '''检查并响应事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 退出
            sys.exit(0)

def mainloop():
    while True:
        # 重绘屏幕
        screen.fill(skin.cb.bg_color)

        # 检查事件
        check_events()

        # 可见最近屏幕
        pygame.display.flip()

mainloop()