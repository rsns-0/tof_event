import pytest
from scripts.click_scripts import *
from pathlib import Path



def test_retry():
    with pytest.raises(NotFoundException) as excinfo:
        path = Path(__file__).parent / "test_resources/quest_marker.png"
        qimg = str(path)
        top_left = (2243,223)
        bot_right = (2542,474)
        width = bot_right[0]-top_left[0]
        height = bot_right[1]-top_left[1]
        regionparam = (top_left[0], top_left[1], width, height)
        quest_marker_coords = valreturn_img(qimg, region=regionparam)