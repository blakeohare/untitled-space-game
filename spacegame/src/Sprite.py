class Sprite:
	def __init__(self, type):
		self.x = 0
		self.y = 0
		self.dx = 0
		self.dy = 0
		self.layer = None
	
	def update(self, scene):
		if self.dx != 0 or self.dy != 0:
			layer = self.layer.above
			newx = self.x + self.dx
			newy = self.y + self.dy
			
	
	def render(self, screen, rc):
		cx = $int(self.x * 24)
		cy = $int(self.y * 24)
		
		$draw_rectangle(screen, cx - 24, cy - 48, 48, 48, 255, 255, 255)