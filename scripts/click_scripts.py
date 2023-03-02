import pyautogui as pa
from time import sleep
import logging
from retry import retry


class NotFoundException(Exception):
    ...

class TriesExhausted(Exception):
    ...


@retry(tries=3,delay=5,exceptions=NotFoundException)
def locate(img_path, conf=0.95, **kwargs):
    result = pa.locateOnScreen(img_path, confidence=conf, **kwargs)
    if not result:
        raise NotFoundException("Value was null.")


@retry(tries=5,delay=30,exceptions=NotFoundException)
def locate_long(img_path, conf=0.95, **kwargs):
    return locate(img_path, conf=0.95, **kwargs)


def sleep_click(coordinates=None, sleep_time=1):
    pa.click(coordinates)
    sleep(sleep_time)
