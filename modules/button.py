import pygame
import pygame.locals as pl
import sys
import os


class Button():
    def __init__(self, screen, x_u, y_u, x_d, y_d, bg_color, font_color, font_path):
        self.screen = screen

