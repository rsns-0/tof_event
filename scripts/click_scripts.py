import pyautogui as pa
from time import sleep
import logging


class NotFoundException(Exception):
    ...

class TriesExhausted(Exception):
    ...


def retry(fn):
    def wrap(*args, tries=3, time_to_sleep=5, expect_value=True, **kwargs):
        try:
            result = fn(*args, **kwargs)
            if expect_value:
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
            if tries <= 0:
                raise TriesExhausted("Out of tries.")
            sleep(time_to_sleep)
            return wrap(
                tries=tries - 1,
                time_to_sleep=time_to_sleep,
                expect_value=expect_value,
                *args,
                **kwargs,
            )

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
