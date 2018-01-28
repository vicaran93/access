from PIL import Image
import sys
import numpy as np
from PIL import ImageFilter

'''
input should be the name of the file to be converted to BW
'''

# Path variables
path="/home/pi/Documents/access/camera/" #"C:/Users/Victor/Documents/UMass Amherst/Fall 2017 (senior)/SDP/images/" #"/home/pi/Documents/access/camera/" # path without image name
save_to=path #"/home/pi/Documents/access/camera/" #"" for same directory

# Check input name
if len(sys.argv) < 2:
    print("No input detected!")
    sys.exit("No input detected! Name of the file without extension must be provided as input through console")

file_name = sys.argv[1]

# Load image:
path = path+file_name+".jpg" # assuming jpg extension which is the one that we use when we take a picture

img = Image.open(path)
img.show()

rgb_im = img.convert('RGB')
r, g, b = rgb_im.split()

# Filter Green and Blue channels  -------------
#Green
# Matlab: ave_green = mean(mean(green));
ave_green =np.mean(g);

# Matlab: green(green < ave_green) = 0;
g = np.array(g)
g[np.where(g < ave_green)] = 0

#Blue
ave_blue =np.mean(b);
b2 = np.array(b)
b2[np.where(b2 < ave_blue)] = 0

#New Green Channel (less error)
newGreen=np.abs(g-b2*0.7)
# Matlab: newGreen1(new_img < 0.25) = 0;
newGreen[np.where(newGreen < 0.25*255)] = 0


newGreen = Image.fromarray(newGreen).convert('L') # to be able to merge r,g,b "need to convert each channel into a luminosity channel"

# Deleting Red and Blue channels
r=r.point(lambda i: i * 0)
b=b.point(lambda i: i * 0)

# Create image with new channels
green_img = Image.merge('RGB', (r, newGreen, b))
green_img.show()


newGreen = np.array(newGreen) #convert to numpy array
newGreen[ np.where(newGreen > 0) ] = 255;

b_w_img = Image.fromarray(newGreen)
b_w_img.show()

# Apply median filter

b_w_img_filtered = b_w_img.filter(ImageFilter.MedianFilter(size=7))
b_w_img_filtered = b_w_img_filtered.filter(ImageFilter.MedianFilter(size=7))
b_w_img_filtered = b_w_img_filtered.filter(ImageFilter.MedianFilter(size=7))
b_w_img_filtered = b_w_img_filtered.filter(ImageFilter.MedianFilter(size=7))

b_w_img_filtered.show()

bw_img_name=file_name+"_bw.jpg"
b_w_img_filtered.save(save_to+bw_img_name)
