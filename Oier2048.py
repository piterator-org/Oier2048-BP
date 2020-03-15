import os
import sys
import json
import modules.skin
import modules.button
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

# initial global args
global lable_list
lable_list = []
global button_list
button_list = []

## debug option
if '--debug' in sys.argv:
    # lable test
    lable_list.append(modules.button.Lable(
        modules.button.Rect_Setting(100, 100, 100, 100),
        screen, (100, 200, 100), 'Test', (250, 200, 70),
        24, 'Fira code'
    ))


def check_events():
    '''检查并响应事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 退出
            sys.exit(0)


def update_screen(screen, lables: list, buttons: list, board=None):
    # 重绘屏幕
    screen.fill(skin.cb.bg_color)
    for lable in lables:
        lable.draw()
    for button in buttons:
        button.draw()
    if board is not None:
        board.draw()


def mainloop():
    while True:
        update_screen(screen, lable_list, button_list, None)

        # 检查事件
        check_events()

        # 可见最近屏幕
        pygame.display.flip()


mainloop()
