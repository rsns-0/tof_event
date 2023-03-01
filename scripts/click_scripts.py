import pyautogui as pa
from time import sleep
import logging


class NotFoundException(Exception):
    ...


def retry(fn):
    def wrap(*args, **kwargs):
        tries = 3
        time_to_sleep = 5
        expect_value = False
        while tries > 0:
            try:
                result = fn(*args, **kwargs)
                if expect_value == True:
                    if not result:
                        raise NotFoundException(
                            f"Function returned false value. Details: Fn:{fn.__name__}, Arg:{args}, Kwarg:{kwargs} "
                        )
                return result
            except NotFoundException:
                logging.warn(
                    f"{fn.__name__} failed, trying again after {time_to_sleep} seconds. Tries remaining: {tries}",
                    exc_info=True,
                )
                sleep(time_to_sleep)
                tries -= 1
    return wrap


@retry
def locate(img_path, conf=0.95, **kwargs):
    return pa.locateOnScreen(img_path, confidence=conf, **kwargs)


@retry
def locate_long(img_path, conf=0.95, **kwargs):
    sleep(30)
    pa.locateOnScreen(img_path, confidence=conf, **kwargs)


def sleep_click(coordinates=None, sleep_time=1):
    pa.click(coordinates)
    sleep(sleep_time)
