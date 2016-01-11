
class Map:
	def __init__(self, map_id):
		self.tiles = None
		self.width = None
		self.height = None
		self.areas_by_id = {}
		self.layers_by_id = {}
		
		file_path = 'maps/' + map_id + '.txt'
		content = $read_text_resource(file_path)
		kvp = {}
		for line in $string_split(content, '\n'):
			parts = $string_split(line, ':')
			if $list_length(parts) > 1:
				key = $string_lower($string_trim(parts[0]))
				value = parts[1]
				for i in range(2, $list_length(parts)):
					value += ":" + parts[i]
				kvp[key] = $string_trim(value)
		
		widthStr = $dictionary_get_with_default(kvp, 'width', None)
		heightStr = $dictionary_get_with_default(kvp, 'height', None)
		layersStr = $dictionary_get_with_default(kvp, 'layers', None)
		
		if widthStr == None: $print("No width defined for " + map_id)
		if heightStr == None: $print("No height defined for " + map_id)
		if layersStr == None: $print("No layer order defined for " + map_id)
		
		areaStr = $string_trim($dictionary_get_with_default(kvp, 'areas', ''))
		if $string_length(areaStr) > 0:
			for area in $string_split(areaStr, ','):
				parts = $string_split(area, '|')
				id = $string_trim(parts[0])
				layer = $string_trim(parts[1])
				x = $parse_int(parts[2])
				y = $parse_int(parts[3])
				width = $parse_int(parts[4])
				height = $parse_int(parts[5])
				self.areas_by_id[id] = Waypoint(id, layer, x, y, width, height)
		
		self.layers = []
		
		width = $parse_int(widthStr)
		height = $parse_int(heightStr)
		
		self.width = width
		self.height = height
		
		for layer_id in $string_split(layersStr, ','):
			layer_id = $string_trim(layer_id)
			if $string_length(layer_id) > 0:
				layerAboveIds = $string_split(kvp['layer-' + layer_id + '-obs'], ',')
				layerBelowIds = $string_split(kvp['layer-' + layer_id + '-bg'], ',')
				layerAbove = LayerSlice(layerAboveIds, width, height)
				layerBelow = LayerSlice(layerBelowIds, width, height)
				
				layer = Layer(layer_id, layerBelow, layerAbove)
				$list_add(self.layers, layer)
				self.layers_by_id[layer_id] = layer
			