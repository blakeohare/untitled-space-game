class Layer:
	def __init__(self, id, bg_slice, obstacle_slice):
		self.id = id
		self.width = obstacle_slice.width
		self.height = obstacle_slice.height
		self.obs = obstacle_slice
		self.bg = bg_slice
		self.slices = [self.bg, self.obs]
		self.sprites = []
	

class LayerSlice:
	def __init__(self, raw_tile_ids, width, height):
		self.width = width
		self.height = height
		
		# source of truth
		self.tiles_as_grid = [None] * (width * height)
		
		# Just a cache. Set to None to invalidate
		self.tiles_as_list = None
		
		layer_occupied_marker = [False] * (width * height)

		layerIdIndex = 0
		for y in range(height):
			for x in range(width):
				i = y * width + x
				if not layer_occupied_marker[i]:
					id_parts = raw_tile_ids[layerIdIndex].split('#')
					id = id_parts[0]
					if id == '@':
						tile = None
						tile_width = $parse_int(id_parts[1])
						tile_height = $parse_int(id_parts[2])
					else:
						template = TILE_MANIFEST.get(id)
						pcount = $list_length(id_parts)
						if pcount == 1:
							tile_width = template.width
							tile_height = template.height
						else:
							tile_width = $parse_int(id_parts[1])
							if pcount == 3:
								tile_height = $parse_int(id_parts[2])
							else:
								tile_height = tile_width
						
						tile = Tile(template, x, y, tile_width, tile_height)
					
					for tx in range(tile_width):
						for ty in range(tile_height):
							rtx = x + tx
							rty = y  + ty
							ri = rty * width + rtx
							if (ri >= $list_length(layer_occupied_marker)):
								$print("IMMA CRASH!")
								$print(x)
								$print(y)
								$print(tile_width)
								$print(tile_height)
								$print(layer_occupied_marker)
							layer_occupied_marker[ri] = True
							self.tiles_as_grid[ri] = tile
					
					layerIdIndex += 1
	
	def get_tiles_as_list(self):
		output = self.tiles_as_list
		if output == None:
			unique = {}
			for tile in self.tiles_as_grid:
				if tile != None:
					unique[tile.unique_id] = tile
			output = []
			for tile_key in $dictionary_keys(unique):
				$list_add(output, unique[tile_key])
			self.tiles_as_list = output
		return output

