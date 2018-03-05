from PIL import Image
import sys
import numpy as np
from PIL import ImageFilter
import matplotlib.pyplot as plt

path_to_image = r"C:\Users\Hassaan\Desktop\School related\Fall 2017\SDP/2018-02-22_1856_cropped.jpg"
im = np.asarray(Image.open(path_to_image), dtype=np.float32)
midHeight, midWidth, channels = im.shape

midHeight = midHeight/2.
midWidth = midWidth/2.

print 0.5*midHeight, 1.5*midHeight
print 0.5*midWidth, 1.5*midWidth

plt.imshow(im)
cropped_img = im[int(0.5*midHeight):int(1.5*midHeight), int(0.5*midWidth):int(1.5*midWidth), :]
plt.figure()
plt.imshow(cropped_img)