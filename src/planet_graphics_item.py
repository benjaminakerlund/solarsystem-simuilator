from PyQt5.QtCore import QPointF, QRectF, Qt
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import (QApplication, QGraphicsItem, QGraphicsScene,
                             QGraphicsView, QGraphicsEllipseItem)

class PlanetGraphicsItem(QGraphicsEllipseItem):


    def __init__(self, x, y, d):
        super().__init__(x, y, d, d)
        white_pen = QPen(Qt.white)
        white_pen.setWidth(1)
        self.setPen(white_pen)
        self.name = None


    def set_name(self, name):
        self.name = name


    def set_brush(self, color):
        '''
        All of the different color types I have defined for the program.
        defined according to QColor()

        '''
        if color == "yellow":
            self.setBrush(QBrush(Qt.yellow))
        elif color == "magenta":
            self.setBrush(QBrush(Qt.magenta))
        elif color == "dyellow":
            self.setBrush(QBrush(Qt.darkYellow))
        elif color == "cyan":
            self.setBrush(QBrush(Qt.cyan))
        elif color == "red":
            self.setBrush(QBrush(Qt.red))
        elif color == "dgray":
            self.setBrush(QBrush(Qt.darkGray))
        elif color == "blue":
            self.setBrush(QBrush(Qt.blue))
        elif color == "dblue":
            self.setBrush(QBrush(Qt.darkBlue))
        else:
            self.setBrush(QBrush(Qt.white))
