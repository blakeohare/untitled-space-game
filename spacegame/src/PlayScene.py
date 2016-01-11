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
		player.layer = start.layer_id
		self.input_target = player
		
		$list_add(self.sprites, player)
	
	def update(self, events, pressed_keys):
		
		v = 4
		if pressed_keys['up']: self.input_target.dy = -v
		elif pressed_keys['down']: self.input_target.dy = v
		if pressed_keys['left']: self.input_target.dx = -v
		elif pressed_keys['right']: self.input_target.dy = v
		
		
		for sprite in self.sprites:
			sprite.update(self)
		
				
	
	def render(self, rc):
		
		sprites_by_layer = {}
		layer_count = $list_length(self.map.layers)
		
		for i in range(layer_count):
			sprites_by_layer[self.map.layer_ids[i]] = []
		
		for sprite in self.sprites:
			$list_add(sprites_by_layer[sprite.layer], sprite)
		
		screen = GAME_WRAPPER_VARS.screen
		for i in range(layer_count):
			layer = self.map.layers[i]
			layer_id = self.map.layer_ids[i]
			sprites = sprites_by_layer[layer_id]
			for sublayer in layer:
				for tile in sublayer.get_tiles_as_list():
					
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
			for sprite in sprites:
				sprite.render(screen, rc)