class GameWrapperVars:
	def __init__(self):
		self.screen = None
		self.exit_please = False
		self.game_state = GameState() # TODO: game load 

GAME_WRAPPER_VARS = GameWrapperVars()

class GameWrapper:
	def __init__(self):
		self.initialized = False
		self.next = self
		self.active_scene = None
		self.pressed_keys = {
			'up': False,
			'down': False,
			'left': False,
			'right': False,
		}
	
	def update(self, events):
		for e in events:
			if e.type == 'quit':
				GAME_WRAPPER_VARS.exit_please = True
			elif e.type == 'keydown':
				self.pressed_keys[e.key] = True
			elif e.type == 'keyup':
				self.pressed_keys[e.key] = False
		
		if GAME_WRAPPER_VARS.exit_please:
			self.next = None
			self.active_scene = None
		elif self.initialized:
			self.active_scene.update(events, self.pressed_keys)
		else:
			# wait until initialized
			pass
	
	def render(self, screen, images, rc, is_primary):
		if not self.initialized:
			GAME_WRAPPER_VARS.screen = screen
			
			scaled_images = {}
			for key in $dictionary_keys(images):
				image = images[key]
				scaled_image = $image_scale(image, $image_width(image) * 3, $image_height(image) * 3)
				scaled_images[key] = scaled_image
			
			IMAGES.images = scaled_images
			
			TILE_MANIFEST.init()
			
			self.initialized = True
			game_state_set_value('map', 'base')
			game_state_set_value('start_id', 'START')
			
			self.active_scene = PlayScene()
			
			
		elif self.active_scene == None:
			pass
		else:
			self.active_scene.render(rc)

