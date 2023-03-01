from scripts.click_scripts import locate, locate_long, sleep_click as click
from time import sleep



def main():
    d = {}
    while True:
        locate(d['gift_box'])
        click(d['gift_box_coordinates]'])
        click(d['half_anniversary_party_coordinates'])
        locate(d['frost_and_flame_title'])
        click(d['match'])
        locate_long(d['fire_icon'])
        sleep(180)
        locate_long(d['gift_box'])

if __name__ == "__main__":
    main()
