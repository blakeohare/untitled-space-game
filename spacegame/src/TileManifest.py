class TileManifest:
	def __init__(self):
		self.tiles = None
	
	def init(self):
		self.tiles = {}
		for file in ['tiles/manifest.txt']:
			for line in $string_split($read_text_resource(file), '\n'):
				line = $string_trim(line)
				if $string_length(line) == 0 or line[0] == '#':
					pass
				else:
					parts = $string_split(line, '\t')
					id = parts[0]
					size = $string_split(parts[1], ',')
					flags = parts[2]
					images = $string_split(parts[3], ',')
					self.tiles[id] = TileTemplate(id, size, flags, images)
	
	def get(self, id):
		return self.tiles[id]


TILE_MANIFEST = TileManifest()