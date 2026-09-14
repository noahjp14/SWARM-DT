import csv
import json

unit_data = {}

# opens csv file from run and stores data in unit dictionairy, jsonifies the code to make sure everything is converted to dictionary format
def parse_csv(filename):
    with open(filename, "r") as file:
        data = csv.DictReader(file)
        for row in data:

            parsed = json.loads(row["data_str"])

            if isinstance(parsed, list):
                parsed = {"neighbors": parsed}

            row["data_str"] = parsed

            group_key = row["UI_id"]
            if (group_key not in unit_data):
                unit_data[group_key] = []

            unit_data[group_key].append(row)

# sorts the dictionairy by local time 
def sort_by_time(unit_data):
    for group_key in unit_data:
        unit_data[group_key].sort(key=lambda row: "local_time")



