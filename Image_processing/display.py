import time
import pygame
import numpy as np
import sys
from PIL import Image

'''
    This program displays a picture stored in the raspberry pi in the Documents/access/camera folder.
    Input: Name of the image without extension

 '''

# Path variables
path = "/home/pi/Documents/access/camera/"  # "C:/Users/Victor/Documents/UMass Amherst/Fall 2017 (senior)/SDP/images/" # path without image name

# Check input name
if len(sys.argv) < 2:
	print("No input detected!")
	sys.exit("No input detected! Name of the file without extension must be provided as input through console")

file_name = sys.argv[1]

# Load image:
path = path + file_name + ".jpg"  # assuming jpg extension which is the one that we use when we take a picture

img = Image.open(path)
img_np = np.array(img)
rows = img_np.shape[0]
cols = img_np.shape[1]
w = 700
h = 500
transform_x = w #600 #648 #how wide to scale the jpg when replaying
transfrom_y = h #486 #how high to scale the jpg when replaying
offset_x = 20 #how far off to left corner to display photos
offset_y = 10 #how far off to left corner to display photos

try:
	pygame.init()
	screen = pygame.display.set_mode() #(w,h),pygame.FULLSCREEN)
	pygame.display.set_caption(file_name)
	#pygame.mouse.set_visible(False) #hide the mouse cursor
	#filename = image.jpg
	img=pygame.image.load(path) #filename
	img = pygame.transform.scale(img,(transform_x,transfrom_y))
	screen.blit(img,(offset_x,offset_y))
	pygame.display.flip() # update the display
	time.sleep(3) # pause
finally:
	pygame.quit()
