import pyautogui
from pyscreeze import Point
from scripts.click_scripts import (
    valreturn_img,
    valreturn_long,
    sleep_click,
)
from pathlib import Path
import logging
import time

import os

top_directory: Path = Path(__file__).parent

os.chdir(top_directory)

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("tof_event_log")
from configs import click_config as cfg, dev_config as dcfg

# =========== Setup


def make_region(int1, int2, int3, int4) -> tuple[int, int, int, int]:
    return (int1, int2, int3 - int1, int4 - int2)



# =========== Setup End

# ============= UI Data

quest_marker_png: str = str(Path(__file__).parent /"resources/images/quest_marker.png")
quest_marker_region: tuple[int, int, int, int] = make_region(2233, 225, 2494, 436)
survivors_png: str = str(Path(__file__).parent / "resources/images/survivors.png")
survivors_region: tuple[int, int, int, int] = make_region(764, 245, 1227, 598)
half_anni_coords:Point = Point(1768, 1183)
punch_event_coords:Point = Point(2472, 1017)
match_coords:Point = Point(2070, 1032)

# ============== Ui Data End


def main():
    while True:
        # Check quest marker exists on startup, then open event by alt+1 -> half anniversary party -> punch event -> match
        time.sleep(2)
        valreturn_img(quest_marker_png, region=quest_marker_region)
        time.sleep(1)
        with pyautogui.hold("alt"):
            pyautogui.press("1")
        time.sleep(2)
        sleep_click(half_anni_coords)
        time.sleep(1)
        sleep_click(punch_event_coords)
        sleep_click(match_coords)

        # Poll every minute to see if in event, then poll every minute to see if out in field again. Click once out in field to allow alt+1 to work for opening event menu.
        valreturn_long(survivors_png, region=survivors_region)
        valreturn_long(quest_marker_png, region=quest_marker_region)
        time.sleep(2)
        logger.debug("restarting loop")
        pyautogui.click()


if __name__ == "__main__":
    main()
