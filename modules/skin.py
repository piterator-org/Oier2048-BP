import os
import sys
import json
import platform
import pygame
import pygame.locals as PL


def read_cfg():
    '''
    -> dict
    '''
    skin_path = os.path.join(
        os.path.abspath("."), 
        "config",
        "skin.json"
    )
    return json.load(open(skin_path, "r"))


def read_path(skin_cfg: dict):
    PATH = skin_cfg["dir"][:]
    dir_work = os.path.abspath(".")
    for item in PATH:
        dir_work = os.path.join(dir_work, item)
    return dir_work


def read_cb(skin_cfg: dict):
    skin_name = skin_cfg["skin"] + ".json"
    skin_path = os.path.join(read_path(skin_cfg), skin_name)
    _Skin = json.load(open(skin_path, "r"))
    return Color_Board(
        tuple(_Skin["1"]), tuple(_Skin["2"]), tuple(_Skin["4"]), tuple(_Skin["8"]),
        tuple(_Skin["16"]), tuple(_Skin["32"]), tuple(_Skin["64"]), tuple(_Skin["128"]),
        tuple(_Skin["256"]), tuple(_Skin["512"]), tuple(_Skin["1024"]), tuple(_Skin["2048"]),
        tuple(_Skin["background"])
    )

class Color_Board():
    def __init__(self, color1: tuple, color2: tuple,
                 color4: tuple, color8: tuple, color16: tuple,
                 color32: tuple, color64: tuple, color128: tuple,
                 color256: tuple, color512: tuple, color1024: tuple,
                 color2048: tuple, bg_color: tuple):
        self.color1 = color1
        self.color2 = color2
        self.color4 = color4
        self.color8 = color8
        self.color16 = color16
        self.color32 = color32
        self.color64 = color64
        self.color128 = color128
        self.color256 = color256
        self.color512 = color512
        self.color1024 = color1024
        self.color2048 = color2048
        self.bg_color = bg_color

    def random_color(self):
        pass


class Skin():
    def __init__(self, skin_cfg: dict):
        self.skin_cfg = skin_cfg
        self.cb = read_cb(skin_cfg)

    def change_skin(self, skin_name: str):
        pass
