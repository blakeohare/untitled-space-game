class Waypoint:
	def __init__(self, id, layer_id, x, y, width, height):
		self.id = id
		self.layer_id = layer_id
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.center_x = x + width / 2.0
		self.center_y = y + height / 2.0