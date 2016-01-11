class ImageLibrary:
	def __init__(self):
		pass

	def get(self, path):
		return self.images[path]
		
IMAGES = ImageLibrary()

def draw_image(img, x, y, screen = None):
	if screen == None: screen = GAME_WRAPPER_VARS.screen
	$image_blit(screen, img, x, y)

