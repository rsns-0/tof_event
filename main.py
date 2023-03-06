from pyscreeze import Point
from scripts.click_scripts import (
    valreturn_img,
    valreturn_long,
    sleep_click,
)
from pathlib import Path
import json
import logging

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("tof_event_log")
from configs import click_config as cfg, dev_config as dcfg

# =========== Setup

def get_img_path(file_name) -> str:
    """Returns the path to the resource folder. Meant to be used from top level only."""
    resource_path:Path = Path(__file__).parent / "resources/images"
    return str(resource_path/file_name)

data_file_path:Path = Path(__file__).parent / f"resources/ui_data/{dcfg.data_file_name}"

with open(data_file_path, "r") as f:
    ui_data:dict = json.load(f)

# =========== Setup End

# ============= UI Data
gift_img_path: str = get_img_path(ui_data["gift_sword_area"]["file_name"])
gift_img_region: tuple[int, int, int, int] = ui_data["gift_sword_area"]["region"]

half_ani_X: int = ui_data['half_ani_button']['coordinates_X']
half_ani_Y: int = ui_data['half_ani_button']['coordinates_Y']
half_ani_point:Point = Point(x=half_ani_X,y=half_ani_Y)

ff_img_path: str = get_img_path(ui_data["frost_flame_img"]["file_name"])
ff_img_region:tuple[int,int,int,int] = ui_data["frost_flame_region"]["region"]

match_X: int = ui_data['match_button']['coordinates_X']
match_Y: int = ui_data['match_button']['coordinates_Y']
match_point:Point = Point(x=match_X,y=match_Y)

flame_icon_path:str = get_img_path(ui_data["flame_icon_area"]["file_name"])
flame_icon_region:tuple[int,int,int,int] = ui_data["flame_icon_area"]["region"]


# ============== Ui Data End


def main():

    while True:
        # Check gift box exists on startup, then click giftbox -> half anniversary party
        gift_coords: Point = valreturn_img(gift_img_path, region=gift_img_region)
        sleep_click(gift_coords)
        sleep_click(half_ani_point)
        
        #Check that frost flame banner exists, then click on match
        valreturn_img(ff_img_path, region=ff_img_region)
        sleep_click(match_point)
        
        #Poll every minute to see if in event, then poll every minute to see if out in field again.
        valreturn_long(flame_icon_path, region=flame_icon_region)
        valreturn_long(gift_img_path, region=gift_img_region)


if __name__ == "__main__":
    main()
