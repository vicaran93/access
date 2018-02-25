from PIL import Image
import sys
import numpy as np

'''
input should be the name of the file to be converted to BW
'''

# Path variables
path="/home/pi/Documents/access/camera/" #"C:/Users/Victor/Documents/UMass Amherst/Fall 2017/SDP/images/" # path without image name
save_to=path# "/home/pi/Documents/access/camera/" #"" for same directory

file_name = sys.argv[1]

# Load image:
path = path+file_name+".jpg" # assuming jpg extension which is the one that we use when we take a picture

img = Image.open(path)
img.show()

#green = img[:,:,2]
rgb_im = img.convert('RGB')
r, g, b = rgb_im.split()
[x,y] = r.size
[x2,y2] = b.size

#r= np.zeros((x,y))
r=r.point(lambda i: i * 0)
#b= np.zeros((x2,y2))
b=b.point(lambda i: i * 0)
#img[:,:,0] = 0
#img[:,:,2] = 0

#green = img

green_img = Image.merge('RGB', (r, g, b))
green_img.show()
#new_img = np.zeros(img.shape);
#new_img[:,:,2] = green

#ave_green = mean(mean(green));
ave_green =np.mean(g);
#A[np.where(A>2)]
#green(green < ave_green) = 0;

g = np.array(g)
g[np.where(g < ave_green)] = 0

#g = Image.fromarray(g)

#new_img = np.zeros(img.shape);
#new_img[:,:,2] = green;
#green_img_th = Image.merge('RGB', (r, g, b))


#b_w_img = green;
#figure
#imshow(b_w_img)
#title(" B&W img")


#A[np.where(A>2)]
#b_w_img( b_w_img > 0 ) = 255;
#b_w_img[ np.where(b_w_img > 0) ] = 255;
g[ np.where(g > 0) ] = 255;

b_w_img = Image.fromarray(g)
#b_w_img = Image.merge('RGB', (r, g, b))
b_w_img.show()

bw_img_name=file_name+"_bw.jpg"
b_w_img.save(save_to+bw_img_name)
