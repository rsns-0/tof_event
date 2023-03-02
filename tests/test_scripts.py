import pytest
from scripts.click_scripts import *

def test_retry():
    with pytest.raises(TriesExhausted) as excinfo:
        top_left = (2243,223)
        bot_right = (2542,474)
        width = bot_right[0]-top_left[0]
        height = bot_right[1]-top_left[1]
        regionparam = (top_left[0], top_left[1], width, height)
        quest_marker_coords = locate("quest_marker.png", region=regionparam)
        print(quest_marker_coords) if quest_marker_coords else print('not found')