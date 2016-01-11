class TitleScene:
	def __init__(self):
		self.next = self
		self.scaled_image = None
	
	def update(self, events):
		for ev in events:
			if ev.type == 'quit':
				self.next = None
			elif ev.type == 'key':
				if ev.down and ev.key == 'enter':
					self.next = PlayScene('base')
	
	def render(self, screen, images, rc, is_primary):
		if self.scaled_image == None:
			img = images['title']
			self.scaled_image = $image_scale(img, $image_width(img) * 3, $image_height(img) * 3)
		
		$image_blit(screen, self.scaled_image, 0, 0)