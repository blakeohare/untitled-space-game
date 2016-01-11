class PlayScene:
	def __init__(self):
		self.map = Map(game_state_get_value('map'))
		start_id = game_state_get_value('start_id')
		start = $dictionary_get_with_default(self.map.areas_by_id, start_id, None)
		if start == None: $print("No start door/waypoint found.")
		
		self.sprites = []
		player = Sprite('player')
		player.x = start.center_x
		player.y = start.center_y
		player.layer = self.map.layers_by_id[start.layer_id]
		
		self.input_target = player
		
		$list_add(self.sprites, player)
	
	def update(self, events, pressed_keys):
		
		v = 1
		if pressed_keys['up']: self.input_target.dy = -v
		elif pressed_keys['down']: self.input_target.dy = v
		if pressed_keys['left']: self.input_target.dx = -v
		elif pressed_keys['right']: self.input_target.dx = v
		
		for sprite in self.sprites:
			sprite.update(self)
		
	def render(self, rc):
		
		sprites_by_layer = {}
		layer_count = $list_length(self.map.layers)
		
		for layer in self.map.layers:
			layer.sprites = [] # CRYTHON-TODO: $list_clear
		
		for sprite in self.sprites:
			$list_add(sprite.layer.sprites, sprite)
		
		screen = GAME_WRAPPER_VARS.screen
		for layer in self.map.layers:
			for slice in layer.slices:
				for tile in slice.get_tiles_as_list():
					patches = tile.render_patches
					if patches == None:
						patches = tile.refresh_render_patches()
					template = tile.template
					image = template.get_image(rc)
					for patch in patches:
						if patch.is_simple:
							$image_blit(screen, image, patch.x, patch.y)
						else:
							$image_blit_partial(screen, image, patch.x, patch.y, patch.start_x, patch.start_y, patch.width, patch.height)
			
			# TODO: sort sprites by y
			for sprite in layer.sprites:
				sprite.render(screen, rc)