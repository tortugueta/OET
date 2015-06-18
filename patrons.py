# TODO: Change the "bead radius" spin box to "bead diameter", and update
#	the code accordingly so that the radius is calculated as the diameter/2.
#	I should update the radius used in wheelScene_updateParameters() and the
#	parameter that gets written to file in wheelScene_saveData()

import sys
import os
import math
import datetime
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import main_window
import graphics_window

class MainWindow(QMainWindow, main_window.Ui_MainWindow):
	
	"""
	This is the main window of the program.
	"""
	
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)
		main_window.Ui_MainWindow.__init__(self, parent)
		
		# Build the main window using the setupUi method generated by Qt
		# Designer
		self.setupUi(self)
		
		# Create the dialog that will show the graphics window
		self.graphWin = GraphicsWindow(parent=self)
		self.graphWin.show()
		
		# Create the scenes for each tab
		self.createScenes()
		
		# Global connections
		self.connect(self.tabWidget, SIGNAL("currentChanged(int)"), self.switchTab)
		self.connect(self.actionReset, SIGNAL("activated()"), self.createScenes)
		self.connect(self.actionInvert, SIGNAL("toggled(bool)"), self.updateColors)
		
		# Connections for the Wheel tab
		self.connect(self.scaleSpinBox, SIGNAL("valueChanged(double)"), self.wheelScene_updateProperties)
		self.connect(self.thicknessSpinBox, SIGNAL("valueChanged(double)"), self.wheelScene_updateProperties)
		self.connect(self.wheelEngagePushButton, SIGNAL("clicked()"), self.wheelScene_startRotation)
		self.connect(self.speedSpinBox, SIGNAL("valueChanged(double)"), self.wheelScene_updateParameters)
		self.connect(self.distanceSpinBox, SIGNAL("valueChanged(double)"), self.wheelScene_updateParameters)
		self.connect(self.densitySpinBox, SIGNAL("valueChanged(double)"), self.wheelScene_updateParameters)
		self.connect(self.diameterSpinBox, SIGNAL("valueChanged(double)"), self.wheelScene_updateParameters)
		self.connect(self.viscositySpinBox, SIGNAL("valueChanged(double)"), self.wheelScene_updateParameters)
		self.connect(self.wheelRecordPushButton, SIGNAL("clicked()"), self.wheelScene_saveData)
		
		# Connections for the Tab2 tab
		
		# Grab the current date for the filename
		now = datetime.datetime.now()
		dateStr = '-'.join([str(now.year), str(now.month), str(now.day)])
		timeStr = ''.join(['%02d' % now.hour, '%02d' % now.minute, '%02d' % now.second])
		self.fname_prefix = '_'.join([dateStr, timeStr])
				
	def createScenes(self):
		"""
		Create all the scenes from scratch
		"""
		
		# Uncheck the "invert" action
		self.actionInvert.setChecked(False)
		
		# Create all the scenes
		self.wheelScene = self.createScene_Wheel()
		self.tab2Scene = self.createScene_Tab2()
		
		# Visualize the scene corresponding to the current tab
		if self.tabWidget.currentIndex() == 0:
			self.graphWin.graphicsView.setScene(self.wheelScene)
		elif self.tabWidget.currentIndex() == 1:
			self.graphWin.graphicsView.setScene(self.tab2Scene)

	def createScene_Wheel(self):
		"""
		Creates the scene of the wheel
		"""
		
		# Create the scene and set some basic properties
		scene = QGraphicsScene(parent=self)
		scene.setBackgroundBrush(Qt.black)
		thickness = self.thicknessSpinBox.value()
		pixelRadius = 100
		pen = QPen(Qt.white, thickness)
		
		# Create the items
		circle = QGraphicsEllipseItem(-pixelRadius, -pixelRadius, pixelRadius*2, pixelRadius*2)
		vline = QGraphicsLineItem(0, -pixelRadius, 0, pixelRadius)
		hline = QGraphicsLineItem(-pixelRadius, 0, pixelRadius, 0)
		circle.setPen(pen)
		vline.setPen(pen)
		hline.setPen(pen)
		wheel = QGraphicsItemGroup()
		wheel.addToGroup(circle)
		wheel.addToGroup(vline)
		wheel.addToGroup(hline)
		wheel.setFlags(QGraphicsItem.GraphicsItemFlags(1))
		
		# Add the items to the scene
		scene.addItem(wheel)
		
		# Create a running variable that will be used to determine the rotation angle
		# of the wheel
		self.wheelAngle = 0.0
		
		return scene
		
	def createScene_Tab2(self):
		"""
		Creates the scene of the second tab
		"""
		
		scene = QGraphicsScene(parent=self)
		
		# Set the color of the background
		scene.setBackgroundBrush(Qt.black)
		
		# Create the pen to be used to draw the items
		strokeWidth = 1
		pen = QPen(Qt.white, strokeWidth)
		
		# Create the items
		x = 300
		y = 300
		width = 100
		height = 50
		rectangle = QGraphicsRectItem(x, y, width, height)
		rectangle.setPen(pen)
		rectangle.setFlags(QGraphicsItem.GraphicsItemFlags(1))
		
		# Add the items to the scene
		scene.addItem(rectangle)
		
		return scene
			
	def wheelScene_updateProperties(self):
		"""
		Update the properties of the scene
		"""
		
		thickness = self.thicknessSpinBox.value()
		scale = self.scaleSpinBox.value()
		
		if self.actionInvert.isChecked():
			pen = QPen(Qt.black, thickness)
		else:
			pen = QPen(Qt.white, thickness)
		
		for item in self.wheelScene_Items[1:]:
			item.setPen(pen)
		
		self.wheelScene.items()[3].setScale(scale)
	
	def wheelScene_startRotation(self):
		"""
		Start the rotation of the wheel
		"""
		
		unitRotation = 0.1 # seconds
		timeline = QTimeLine(unitRotation * 1000)
		timeline.setFrameRange(0, 1)
		timeline.setUpdateInterval(1)
		timeline.setCurveShape(3)
		self.rotation = QGraphicsItemAnimation()
		self.rotation.setTimeLine(timeline)
		
		self.connect(timeline, SIGNAL("finished()"), self.wheelScene_startRotation)
		self.connect(self.wheelStopPushButton, SIGNAL("clicked()"), timeline.stop)
		
		angularV = self.speedSpinBox.value()
		initial = self.wheelAngle
		if initial > 360:
			initial -= 360
		final = initial + angularV * 360 * unitRotation
		self.wheelAngle = final
		
		self.rotation.setRotationAt(0, initial)
		self.rotation.setRotationAt(1, final)
		self.rotation.setItem(self.wheelScene.items()[3])
		timeline.start()
	
	def wheelScene_updateParameters(self):
		"""
		Update the linear velocity, DEP and centripetal force according to the
		values of the parameters
		"""
		
		# Linear velocity
		angularV_SI = self.speedSpinBox.value() * 2 * math.pi				# rad/s
		linearV = angularV_SI * self.distanceSpinBox.value()				# In um/s
		self.linVelocityLcdNumber.display(linearV)
		
		# DEP, which, at constant velocity, will be exactly the same as the
		# drag force
		viscosity_SI = self.viscositySpinBox.value() * 1e-3					# Pa s
		pradius_SI = (self.diameterSpinBox.value() / 2) * 1e-6				# m
		linearV_SI = linearV * 1e-6											# m/s
		dep_SI = 6 * math.pi * viscosity_SI * pradius_SI * linearV_SI		# N
		dep = dep_SI * 1e12													# pN
		self.forceLcdNumber.display(dep)
		
		# Centripetal force
		distance_SI = self.distanceSpinBox.value() * 1e-6					# m
		density_SI = self.densitySpinBox.value() * 1e3						# Kg/m3
		beadVolume_SI = 4 * math.pi * pradius_SI**3 / 3						# m3
		beadMass_SI = density_SI * beadVolume_SI							# Kg
		centripetal_SI = beadMass_SI * angularV_SI**2 * distance_SI			# In N
		centripetal = centripetal_SI * 1e12									# pN
		self.centripetalLcdNumber.display(centripetal)

	def wheelScene_saveData(self):
		"""
		Save parameters to disk
		"""
		
		fname = self.fname_prefix + '_WheelTest' + '.dat' 
		if os.path.isfile(fname):
			# Open in append mode
			file = open(fname, 'a')
		else:
			# Open in write mode (create the file) and write header
			file = open(fname, 'w')
			
			scaleHead = 'Scale'
			thicknessHead = 'Thickness'
			angularVelocityHead = 'AngularVelocity (rps)'
			distanceHead = 'Distance (um)'
			densityHead = 'Density (g/cm3)'
			diameterHead = 'Particle diameter (um)'
			viscosityHead = 'Viscosity (mPa s)'
			linearVelocityHead = 'Linear velocity (um/s)'
			depHead = 'DEP (pN)'
			centripetalForceHead = 'Centripetal force (pN)'
			header = '\t'.join(['# ' + scaleHead, thicknessHead, angularVelocityHead, distanceHead, densityHead, diameterHead, viscosityHead, linearVelocityHead, depHead, centripetalForceHead])
			file.write('# The Wheel test\n')
			file.write(header + '\n\n')
		
		# Write the values
		scale = str(self.scaleSpinBox.value())
		thickness = str(self.thicknessSpinBox.value())
		angularVelocity = str(self.speedSpinBox.value())			# rps
		distance = str(self.distanceSpinBox.value())				# um
		density = str(self.densitySpinBox.value())					# g/cm3
		diameter = str(self.diameterSpinBox.value())				# um
		viscosity = str(self.viscositySpinBox.value())				# mPa s
		linearVelocity = str(self.linVelocityLcdNumber.value())		# um/s
		dep = str(self.forceLcdNumber.value())						# pN
		centripetalForce = str(self.centripetalLcdNumber.value())	# pN
		recordLine = '\t'.join([scale, thickness, angularVelocity, distance, density, diameter, viscosity, linearVelocity, dep, centripetalForce])
		file.write(recordLine + '\n')
			
		file.close()

	def updateColors(self, inverted):
		"""
		Update the colors of all the scenes
		"""
		
		if inverted:
			# Modify the Wheel
			self.wheelScene.setBackgroundBrush(Qt.white)
			pen = QPen(Qt.black, self.thicknessSpinBox.value())
			for item in self.wheelScene.items()[0:3]:
				item.setPen(pen)
			
			# Modify the second tab
			self.tab2Scene.setBackgroundBrush(Qt.white)
			pen = QPen(Qt.black, 1)
			for item in self.tab2Scene.items():
				item.setPen(pen)
		else:
			# Modify the Wheel
			self.wheelScene.setBackgroundBrush(Qt.black)
			pen = QPen(Qt.white, self.thicknessSpinBox.value())
			for item in self.wheelScene.items()[0:3]:
				item.setPen(pen)
			
			# Modify the second tab
			self.tab2Scene.setBackgroundBrush(Qt.black)
			pen = QPen(Qt.white, 1)
			for item in self.tab2Scene.items():
				item.setPen(pen)
	
	def switchTab(self, tabindex):
		"""
		What to do when the tab is changed
		"""
		
		if tabindex == 0:		
			self.graphWin.graphicsView.setScene(self.wheelScene)
		elif tabindex == 1:
			self.graphWin.graphicsView.setScene(self.tab2Scene)
			

class GraphicsWindow(QDialog, graphics_window.Ui_GraphicsWindow):
	"""
	This is the dialog that shows the graphics window
	"""
	
	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		graphics_window.Ui_GraphicsWindow.__init__(self, parent)
		
		# Build the main window using the setupUi method generated by Qt
		# Designer
		self.setupUi(self)


def main():
	app = QApplication(sys.argv)
	mainWin = MainWindow()
	mainWin.show()
	app.exec_()

main()
