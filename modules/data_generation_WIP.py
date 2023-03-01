"""
WIP
WIP
WIP
"""

from .ui_data_structure_WIP import UiDataCoordinatesOnly, UiDataImage
from pathlib import Path, WindowsPath
import json



def data_generation(data): 
    ui_items = {}
    with open(json_data_path, 'r') as f:
        json_data:dict = json.load(f)
        for k,v in json_data:
            if not v['file_type']:
                UiDataCoordinatesOnly(coordinates=v['coordinates'])
            else:
                UiDataImage(
                    coordinates=v['coordinates'],
                    name=v['name'],
                    image_bounds=v['image_bounds'],
                    )
                

json_data_path = Path("resources/ui_data/data.json")