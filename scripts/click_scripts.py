import pyautogui as pa
from time import sleep
from retry import retry
from configs import click_config as cfg
import logging
logging.basicConfig(level=logging.INFO)
log1 = logging.getLogger("click_scripts_logger")

class NotFoundException(Exception):
    ...


@retry(tries=3,delay=5,exceptions=NotFoundException)
def locate(img_path, conf1=cfg.confidence, **kwargs):
    if not kwargs.get('region'):
        log1.info('Region was not passed in to locate function.')
        raise NotImplementedError('Region was not passed in to locate function.')
    if result := pa.locateCenterOnScreen(img_path, confidence=conf1, **kwargs):
        return result
    raise NotFoundException("Value was null.")


@retry(tries=10,delay=60,exceptions=NotFoundException)
def locate_long(img_path, conf1=cfg.confidence, **kwargs):
    return locate(img_path, confidence=conf1, **kwargs)


def sleep_click(coordinates=None, sleep_time=1):
    pa.click(coordinates)
    sleep(sleep_time)
