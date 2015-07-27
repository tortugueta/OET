#! /usr/bin/python
# FIXME: for some reason the wheel does not appear centered
# FIXME: The scene creation, animations and stuff, should probably be coded in
#	the GraphicsWindow class, not in the MainWindow
# FIXME: When I create the corners in tab2 and also when I resize them, I need
#	to add some weird offset to make them align to the edge of the scene. I
#	should find out why I need those offsets.
# FIXME: When stopping, lowering the rps, and starting again, sometimes you
#	get a first rapid short rotation. That is because the initial angle is set
#	to the end angle of the previous unit rotation. This is not trivial to
#	solve because when I stop an animation mid-play, I don't know how to fetch
#	the current angle of the figure.
# FIXME: the GraphicsWindow should be a MainWindow instad of a QDialog
# This is a test.

import sys
import os
import math
import datetime
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import main_window
import graphics_window
import calibrationWindow

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
		
		# Populate the list of shapes in the Shapes tab
		self.tab3_shapesComboBox.addItems(['Circle', 'Rectangle'])
		
		# Create the scenes for each tab
		self.createScenes()
		
		# Global connections
		self.connect(self.tabWidget, SIGNAL("currentChanged(int)"), self.switchTab)
		self.connect(self.actionReset, SIGNAL("activated()"), self.createScenes)
		self.connect(self.actionInvert, SIGNAL("toggled(bool)"), self.updateColors)
		
		# Connections for the Wheel tab
		self.connect(self.tab1_scaleSpinBox, SIGNAL("valueChanged(double)"), self.wheelScene_updateProperties)
		self.connect(self.tab1_innerRadiusSpinBox, SIGNAL("valueChanged(double)"), self.wheelScene_updateProperties)
		self.connect(self.tab1_thicknessSpinBox, SIGNAL("valueChanged(double)"), self.wheelScene_updateProperties)
		self.connect(self.tab1_engagePushButton, SIGNAL("clicked()"), self.wheelScene_startRotation)
		self.connect(self.tab1_speedSpinBox, SIGNAL("valueChanged(double)"), self.wheelScene_updateParameters)
		self.connect(self.tab1_distanceSpinBox, SIGNAL("valueChanged(double)"), self.wheelScene_updateParameters)
		self.connect(self.tab1_densitySpinBox, SIGNAL("valueChanged(double)"), self.wheelScene_updateParameters)
		self.connect(self.tab1_diameterSpinBox, SIGNAL("valueChanged(double)"), self.wheelScene_updateParameters)
		self.connect(self.tab1_viscositySpinBox, SIGNAL("valueChanged(double)"), self.wheelScene_updateParameters)
		self.connect(self.tab1_recordPushButton, SIGNAL("clicked()"), self.wheelScene_saveData)
		
		# Connections for the Shapes tab
		self.connect(self.tab3_shapesComboBox, SIGNAL("currentIndexChanged(int)"), self.shapesScene_update)
		self.connect(self.tab3_thicknessSpinBox, SIGNAL("valueChanged(double)"), self.shapesScene_update)
		self.connect(self.tab3_scaleSpinBox, SIGNAL("valueChanged(double)"), self.shapesScene_update)
		self.connect(self.tab3_rotationSpinBox, SIGNAL("valueChanged(double)"), self.shapesScene_update)
		self.connect(self.tab3_filledCheckBox, SIGNAL("stateChanged(int)"), self.shapesScene_update)
		self.connect(self.tab3_nrowsSpinBox, SIGNAL("valueChanged(int)"), self.shapesScene_update)
		self.connect(self.tab3_ncolumnsSpinBox, SIGNAL("valueChanged(int)"), self.shapesScene_update)
		self.connect(self.tab3_rowPitchSpinBox, SIGNAL("valueChanged(double)"), self.shapesScene_update)
		self.connect(self.tab3_columnPitchSpinBox, SIGNAL("valueChanged(double)"), self.shapesScene_update)
		
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
		self.shapesScene = self.createScene_Shapes()
		self.shapesScene_update()
		
		# Visualize the scene corresponding to the current tab and keep a pointer
		# to the current scene in the GraphicsWindow instance
		tabIndex = self.tabWidget.currentIndex()
		self.switchTab(tabIndex)

	def createScene_Wheel(self):
		"""
		Creates the scene of the wheel
		"""
		
		# Create the scene and set some basic properties
		scene = QGraphicsScene(parent=self)
		scene.setBackgroundBrush(Qt.black)
		thickness = self.tab1_thicknessSpinBox.value()
		pixelRadius_outer = 100
		pixelRadius_inner = self.tab1_innerRadiusSpinBox.value()
		pen = QPen(Qt.white, thickness)
		
		# Create the items
		outer_circle = QGraphicsEllipseItem(-pixelRadius_outer, -pixelRadius_outer, pixelRadius_outer*2, pixelRadius_outer*2)
		inner_circle = QGraphicsEllipseItem(-pixelRadius_inner, -pixelRadius_inner, pixelRadius_inner*2, pixelRadius_inner*2)
		vline = QGraphicsLineItem(0, -pixelRadius_outer, 0, pixelRadius_outer)
		hline = QGraphicsLineItem(-pixelRadius_outer, 0, pixelRadius_outer, 0)
		outer_circle.setPen(pen)
		inner_circle.setPen(pen)
		vline.setPen(pen)
		hline.setPen(pen)
		wheel = QGraphicsItemGroup()
		wheel.addToGroup(outer_circle)
		wheel.addToGroup(inner_circle)
		wheel.addToGroup(vline)
		wheel.addToGroup(hline)
		wheel.setFlags(QGraphicsItem.GraphicsItemFlags(1)) # Make the item movable
		wheel.setPos(QPointF(0, 0))
		
		# Add the items to the scene
		scene.addItem(wheel)
		
		# Create a running variable that will be used to determine the rotation angle
		# of the wheel
		self.wheelAngle = 0.0
		
		# Make the calculations with the initial values
		self.wheelScene_updateParameters()
		
		return scene

	def wheelScene_updateProperties(self):
		"""
		Update the properties of the scene
		"""
		
		thickness = self.tab1_thicknessSpinBox.value()
		scale = self.tab1_scaleSpinBox.value()
		innerRadius = self.tab1_innerRadiusSpinBox.value()
		
		if self.actionInvert.isChecked():
			pen = QPen(Qt.black, thickness)
		else:
			pen = QPen(Qt.white, thickness)
		
		for item in self.wheelScene.items()[0:3]:
			item.setPen(pen)
		
		self.wheelScene.items()[4].setScale(scale)
		self.wheelScene.items()[2].setRect(-innerRadius, -innerRadius, innerRadius*2, innerRadius*2)
	
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
		self.connect(self.tab1_stopPushButton, SIGNAL("clicked()"), timeline.stop)
		
		angularV = self.tab1_speedSpinBox.value()
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
		angularV_SI = self.tab1_speedSpinBox.value() * 2 * math.pi				# rad/s
		linearV = angularV_SI * self.tab1_distanceSpinBox.value()				# In um/s
		self.tab1_linVelocityLcdNumber.display(linearV)
		
		# DEP, which, at constant velocity, will be exactly the same as the
		# drag force
		viscosity_SI = self.tab1_viscositySpinBox.value() * 1e-3			# Pa s
		pradius_SI = (self.tab1_diameterSpinBox.value() / 2) * 1e-6			# m
		linearV_SI = linearV * 1e-6											# m/s
		dep_SI = 6 * math.pi * viscosity_SI * pradius_SI * linearV_SI		# N
		dep = dep_SI * 1e12													# pN
		self.tab1_forceLcdNumber.display(dep)
		
		# Centripetal force
		distance_SI = self.tab1_distanceSpinBox.value() * 1e-6				# m
		density_SI = self.tab1_densitySpinBox.value() * 1e3					# Kg/m3
		beadVolume_SI = 4 * math.pi * pradius_SI**3 / 3						# m3
		beadMass_SI = density_SI * beadVolume_SI							# Kg
		centripetal_SI = beadMass_SI * angularV_SI**2 * distance_SI			# In N
		centripetal = centripetal_SI * 1e12									# pN
		self.tab1_centripetalLcdNumber.display(centripetal)

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
		scale = str(self.tab1_scaleSpinBox.value())
		thickness = str(self.tab1_thicknessSpinBox.value())
		angularVelocity = str(self.tab1_speedSpinBox.value())			# rps
		distance = str(self.tab1_distanceSpinBox.value())				# um
		density = str(self.tab1_densitySpinBox.value())					# g/cm3
		diameter = str(self.tab1_diameterSpinBox.value())				# um
		viscosity = str(self.tab1_viscositySpinBox.value())				# mPa s
		linearVelocity = str(self.tab1_linVelocityLcdNumber.value())		# um/s
		dep = str(self.tab1_forceLcdNumber.value())						# pN
		centripetalForce = str(self.tab1_centripetalLcdNumber.value())	# pN
		recordLine = '\t'.join([scale, thickness, angularVelocity, distance, density, diameter, viscosity, linearVelocity, dep, centripetalForce])
		file.write(recordLine + '\n')
			
		file.close()

	def createScene_Tab2(self):
		"""
		Creates the scene of the second tab
		"""
		
		scene = QGraphicsScene(parent=self)
		
		# Set the color of the background and pens
		scene.setBackgroundBrush(Qt.black)
		thickness = 10
		pen = QPen(Qt.white, thickness)
		
		# Create the alignment marks
		height = self.graphWin.graphicsView.height()
		width = self.graphWin.graphicsView.width()
		fraction = 10
		
		tlcorner_vline = QGraphicsLineItem(0, 0, 0, height/fraction)
		tlcorner_vline.setPen(pen)
		tlcorner_hline = QGraphicsLineItem(0, 0, width/fraction, 0)
		tlcorner_hline.setPen(pen)
		tlcorner = QGraphicsItemGroup()
		tlcorner.addToGroup(tlcorner_vline)
		tlcorner.addToGroup(tlcorner_hline)
		tlcorner.setPos(self.graphWin.graphicsView.mapToScene(0, 0))
		scene.addItem(tlcorner)
		
		blcorner_vline = QGraphicsLineItem(0, 0, 0, -height/fraction)
		blcorner_vline.setPen(pen)
		blcorner_hline = QGraphicsLineItem(0, 0, width/fraction, 0)
		blcorner_hline.setPen(pen)
		blcorner = QGraphicsItemGroup()
		blcorner.addToGroup(blcorner_vline)
		blcorner.addToGroup(blcorner_hline)
		blcorner.setPos(self.graphWin.graphicsView.mapToScene(0, height-3)) # For some reason there is a 3 pixel offset
		scene.addItem(blcorner)
		
		trcorner_vline = QGraphicsLineItem(0, 0, 0, height/fraction)
		trcorner_vline.setPen(pen)
		trcorner_hline = QGraphicsLineItem(0, 0, -width/10, 0)
		trcorner_hline.setPen(pen)
		trcorner = QGraphicsItemGroup()
		trcorner.addToGroup(trcorner_vline)
		trcorner.addToGroup(trcorner_hline)
		trcorner.setPos(self.graphWin.graphicsView.mapToScene(width-3, 0)) # For some reason there is a 3 pixel offset
		scene.addItem(trcorner)
		
		brcorner_vline = QGraphicsLineItem(0, 0, 0, -height/fraction)
		brcorner_vline.setPen(pen)
		brcorner_hline = QGraphicsLineItem(0, 0, -width/fraction, 0)
		brcorner_hline.setPen(pen)
		brcorner = QGraphicsItemGroup()
		brcorner.addToGroup(brcorner_vline)
		brcorner.addToGroup(brcorner_hline)
		brcorner.setPos(self.graphWin.graphicsView.mapToScene(width-3, height-3)) # For some reason there is a 3 pixel offset
		scene.addItem(brcorner)

		return scene

	def createScene_Shapes(self):
		"""
		Creates a scene where we can choose among different basic shapes
		"""
		
		# Create the scene and set some basic properties
		scene = QGraphicsScene(parent=self)
		scene.setBackgroundBrush(Qt.black)

		return scene
	
	def shapesScene_update(self):
		"""
		Removes the item currently displayed in the scene and adds the
		currently selected item
		"""
		
		# Remove the existing shape in order to draw the new one, but get its
		# position
		try:
			for item in self.shapesScene.items()[0:-1]:
				self.shapesScene.removeItem(item)
		except IndexError:
			pos = QPointF(0, 0)
		
		# Read the parameters set in the interface
		selectedShape = self.tab3_shapesComboBox.currentIndex()
		thickness = self.tab3_thicknessSpinBox.value()
		scale = self.tab3_scaleSpinBox.value()
		angle = self.tab3_rotationSpinBox.value()
		filled = self.tab3_filledCheckBox.isChecked()
		nrows = self.tab3_nrowsSpinBox.value()
		ncolumns = self.tab3_ncolumnsSpinBox.value()
		row_pitch = self.tab3_rowPitchSpinBox.value()
		column_pitch = self.tab3_columnPitchSpinBox.value()
		radius = 50 # This is the radius for the circles and half the size for the rectangles
		row_period = 2 * radius + row_pitch
		column_period = 2 * radius + column_pitch
				
		# Set the colors accoding to the "Invert" selection
		if self.actionInvert.isChecked():
			pen = QPen(Qt.black, thickness)
			brush = QBrush(Qt.black)
		else:
			pen = QPen(Qt.white, thickness)
			brush = QBrush(Qt.white)
		
		# Code specific to each shape selection
		if selectedShape == 0:
			# Code for the circle
			circleList = [QGraphicsEllipseItem(0 + column * column_period, 0 - row * row_period, radius * 2,  radius * 2)
				for row in xrange(nrows)
				for column in xrange(ncolumns)]
			item = QGraphicsItemGroup()
			for circle in circleList:
				circle.setPen(pen)
				if filled:
					circle.setBrush(brush)
				item.addToGroup(circle)
			item.setFlags(QGraphicsItem.GraphicsItemFlags(1)) # Make item movable
			item.setPos(-item.boundingRect().width()/2, item.boundingRect().height()/2)
			item.setRotation(angle)
			self.shapesScene.addItem(item)
			item.setScale(scale)
		elif selectedShape == 1:
			# Code for the rectangle
			rectangleList = [QGraphicsRectItem(0 + column * column_period, 0 - row * row_period,  radius * 2, radius * 2)
				for row in xrange(nrows)
				for column in xrange(ncolumns)]
			item = QGraphicsItemGroup()
			for rectangle in rectangleList:
				rectangle.setPen(pen)
				if filled:
					rectangle.setBrush(brush)
				item.addToGroup(rectangle)
			item.setFlags(QGraphicsItem.GraphicsItemFlags(1)) # Make item movable
			item.setPos(-item.boundingRect().width()/2, item.boundingRect().height()/2)
			item.setRotation(angle)
			self.shapesScene.addItem(item)
			item.setScale(scale)

	def updateColors(self, inverted):
		"""
		Update the colors of all the scenes
		"""
		
		if inverted:
			# Modify the Wheel scene
			self.wheelScene.setBackgroundBrush(Qt.white)
			for item in self.wheelScene.items():
				try:
					pen = item.pen()
					pen.setBrush(Qt.black)
					item.setPen(pen)
				except AttributeError:
					pass
			
			# Modify the second scene
			self.tab2Scene.setBackgroundBrush(Qt.white)
			for item in self.tab2Scene.items():
				try:
					pen = item.pen()
					pen.setBrush(Qt.black)
					item.setPen(pen)
				except AttributeError:
					pass
				if self.tab2_filledCheckBox.isChecked():
					try:
						item.setBrush(Qt.black)
					except AttributeError:
						pass
					
			# Modify the Shapes scene
			self.shapesScene.setBackgroundBrush(Qt.white)
			for item in self.shapesScene.items():
				try:
					pen = item.pen()
					pen.setBrush(Qt.black)
					item.setPen(pen)
				except AttributeError:
					pass
				if self.tab3_filledCheckBox.isChecked():
					try:
						item.setBrush(Qt.black)
					except AttributeError:
						pass
		else:
			# Modify the Wheel scene
			self.wheelScene.setBackgroundBrush(Qt.black)
			for item in self.wheelScene.items():
				try:
					pen = item.pen()
					pen.setBrush(Qt.white)
					item.setPen(pen)
				except AttributeError:
					pass
			
			# Modify the second scene
			self.tab2Scene.setBackgroundBrush(Qt.black)
			for item in self.tab2Scene.items():
				try:
					pen = item.pen()
					pen.setBrush(Qt.white)
					item.setPen(pen)
				except AttributeError:
					pass
				if self.tab2_filledCheckBox.isChecked():
					try:
						item.setBrush(Qt.black)
					except AttributeError:
						pass
			
			# Modify the Shapes scene
			self.shapesScene.setBackgroundBrush(Qt.black)
			for item in self.shapesScene.items():
				try:
					pen = item.pen()
					pen.setBrush(Qt.white)
					item.setPen(pen)
				except AttributeError:
					pass
				if self.tab3_filledCheckBox.isChecked():
					try:
						item.setBrush(Qt.white)
					except AttributeError:
						pass
	
	def switchTab(self, tabindex):
		"""
		What to do when the tab is changed
		"""
		
		if tabindex == 0:	
			self.graphWin.graphicsView.setScene(self.wheelScene)
			try:
				self.calWindow.close()
			except AttributeError:
				pass
		elif tabindex == 1:
			self.graphWin.graphicsView.setScene(self.tab2Scene)
			try:
				self.calWindow.close()
			except AttributeError:
				pass
			self.calWindow = CalibrationWindow(self)
			self.calWindow.show()
			self.connect(self.tab2_opacitySpinBox, SIGNAL("valueChanged(double)"), self.calWindow.changeOpacity)
		elif tabindex == 2:
			self.graphWin.graphicsView.setScene(self.shapesScene)
			try:
				self.calWindow.close()
			except AttributeError:
				pass


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
	
	def resizeEvent(self, event):
		"""
		What to do when we resize the window
		"""

		newWidth = event.size().width()
		newHeight = event.size().height()
		
		# Check to which tab the current scene corresponds, and act accordingly
		currentTab = self.parent().tabWidget.currentIndex()
		if currentTab == 0:
			self.resizeEvent_wheel(event)
		elif currentTab == 1:
			self.resizeEvent_tab2(event, newWidth, newHeight)
		elif currentTab == 2:
			self.resizeEvent_shapes(event)
	
	def resizeEvent_wheel(self, event):
		"""
		What to do in the Wheel scene when we resize the window
		"""
		
		QDialog.resizeEvent(self, event)
		
	def resizeEvent_tab2(self, event, newWidth, newHeight):
		"""
		What to do in the tab2 scene when we resize the window
		"""

		QDialog.resizeEvent(self, event)
		self.graphicsView.setSceneRect(-newWidth/2, -newHeight/2, newWidth/2, newHeight/2)
		scene = self.graphicsView.scene()
		if scene != None:
			tlcorner = scene.items()[-1]
			blcorner = scene.items()[-4]
			trcorner = scene.items()[-7]
			brcorner = scene.items()[-10]
			
			tlcorner.setPos(self.graphicsView.mapToScene(0, 0))
			blcorner.setPos(self.graphicsView.mapToScene(0, newHeight-25)) # For some reason I need the 25 pixel offset
			trcorner.setPos(self.graphicsView.mapToScene(newWidth-25, 0)) # For some reason I need the 25 pixel offset
			brcorner.setPos(self.graphicsView.mapToScene(newWidth-25, newHeight-25)) # For some reason I need the 25 pixel offset

	def resizeEvent_shapes(self, event):
		"""
		What to do in the Shapes scene when we resize the window
		"""
		
		QDialog.resizeEvent(self, event)
		

class CalibrationWindow(QDialog, calibrationWindow.Ui_calibrationWindow):
	"""
	This is the window that we use to calibrate the camera region
	"""
	
	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		calibrationWindow.Ui_calibrationWindow.__init__(self, parent)
		
		self.setupUi(self)
		
	def mousePressEvent(self, event):
		"""
		What to do when the mouse is clicked in the calibration window
		"""
		
		QDialog.mousePressEvent(self, event)
		width = float(self.geometry().width())
		height = float(self.geometry().height())
		xpos = float(event.x())
		ypos = float(event.y())
		relativeX = xpos/width
		relativeY = ypos/height
		
		viewportWidth = self.parent().graphWin.graphicsView.width()
		viewportHeight = self.parent().graphWin.graphicsView.height()
		extrapolatedX = relativeX * viewportWidth
		extrapolatedY = relativeY * viewportHeight
		newEvent = QMouseEvent(QEvent.MouseButtonPress, QPoint(extrapolatedX, extrapolatedY), Qt.LeftButton, Qt.NoButton, Qt.NoModifier)
		
		self.parent().graphWin.graphicsView.mousePressEvent_tab2(newEvent)
		
	def changeOpacity(self, opacity):
		"""
		Change the opacity of the calibration window
		"""
		
		self.setWindowOpacity(opacity)
		
		
def main():
	app = QApplication(sys.argv)
	#app.setStyle("plastique")
	mainWin = MainWindow()
	mainWin.show()
	app.exec_()

main()
