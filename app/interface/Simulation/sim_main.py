# This file serves as the main file for the simulaton interface display

from interface.Simulation.SimBoxGenerated import Ui_Form as interface
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QGraphicsScene, QApplication
from PyQt6.QtGui import QBrush, QPen, QColor
from PyQt6.QtCore import Qt
import sys
from ingest_layer.parser import *

unit_objects = {}

class SimulationWidget(interface, QWidget):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.scene = QGraphicsScene()
            self.graphicsView.setScene(self.scene)
            self.scene.setBackgroundBrush(QColor("#0a0e14"))  #dark background
            
            self.draw_units()
        def showEvent(self, event):
            super().showEvent(event)
            self.graphicsView.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

        def draw_units(self):
            pen = QPen(QColor("green"), 3)
            brush = QBrush(QColor("teal"), Qt.BrushStyle.FDiagPattern)

            for unit in unit_data:
                for row in unit_data[unit]:
                     if (row["SType"] == "pose"):
                          x = row["data_str"]["x"]
                          y = row["data_str"]["y"]
                          circle = self.scene.addEllipse(x, y, 150, 150, pen, brush)
                          circle.setFlag(circle.GraphicsItemFlag.ItemIsSelectable)
                          break



            
            
            