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

## initial global args
# lable and button list
global lable_list
lable_list = []
global button_list
button_list = []
# msg lable

## debug option
# debug tool lable
debug_lable = modules.button.Lable(
            modules.button.Rect_Setting(400, 400, 300, 50),
            screen, (212, 121, 117), "Debug successfully",
            (181, 90, 37), 15, "Fira code" 
        )
def create_debug_lable(screen):
    lable_list.append(debug_lable)
def remove_debug_lable(screen):
    if debug_lable in lable_list:
        del lable_list[lable_list.index(debug_lable)]

if '--debug' in sys.argv:
    # button test
    button_list.append(modules.button.Button(
        screen, modules.button.Lable(
            modules.button.Rect_Setting(
                100, 100, 200, 50
            ), screen, (100, 200, 50), "Test button", 
            (50, 100, 50), 20, "Fira code"
        ), create_debug_lable, False, (37, 181, 99),
        remove_debug_lable
    ))

## game functions
# check keydown, click down events
def check_events():
    '''检查并响应事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 退出
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_x, click_y = pygame.mouse.get_pos()
            for button in button_list:
                if button.lable.rect.collidepoint(click_x, click_y):
                    button.status = True
                    button.event(screen)
                else:
                    button.status = False
                    button.unevent(screen)


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
