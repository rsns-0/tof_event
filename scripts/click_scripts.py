import pyautogui as pa
from time import sleep
from retry import retry
from retry.api import retry_call
from configs import click_config as cfg
import logging
logging.basicConfig(level=logging.INFO)
log1 = logging.getLogger("click_scripts_logger")
from pyscreeze import Point

class NotFoundException(Exception):
    ...




@retry(tries=3,delay=5,exceptions=NotFoundException)
def valreturn_img(img_path:str, region:tuple[int,int,int,int], confidence:float=cfg.confidence, **kwargs):
    """valreturn_img Checks if image exists then returns its coordinates (which you can optionally use for next click command).
    There should be a retry decorator attached to function definition which will retry the search if the image is not found within the specified amount of tries and delay in decorator args.

    Args:
        img_path (str): Full or relative path to the image file.
        region (tuple[int,int,int,int]): Area to look for the images. First two ints are the coordinates of the top left corner of the region. Second two are the width and height.
        confidence (float, optional): Lower is higher chance of false positive. Higher is higher chance of false negative. Defaults to cfg.confidence.

    Raises:
        NotFoundException: When the image cannot be found anywhere. Could be that the region to search in is wrong or confidence is too high.

    Returns:
        Point: Coordinates to the image on screen.
    """
    if result := pa.locateCenterOnScreen(img_path, region=region, confidence=confidence, **kwargs):
        return result
    raise NotFoundException(
        f"""
        Tried searching for {img_path} and it was not found at this time.
        It may not be in the specified region of {region}.
        Or, the confidence parameter is too high ({confidence})
        Check if the game window is open and unobstructed.
        """
        )


@retry(tries=10,delay=60,exceptions=NotFoundException)
def valreturn_long(img_path:str, region:tuple[int,int,int,int], confidence:float=cfg.confidence, **kwargs) -> Point:
    """Retry decorator time is modified for longer duration, otherwise same as original."""
    if result := pa.locateCenterOnScreen(img_path, region=region, confidence=confidence, **kwargs):
        return result
    raise NotFoundException(
        f"""
        Tried searching for {img_path} and it was not found at this time.
        It may not be in the specified region of {region}.
        Or, the confidence parameter is too high ({confidence})
        Check if the game window is open and unobstructed.
        """
        )


def sleep_click(coordinates:Point|None=None, sleep_time=cfg.sleep_click_default) -> None:
    """Clicks at current position if no coordinates are passed. Sleeps for specified time afterwards."""
    pa.click(coordinates) if coordinates else pa.click()
    sleep(sleep_time)
