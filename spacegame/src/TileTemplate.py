class TileTemplate:
	def __init__(self, id, size, flags, images):
		self.id = id
		self.width = $parse_int(size[0])
		self.height = $parse_int(size[1])
		self.image_init = False
		self.images = []
		self.blocking = False
		self.static_image = None
		self.is_static_image = False
		self.tesselation_fixed = False # true if the tile should start the tesselation at the position of the tile, rather than the top left corner of the screen
		for image in images:
			# TODO: adjustable frame speed stuff
			self.images += [IMAGES.images['tiles/' + image]] * 6
		
		if $list_length(images) == 1:
			self.static_image = self.images[0]
			self.is_static_image = True
		else:
			self.image_count = $list_length(self.images)
			
		
		
		for flag in flags:
			if flag == '-':
				pass
			elif flag == 'x':
				self.blocking = True
			elif flag == 't':
				self.tesselation_fixed = True
			else:
				$print("Unrecognized flag in tile '" + id + "': '" + flag + "'")
				
	
	def get_image(self, rc):
		if self.is_static_image:
			return self.static_image
		return self.images[rc % self.image_count]
		