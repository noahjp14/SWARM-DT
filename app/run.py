from ingest_layer.parser import *

filepath_for_test = "app/data/QS_BASELINE_30U_2OF6_iteration_4_log(in).csv"


def load_sort(file):
    parse_csv(file)
    sort_by_time(unit_data)

    print("parse complete")


if __name__ == "__main__":

    load_sort(filepath_for_test)
    

    print(unit_data["5"])
