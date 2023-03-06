from pyscreeze import Point
import pytest
from scripts.click_scripts import *
from pathlib import Path
import pyautogui as pa

from scripts.click_scripts import locate, locate_long, sleep_click as sclick
import json
import os

# def test_retry():
#     with pytest.raises(NotFoundException) as excinfo:
#         path = Path(__file__).parent / "test_resources/quest_marker.png"
#         qimg = str(path)
#         top_left = (2243,223)
#         bot_right = (2542,474)
#         width = bot_right[0]-top_left[0]
#         height = bot_right[1]-top_left[1]
#         regionparam = (top_left[0], top_left[1], width, height)
#         quest_marker_coords = locate(qimg, region=regionparam)


def test_image_locate():
    path = Path(__file__).parent / "test_resources/vsicon.png"
    assert type(str(path)) is str


def test_coords_value_is_point():
    # must have vs code in full screen
    path = Path(__file__).parent / "test_resources/vsicon.png"
    coords = locate(img_path=str(path), confidence = 0.5, region=(0,0,250,250))
    assert type(coords) is Point

def test_mouse_coords_matches():
    # must have vs code in full screen
    path = Path(__file__).parent / "test_resources/vsicon.png"
    coords = locate(str(path), confidence = 0.5, region=(0,0,250,250))
    pa.moveTo(coords)
    mousecoords = pa.position()
    assert mousecoords == coords

def test_able_to_locate_gift_box():
    # must place the image near top left of screen
    path = Path(__file__).parent / "test_resources/gift_sword_area.png"
    coords = locate(str(path), confidence = 0.5, region=(0,0,500,500))
    pa.moveTo(coords)
    mousecoords = pa.position()
    assert mousecoords == coords

def test_able_to_locate_flame_icon():
    # must place the image near top left of screen
    path = Path(__file__).parent / "test_resources/flame_icon_area.png"
    coords = locate(str(path), confidence = 0.5, region=(0,0,500,500))
    pa.moveTo(coords)
    mousecoords = pa.position()
    assert mousecoords == coords
    