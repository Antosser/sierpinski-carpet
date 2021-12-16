from PIL import Image
import PIL
from functools import cache

# @cache
# def isActive(x, y, size):
# 	pixels = 3 ** size
# 	if size == 1:
# 		return True
# 	if (pixels / 3) <= (x + 1) <= (pixels * 2 / 3) and (pixels / 3) <= (y + 1) <= (pixels * 2 / 3):
# 		return False
# 	return isActive(x % (3 ** (size - 1)), y % (3 ** (size - 1)), size - 1)
	

def generate(size):
	pixels = 3 ** size
	im = PIL.Image.new('RGB', (pixels, pixels), 'black')
	color = (255, 255, 255)

	for i in range(pixels):
		for j in range(pixels):
			#if isActive(i, j, size):
			#    im.putpixel((i, j), color)
			
			active = True
			for k in range(2, size + 1):
				pixels = 3 ** k
				x = i % pixels
				y = j % pixels
				if (pixels / 3) <= (x + 1) <= (pixels * 2 / 3) and (pixels / 3) <= (y + 1) <= (pixels * 2 / 3):
					active = False
					break
			if active:
				im.putpixel((i, j), color)
	
	im.save(f'{size}.png')

if __name__ == '__main__':
	generate(int(input('Size: ')))