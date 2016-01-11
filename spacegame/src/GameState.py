class GameState:
	def __init__(self):
		self.room_state = {}
		self.unsaved_state = {}
		self.saved_state = {}
	
	
	def set_value(self, key, value):
		self.room_state[key] = value
	
	def get_value(self, key):
		value = $dictionary_get_with_default(self.room_state, key, None)
		if value != None: return value
		value = $dictionary_get_with_default(self.unsaved_state, key, None)
		if value != None: return value
		value = $dictionary_get_with_default(self.saved_state, key, None)
		return value
	
	def save_room(self):
		for key in $dictionary_keys(self.room_state):
			self.unsaved_state[key] = self.room_state[key]
		self.room_state = {}
	
	def restart_room(self):
		self.room_state = {}
	
	def save_game(self):
		self.save_room()
		for key in $dictionary_keys(self.unsaved_state):
			self.saved_state[key] = self.unsaved_state[key]
		self.unsaved_state = {}
		
		# TODO: save saved_state to file or something.
	

def game_state_set_value(key, value):
	GAME_WRAPPER_VARS.game_state.set_value(key, value)

def game_state_get_value(key):
	return GAME_WRAPPER_VARS.game_state.get_value(key)