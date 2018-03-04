from PIL import Image
import sys
import numpy as np
from PIL import ImageFilter
import math

def colorSeg(f, m, T):
    '''
    Using Numpy and vectorizing 3D distance equation

    :param f: Image in obtained from  Image.open(path)
    :param m: vector of size 3 having mean values for R G B.
    :param T: Threshold or radious of the sphere in the RGB space
    :return: Returns matrix I for BW img --> Usin
    '''


    rgb_im = f.convert('RGB')
    r, g, b = rgb_im.split()

    # Average R G B values on the spheres
    ar = m[0]
    ag = m[1]
    ab = m[2]

    # Converting to Numpy arrays
    r = np.array(r)
    g = np.array(g)
    b = np.array(b)

    # From distance equation D = sqrt(math.pow((zr - ar) , 2) + math.pow((zg - ag),2) + math.pow((zb - ab),2)) in a vectorized version
    # (r - ar)^2  (g - ag)^2  (b - ab)^2
    I = pow((r - ar),2)
    A = pow((g - ag),2)
    B = pow((b - ab),2)
    C = pow(T,2) - A - B
    # now we can use the inequality equation derived from the 3d distance eq and say that I < C to bei n the sphere

    # create zeros matrix
    rows = r.shape[0]
    cols = r.shape[1]
    g = np.zeros((rows, cols))

    # Assign white pixels to pixels within threshold
    g[np.where(I < C)] = 255

    return g


# Path variables
path="/home/pi/Documents/access/camera/" # "C:/Users/Victor/Documents/UMass Amherst/Fall 2017 (senior)/SDP/images/" #"/home/pi/Documents/access/camera/" # path without image name
save_to=path # "/home/pi/Documents/access/camera/" #"" for same directory

# Check input name
if len(sys.argv) < 2:
    print("No input detected!")
    sys.exit("No input detected! Name of the file without extension must be provided as input through console")


file_name = sys.argv[1]
print(" -> Color segmentation (RGB to BW): "+file_name)

# Load image:
path = path+file_name+".jpg" # assuming jpg extension which is the one that we use when we take a picture
img = Image.open(path)

#img.show()

#m = [255*0.14412,255*0.707508,255*0.115358]
#T = 0.25*255;

m = [255*0.246405,255*0.879411765,255*0.061];
T = 0.20*255;

I = colorSeg(img,m,T)
I = Image.fromarray(I).convert('L')
#I.show()

b_w_img_filtered = I.filter(ImageFilter.MedianFilter(size=7))
b_w_img_filtered = b_w_img_filtered.filter(ImageFilter.MedianFilter(size=7))
b_w_img_filtered = b_w_img_filtered.filter(ImageFilter.MedianFilter(size=7))
b_w_img_filtered = b_w_img_filtered.filter(ImageFilter.MedianFilter(size=7))

bw_img_name=file_name+"_bw.jpg"
#I.save(save_to+bw_img_name)
b_w_img_filtered.save(save_to+bw_img_name)
print("------------------------ Done ------------------------")
