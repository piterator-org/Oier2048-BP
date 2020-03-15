import pygame
import pygame.locals as pl
import sys
import os


class Rect_Setting():
    def __init__(self, left: int, top: int, width: int, height: int):
        self.left = left
        self.top = top
        self.width = width
        self.height = height


class Lable():
    '''
    A simple lable contain a rectangle and text
    '''

    def __init__(self, rect_setting: Rect_Setting, screen,
                 color: tuple, text: str, text_color: str, 
                 text_size: int, font: str):
        '''
        Inialize the lable
        '''
        self.color = color
        self.screen = screen
        self.text = text
        self.text_color = text_color
        self.font = font
        self.text_size = text_size
        self.rect_setting = rect_setting
        self.init_rect()

    def init_rect(self):
        '''
        initialize the lable rect and text as img rect
        '''
        self.rect = pygame.Rect(
            self.rect_setting.left, self.rect_setting.top,
            self.rect_setting.width, self.rect_setting.height
        )
        self.text_img = pygame.font.SysFont(
            self.font, self.text_size).render(
                self.text, True, self.text_color
        )
        self.text_rect = self.text_img.get_rect()
        self.text_rect.center = self.rect.center
    
    def draw(self):
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.text_img, self.text_rect)

class Button():
    '''
    A simple button contain a lable and a event
    And the active color.
    '''
    def __init__(self, screen, lable: Lable, event,
                 status: bool, active_color: tuple):
        self.lable = lable
        self.event = event
        self.status = status
        self.normal_color = self.lable.color
        self.active_color = active_color
    
    def draw(self):
        if self.status is True:
            self.lable.color = self.active_color
            self.lable.draw()
        else:
            slef.lable.color = self.normal_color
            self.lable.draw()
