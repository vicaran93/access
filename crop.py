from PIL import Image
import sys,math,ast

'''
    This program crops an image located at where the variable 'path' specifies. Resulting cropped image is saved at
    the directory where this program lives in .

    Inputs: $python crop.py <width> <height> <[x,y]>
            Width: The width of the template we want to crop (y axis). Integer
            Height: The height of the template we want to crop (x axis). Integer
            [x,y]: Center point where we would like to crop around. Integer array
    The cropping default if there are not inputs are:


'''
# Path variables
path="/home/pi/Documents/access/camera/test1.jpg"
save_to="/home/pi/Documents/access/camera/" #"" for same directory
cropped_img_name="crop_test.jpg"

# Load image:
img = Image.open(path)
xsize,ysize = img.size
print(str(xsize))
print(str(ysize))
# Initializing settings:
#   Read if there are inputs from command line
if len(sys.argv) == 4: #meaning that we have 3 inputs from command line
    print("Inputs detected!")
    width =int(sys.argv[1])
    height = int(sys.argv[2])
    xy = sys.argv[3]
    xy= ast.literal_eval(xy) #'[1,2]' --> [1,2]
else:
    #no inputs at command line
    print("No inputs detected. Using default values.")
    x_center = math.ceil(xsize/2) # check ceil
    y_center = math.ceil(ysize/2)  # check ceil
    width = x_center
    height = x_center
    xy = [x_center,y_center]

# Verify cropping coordinates

x_i = math.ceil(xy[0] - width/2)
if x_i < 0: x_i=0
y_i = math.ceil(xy[1] - height/2)
if y_i < 0: y_i=0
x_f = math.ceil(xy[0] + width/2)
if x_f > xsize: x_f = xsize
y_f = math.ceil(xy[1] + height/2)
if y_f > ysize: y_f = ysize

img2 = img.crop(
    (
        x_i,
        y_i,
        x_f,
        y_f
    )
)
#img2 = img.crop((0, 0, xSize/2, ySize/2))
img2.save(save_to+cropped_img_name)
