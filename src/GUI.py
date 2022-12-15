from PyQt5.QtGui import QPen, QBrush
from world import World
from corrupted_save_file_error import *
from loadsave_IO import LoadSaveIO
from planet_graphics_item import PlanetGraphicsItem
from planet import Planet
from PyQt5.QtCore import Qt, QPointF, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QMessageBox, QAction, QMainWindow


class Ui_MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()
        self.setWindowTitle("SolarSim")
        self.setGeometry(0, 0, 1920, 1080)
        self.cycles = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_scene)


        self.added_items = []

        self.init_grapics()

        self.init_input()

        self.show()

    def init_input(self):
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(1660, 12, 260, 720))
        font = QtGui.QFont()
        font.setPointSize(10)
        font8 = QtGui.QFont()
        font8.setPointSize(8)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("Input")

        #input speed
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 80, 120, 15))
        self.label.setText("Sim duration [days]:")
        self.lineEdit1 = QtWidgets.QLineEdit(self.groupBox)
        #self.lineEdit1.setText("Sim duration")
        self.lineEdit1.returnPressed.connect(self.set_sim_duration)
        self.lineEdit1.setGeometry(QtCore.QRect(150, 80, 69, 22))

        #input speed
        self.lineEdit2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit2.setGeometry(QtCore.QRect(150, 120, 69, 22))
        #self.lineEdit2.setText("Sim speed")
        self.lineEdit2.returnPressed.connect(self.set_sim_speed)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 120, 15))
        self.label_2.setText("Sim speed [days/s]:")


        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 221, 21))
        self.label_3.setText("Simulation parameters:")

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 250, 221, 31))
        self.label_4.setText("Satellite Parameters:")


        #BUTTONS
        self.LoadButton = QtWidgets.QPushButton(self.groupBox)
        self.LoadButton.setGeometry(40, 170, 75, 23) #120 good loc for save button
        self.LoadButton.setFont(font8)
        self.LoadButton.setText("Load")
        self.LoadButton.clicked.connect(self.Load_handler)

        self.ClearButton = QtWidgets.QPushButton(self.groupBox)
        self.ClearButton.setGeometry(120, 170, 75, 23)
        self.ClearButton.setFont(font8)
        self.ClearButton.setText("Clear")
        self.ClearButton.clicked.connect(self.scene.clear)

        self.RunButton = QtWidgets.QPushButton(self.groupBox)
        self.RunButton.setGeometry(QtCore.QRect(40, 200, 75, 23))
        self.RunButton.setFont(font8)
        self.RunButton.setText("Run")
        self.RunButton.clicked.connect(self.Run_handler)

        self.Update = QtWidgets.QPushButton(self.groupBox)
        self.Update.setGeometry(120, 200, 75, 23)
        self.Update.setFont(font8)
        self.Update.setText("Stop")
        self.Update.clicked.connect(self.timer.stop)

        self.LoadsatButton = QtWidgets.QPushButton(self.groupBox)
        self.LoadsatButton.setGeometry(QtCore.QRect(40, 450, 111, 23))
        self.LoadsatButton.setFont(font8)
        self.LoadsatButton.setText("Load Sat")
        self.LoadsatButton.clicked.connect(self.Load_sat_handler)

        #input 4 sat coordinates
        self.lineEdit3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit3.setGeometry(QtCore.QRect(150, 300, 69, 22))
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 300, 120, 15))
        self.label_5.setText("Coordinates in [km]:")
        self.label_xyz2 = QtWidgets.QLabel(self.groupBox)
        self.label_xyz2.setGeometry(QtCore.QRect(160, 280, 120, 15))
        self.label_xyz2.setText("x, y, z")

        #input 6, Velocity Do i need 3 different inputs?
        self.lineEdit7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit7.setGeometry(QtCore.QRect(150, 340, 69, 22))
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 340, 120, 15))
        self.label_6.setText("Velocity [m/s]:")
        self.label_xyz = QtWidgets.QLabel(self.groupBox)
        self.label_xyz.setGeometry(QtCore.QRect(160, 320, 120, 15))
        self.label_xyz.setText("x, y, z")

        #input 7, Mass
        self.lineEdit8 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit8.setGeometry(QtCore.QRect(150, 380, 69, 22))
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 380, 120, 15))
        self.label_7.setText("Mass [kg]:")

        #input 8, name
        self.lineEdit9 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit9.setGeometry(QtCore.QRect(150, 420, 69, 22))
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(20, 420, 120, 15)
        self.label_8.setText("Name:")

    def init_grapics(self):
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 1920, 1080)
        black_brush = QBrush(Qt.black)
        self.scene.setBackgroundBrush(black_brush)

        view = QtWidgets.QGraphicsView(self.scene, self)
        view.setGeometry(QtCore.QRect(20, 20, 1640, 960))

    def add_planet_graphics_items(self):
        self.scene.clear()
        #need to scale the coordinates. since the center of our sim window will be on the pixel (540,360)
        #and the Y-axis scales downward from the top of the screen, so eg. (540,350) will be displayed above the origin

        for planet in self.world.get_planets():
            if planet.name != " SUN":
                x = int(960.0 + planet.x_loca / 5000000000.0)
                y = int(540.0 - planet.y_loca / 5000000000.0)
                d = int(planet.radius * 2.0 / 1000000.0)
                color = planet.color.strip()
                #z = float(planet.z_loca) / 100000
                if d < 50:
                    item = PlanetGraphicsItem(x, y, d)
                else:
                    item = PlanetGraphicsItem(x, y, 50)
                item.set_brush(color)
                item.set_name(planet.name)
                #item.setPos(QPointF(x, y))
                self.added_items.append(item)
                self.scene.addItem(item)
            else:
                x = int(960.0 + planet.x_loca / 5000000000.0)
                y = int(540.0 - planet.y_loca / 5000000000.0)
                d = 10
                color = planet.color.strip()
                item = PlanetGraphicsItem(x, y, d)
                item.set_name(planet.name)
                item.set_brush(color)
                self.added_items.append(item)
                self.scene.addItem(item)

    def update_scene(self):
        self.world.update_all()
        #self.add_planet_graphics_items()
        self.update_graphics_items()
        if self.cycles < self.sim_dur:
            self.cycles += 1
        else:
            self.timer.stop()

    def update_graphics_items(self):
        '''
        Function to set new positions for each graphics item
        '''
        #Name variable set for debugging purposes
        for item in self.added_items:
            for planet in self.world.get_planets():
                if item.name == planet.name:
                    if not item.name == " SUN":
                        name = item.name
                        x = int(960.0 + planet.x_loca / 5000000000.0)
                        y = int(540.0 - planet.y_loca / 5000000000.0)
                        d = int(planet.radius * 2.0 / 1000000.0)
                        if d < 50:
                            if planet.radius < 1000:
                                name = item.name
                                x = int(960.0 + planet.x_loca / 5000000000.0)
                                y = int(540.0 - planet.y_loca / 5000000000.0)
                                item.setRect(x, y, 10, 10)
                            else:
                                item.setRect(x, y, d, d)
                        else:
                            item.setRect(x, y, 50, 50)
                    else:
                        name = item.name
                        x = int(960.0 + planet.x_loca / 5000000000.0)
                        y = int(540.0 - planet.y_loca / 5000000000.0)
                        d = 10
                        item.setRect(x, y, d, d)


    def Load_handler(self):
        path = self.open_dialog_box()
        if path:
            with open(path, "r") as f:
                self.world = LoadSaveIO.load_save(World(), f)

            self.add_planet_graphics_items()

    def Run_handler(self):
        self.set_sim_speed()
        self.set_sim_duration()
        #self.update_scene()
        self.timer.setInterval(int(1000 / self.sim_speed))
        self.timer.start()
        self.cycles = 0

    def set_sim_duration(self):
        self.sim_dur = int(self.lineEdit1.text())

    def set_sim_speed(self):
        self.sim_speed = int(self.lineEdit2.text())


    def Load_sat_handler(self):
        self.set_sat_name()
        self.set_sat_mass()
        self.set_sat_velo()
        self.set_sat_coord()
        sat = Planet()
        sat.set_name(self.sat_name)
        sat.set_mass(self.sat_mass)
        sat.set_radius(100)
        sat.conv_set_location(self.satc_x, self.satc_y, self.satc_z)
        sat.set_velocity(self.satv_x, self.satv_y, self.satv_z)
        sat.set_color("blank")
        self.world.add_planet(sat)

        self.add_sat_graphics_item(sat)
        self.update_graphics_items()


    def add_sat_graphics_item(self, sat):
        x = int(960.0 + sat.x_loca / 5000000000.0)
        y = int(540.0 - sat.y_loca / 5000000000.0)
        d = 10
        color = sat.color
        item = PlanetGraphicsItem(x, y, d)
        item.set_name(sat.name)
        item.set_brush(color)
        self.added_items.append(item)
        self.scene.addItem(item)

    def set_sat_name(self):
        self.sat_name = self.lineEdit9.text()
    def set_sat_mass(self):
        self.sat_mass = float(self.lineEdit8.text())
    def set_sat_velo(self):
        vel = self.lineEdit7.text()
        vel_l = vel.split(",")
        self.satv_x = float(vel_l[0])
        self.satv_y = float(vel_l[1])
        self.satv_z = float(vel_l[2])
    def set_sat_coord(self):
        coord = self.lineEdit3.text()
        coord_l = coord.split(",")
        self.satc_x = float(coord_l[0])
        self.satc_y = float(coord_l[1])
        self.satc_z = float(coord_l[2])

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        return path

    def closeEvent(self, event):
        close = QMessageBox()
        close.setText("Are you sure you want to exit the sim?")
        close.setWindowTitle("Exit program.")
        close.setIcon(QMessageBox.Critical)
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec_()

        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()





