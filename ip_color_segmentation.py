from PIL import Image
import sys
import numpy as np

import math

def colorSeg(f, m, T):

    f = np.array(f)
    print(f.shape)
    xsize = f.shape[0]
    ysize = f.shape[1]

    I = np.zeros((xsize, ysize))
    #f = double(f);
    ar = m[0];
    ag = m[1];
    ab = m[2];

    max_x = 0;
    min_X = 1000000000;

    for i in range(xsize):

        for j in range(ysize):

            zr = np.array(f[i, j, 0]);
            zg = np.array(f[i, j, 1]);
            zb = np.array(f[i, j, 2]);

            D = math.sqrt(math.pow((zr - ar) , 2) + math.pow((zg - ag),2) + math.pow((zb - ab),2))

            # distances = [distances D];
            if max_x < D:
                max_x = D;

            if min_X > D:
                min_X = D;

            if D < T:
                I[i, j] = 255;

    return I


# Path variables
path="C:/Users/Victor/Documents/UMass Amherst/Fall 2017 (senior)/SDP/images/" #"/home/pi/Documents/access/camera/" # path without image name
save_to=path# "/home/pi/Documents/access/camera/" #"" for same directory

# Check input name
if len(sys.argv) < 2:
    print("No input detected!")
    sys.exit("No input detected! Name of the file without extension must be provided as input through console")


file_name = sys.argv[1]

# Load image:
path = path+file_name+".jpg" # assuming jpg extension which is the one that we use when we take a picture

img = Image.open(path)
#img.show()

m = [255*0.14412,255*0.707508,255*0.115358]
T = 0.25*255;

I = colorSeg(img,m,T)
I = Image.fromarray(I).convert('L')
I.show()



