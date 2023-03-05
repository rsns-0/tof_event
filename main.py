from scripts.click_scripts import locate, locate_long, sleep_click as sclick
from time import sleep
from pathlib import Path
import json
import os

os.getcwd()

data_file = Path(__file__).parent/"resources/ui_data/final_data_file.json"
resource_path = Path(__file__).parent/"resources/images"
with open(data_file,'r') as f:
    json_data = json.load(f)

def img_path(file_name):
    return str(resource_path/file_name)

def main():
    d = json_data
    while True:
        gift_img_path=img_path(d['gift_sword_area']['file_name'])
        gift_coords = locate(gift_img_path)
        sclick(*gift_coords)
        sclick(d['half_ani_button'])
        ff_img_path=img_path(d['frost_flame_img']['file_name'])
        ff_coords = locate(ff_img_path)
        sclick(ff_coords)
        flame_icon_path = img_path(d['flame_icon_area']['file_name'])
        locate_long(flame_icon_path)
        locate_long(gift_img_path)

if __name__ == "__main__":
    main()
