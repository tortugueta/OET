from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ViewPort(QGraphicsView):
	"""
	This is a subclass of QGraphicsWindow that adds behavior to its
	mousePressEvent function
	"""
	
	def __init__(self, parent=None):
		QGraphicsView.__init__(self, parent)
		
		self.ensureVisible(0, 0, 859, 631)
		self.clicked = False
	
	def mousePressEvent(self, event):
		"""
		What to do when the mouse is clicked in the graphics window
		"""
		
		# Check to which tab the current scene corresponds, and act accordingly
		currentTab = self.parent().parent().tabWidget.currentIndex()
		if currentTab == 0:
			self.mousePressEvent_wheel()
		elif currentTab == 1:
			self.mousePressEvent_tab2(event)

	def mousePressEvent_wheel(self):
		"""
		What to do when we click in the scene of The Wheel
		"""
		
		pass

	def mousePressEvent_tab2(self, event):
		"""
		What to do when we click in the scene of the tab2
		"""
		
		currentScene = self.scene()
		sceneCoordinates = self.mapToScene(event.pos())
		radius = 40

		if not self.clicked:
			strokeWidth = 15
			pen = QPen(Qt.white, strokeWidth)
			circle = QGraphicsEllipseItem(0, 0, radius * 2, radius * 2)
			circle.setPos(sceneCoordinates.x() - radius, sceneCoordinates.y() - radius)
			circle.setPen(pen)
			currentScene.addItem(circle)
			self.centerOn(0, 0)
			self.clicked = True
		else:
			duration = 1 # seconds
			timeline = QTimeLine(duration * 1000)
			timeline.setFrameRange(0, 1)
			timeline.setUpdateInterval(1)
			timeline.setCurveShape(2)
			self.movement = QGraphicsItemAnimation()
			self.movement.setTimeLine(timeline)
			
			self.movement.setPosAt(0, currentScene.items()[0].scenePos())
			finalx = sceneCoordinates.x() - radius
			finaly = sceneCoordinates.y() - radius
			self.movement.setPosAt(1, QPointF(finalx, finaly))
			self.movement.setItem(currentScene.items()[0])
			timeline.start()
			self.clicked = False
