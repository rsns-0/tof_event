import pandas
import json
import logging
from pathlib import Path
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('tof_event_log')

xl_file_path = Path(__file__).parent / "resources/ui_data/dataset1.xlsx"
destination_path = Path(__file__).parent / "resources/ui_data/final_data_file.json"

def main():
    conversion()
    logger.info(f'File saved to {destination_path}')

def conversion():

    def generate_region(x1, y1, x2, y2):
        return (x1, y1, x2 - x1, y2 - y1)


    df = pandas.read_excel(xl_file_path)

    dict_ui_data = {}


    for index, row in df.iterrows():

        item_name = row["name"]
        if row[1] == "image":
            dict_ui_data[item_name] = {
                "file_name": row["file_name"],
                "region": generate_region(row[5], row[6], row[7], row[8]),
                "type": "image",
            }
        else:
            dict_ui_data[item_name] = {
                "coordinates": (row[2], row[3]),
                "type":"point",
                }

    
    with open(destination_path, "w") as f:
        json.dump(dict_ui_data, f, indent=4, sort_keys=True)





if __name__ == "__main__":
    main()
