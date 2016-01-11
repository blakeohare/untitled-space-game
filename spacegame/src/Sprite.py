class Sprite:
	def __init__(self, type):
		self.x = 0
		self.y = 0
		self.dx = 0
		self.dy = 0
		self.radius = .7
		self.layer = None
	
	def update(self, scene):
		if self.layer == None:
			$print("SPRITE IS NOT IN A LAYER")
			return
		
		layerObs = self.layer.obs
		layerBg = self.layer.bg
		
		if self.dx != 0 or self.dy != 0:
			newx = self.x + self.dx
			self.try_update_pos(newx, self.y, layerObs)
			newy = self.y + self.dy
			self.try_update_pos(self.x, newy, layerObs)
			self.dx = 0
			self.dy = 0
	
	def try_update_pos(self, newx, newy, layerObs):
		left = $int(self.x - self.radius)
		right = $int(self.x + self.radius)
		top = $int(self.y - self.radius)
		bottom = $int(self.y + self.radius)
		
		width = layerObs.width
		if left < 0 or right >= width: return
		if top < 0 or bottom >= layerObs.height: return
		
		grid = layerObs.tiles_as_grid
		
		yi = top
		while yi <= bottom:
			xi = left
			i = yi * width + xi
			while xi <= right:
				tile = grid[i]
				if tile != None:
					$print("FOUND TILE: " + $str(xi) + ', ' + $str(yi))
					if tile.is_blocking:
						return
				i += 1
				xi += 1
			yi += 1
		
		self.x = newx
		self.y = newy
	
	def render(self, screen, rc):
		cx = $int(self.x * 24)
		cy = $int((self.y + self.radius) * 24)
		
		$draw_rectangle(screen, cx - 24, cy - 48, 48, 48, 255, 255, 255)