import pyautogui as pa
from decorator import decorator
from time import sleep
import logging

class NotFoundException(Exception):
    ...

@decorator
def retry(fn, tries=3, time_to_sleep=5, expect_value=True, *args, **kwargs):
    tries_remaining=tries
    while tries_remaining>0:
        try:
            result = fn(*args, **kwargs)
            if expect_value==True:
                if not result: raise NotFoundException(f'Function returned false value. Details: Fn:{fn.__name__}, Arg:{args}, Kwarg:{kwargs} ')
            return result
        except NotFoundException as e:
            logging.warn(f"{fn.__name__} failed, trying again after {time_to_sleep} seconds. Tries remaining: {tries_remaining}", exc_info=True)
            sleep(time_to_sleep)
            tries_remaining-=1

@retry
def locate(img_path, conf=0.95, **kwargs):
    return pa.locateOnScreen(img_path, confidence=conf, **kwargs)

@retry(time_to_sleep=30, tries=3)
def locate_long(img_path, conf=0.95, **kwargs):
    pa.locateOnScreen(img_path, confidence=conf, **kwargs)

def sleep_click(coordinates=None, sleep_time=1):
    pa.click(coordinates)
    sleep(sleep_time)
