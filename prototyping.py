import pyautogui as pa
from scripts.click_scripts import locate

def main():
    
    top_left = (2243,223)
    bot_right = (2542,474)
    width = bot_right[0]-top_left[0]
    height = bot_right[1]-top_left[1]
    regionparam = (top_left[0], top_left[1], width, height)
    print(regionparam)
    quest_marker_coords = locate("quest_marker.png", region=regionparam)
    print(quest_marker_coords) if quest_marker_coords else print('not found')
    pa.moveTo(quest_marker_coords)
    pa.click()
    
    
if __name__ == '__main__':
    main()