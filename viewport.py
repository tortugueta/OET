from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ViewPort(QGraphicsView):
	"""
	This is a subclass of QGraphicsWindow that adds behavior to its
	mousePressEvent function
	"""
	
	def __init__(self, parent=None):
		QGraphicsView.__init__(self, parent)
		
		#self.setSceneRect(-self.width()/2, -self.height()/2, self.width()/2, self.height()/2)
		self.clicked = False
	
	def mousePressEvent(self, event):
		"""
		What to do when the mouse is clicked in the graphics window
		"""
		
		# Check to which tab the current scene corresponds, and act accordingly
		currentTab = self.parent().parent().tabWidget.currentIndex()
		if currentTab == 0:
			self.mousePressEvent_wheel(event)
		elif currentTab == 1:
			self.mousePressEvent_tab2(event)
		elif currentTab == 2:
			self.mousePressEvent_shapes(event)

	def mousePressEvent_wheel(self, event):
		"""
		What to do when we click in the scene of The Wheel
		"""
		
		QGraphicsView.mousePressEvent(self, event)

	def mousePressEvent_tab2(self, event):
		"""
		What to do when we click in the scene of the tab2
		"""
		
		currentScene = self.scene()
		sceneCoordinates = self.mapToScene(event.pos())

		# Click to create trap
		if not self.clicked:
			self.size = self.parent().parent().tab2_sizeSpinBox.value()
			strokeWidth = self.parent().parent().tab2_thicknessSpinBox.value()
			circle = QGraphicsEllipseItem(0, 0, self.size, self.size)
			circle.setPos(sceneCoordinates.x() - self.size/2, sceneCoordinates.y() - self.size/2)
			if self.parent().parent().tab2_filledCheckBox.isChecked():
				if self.parent().parent().actionInvert.isChecked():
					brush = QBrush(Qt.black)
					pen = QPen(Qt.black, strokeWidth)
				else:
					brush = QBrush(Qt.white)
					pen = QPen(Qt.white, strokeWidth)
				circle.setBrush(brush)
			else:
				if self.parent().parent().actionInvert.isChecked():
					pen = QPen(Qt.black, strokeWidth)
				else:
					pen = QPen(Qt.white, strokeWidth)
			circle.setPen(pen)
			currentScene.addItem(circle)
			self.centerOn(0, 0)
			self.clicked = True
		# Click to move trap
		else:
			duration = self.parent().parent().tab2_travelTimeSpinBox.value() # seconds
			timeline = QTimeLine(duration * 1000)
			timeline.setFrameRange(0, 1)
			timeline.setUpdateInterval(1)
			timeline.setCurveShape(2)
			self.movement = QGraphicsItemAnimation()
			self.movement.setTimeLine(timeline)
			
			self.movement.setPosAt(0, currentScene.items()[0].scenePos())
			finalx = sceneCoordinates.x() - self.size/2
			finaly = sceneCoordinates.y() - self.size/2
			self.movement.setPosAt(1, QPointF(finalx, finaly))
			self.movement.setItem(currentScene.items()[0])
			timeline.start()
			self.clicked = False

	def mousePressEvent_shapes(self, event):
		"""
		What to do when we click in the scene of tab3
		"""
		
		QGraphicsView.mousePressEvent(self, event)
