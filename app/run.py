from ingest_layer.parser import *
from interface.Simulation.sim_main import *

filepath_for_test = "/Users/noahpointer/SWARM-DT/app/data/QS_BASELINE_30U_2OF6_iteration_4_log(in).csv"


def load_sort(file):
    parse_csv(file)
    sort_by_time(unit_data)

    print("parse complete")



def run():
    load_sort(filepath_for_test)
    from interface.Simulation.sim_main import SimulationWidget
    from PyQt6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = SimulationWidget()
    window.show()
    sys.exit(app.exec())



run()