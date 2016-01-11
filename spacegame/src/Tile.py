TILE_ID_ALLOC = [0]

class Tile:
	def __init__(self, template, x, y, width, height):
		self.template = template
		self.is_blocking = template.is_blocking
		self.id = template.id
		TILE_ID_ALLOC[0] += 1
		self.unique_id = TILE_ID_ALLOC[0]
		self.x = x
		self.y = y
		self.width = width
		self.height = height
	
		self.render_patches = None

	def refresh_render_patches(self):
		heights = []
		widths = []
		xcoords = []
		ycoords = []
		xstarts = []
		ystarts = []
		template = self.template
		twidth = template.width
		theight = template.height
		x = self.x
		y = self.y
		width = self.width
		height = self.height
		if not template.tesselation_fixed:
			if x % twidth != 0:
				excess = x % twidth
				$list_add(xcoords, x)
				$list_add(xstarts, excess)
				$list_add(widths, twidth - excess)
				x += widths[0]
				width -= widths[0]
			if y % theight != 0:
				excess = y % theight
				$list_add(ycoords, y)
				$list_add(ystarts, excess)
				$list_add(heights, theight - excess)
				y += heights[0]
				height -= heights[0]
		
		while width >= twidth:
			$list_add(widths, None)
			$list_add(xcoords, x)
			$list_add(xstarts, 0)
			x += twidth
			width -= twidth
		if width > 0:
			$list_add(widths, width)
		
		while height >= theight:
			$list_add(heights, None)
			$list_add(ycoords, y)
			$list_add(ystarts, 0)
			y += theight
			height -= theight
		if height > 0:
			$list_add(heights, height)
		
		patches = []
		
		cols = $list_length(widths)
		rows = $list_length(heights)
		x = 0
		while x < cols:
			y = 0
			while y < rows:
				width = widths[x]
				height = heights[y]
				is_simple = width == None and height == None
				if width == None: width = twidth
				if height == None: height = theight
				$list_add(patches, RenderPatch(is_simple, xcoords[x], ycoords[y], xstarts[x], ystarts[y], width, height))
				y += 1
			x += 1
		
		self.patches = patches
		return patches
		
class RenderPatch:
	def __init__(self, is_simple, x, y, start_x, start_y, width, height):
		self.is_simple = is_simple
		self.x = x * 24
		self.y = y * 24
		self.start_x = start_x * 24
		self.start_y = start_y * 24
		self.width = width * 24
		self.height = height * 24

