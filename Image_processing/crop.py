from PIL import Image
import sys,math,ast

'''
    This program crops an image located at where the variable 'path' specifies (Camera folder). Resulting cropped image is saved at
   'save_to' variable . The cropped image will be named as its original name plus the '_cropped.jpg'string.

    Inputs: $python crop.py <file_name> <width> <height> <[x,y]>
	    file_name: This is the name of the file without the file type extension (i.e. .jpg)
            Width: The width of the template we want to crop (y axis). Integer
            Height: The height of the template we want to crop (x axis). Integer
            [x,y]: Center point where we would like to crop around. Integer array

    Inputs: $python crop.py <file_name>
           width = x_center
           height = y_center
    	   xy = [x_center,y_center]

    If there are not inputs:
	   Same as previous settings but file_name = "test1.jpg"


'''
# Path variables
path="/home/pi/Documents/access/camera/" # path without image name 
save_to="/home/pi/Documents/access/camera/" #"" for same directory
#cropped_img_name="crop_test.jpg"


# Initializing settings:
#   Read if there are inputs from command line
if len(sys.argv) == 5: #meaning that we have 4 inputs from command line 'filename width height [x,y]'
    #print("4 inputs detected!")
    file_name = sys.argv[1]
    width =int(sys.argv[2])
    height = int(sys.argv[3])
    xy = sys.argv[4]
    xy= ast.literal_eval(xy) #'[1,2]' --> [1,2]
elif len(sys.argv) == 2:
    # Meaning  that we have only one input so it has only the name of the file
    #print("One input detected. Using input as the file name and using default cropping settings")
    file_name = sys.argv[1]
    # Load image:
    path = path+file_name+".jpg" # assuming jpg extension which is the one that we use when we take a picture
    img = Image.open(path)
    xsize,ysize = img.size
    #print(str(xsize))
    #print(str(ysize))
    x_center = math.ceil(xsize/2) # check ceil
    y_center = math.ceil(ysize/2)  # check ceil
    width = x_center
    height = y_center
    xy = [x_center,y_center]
else:
    #no inputs at command line
    print("No inputs detected. Using default values. Using filename = 'test1.jpg'")
    file_name = "test1"
    # Load image:
    path = path+file_name+".jpg" # assuming jpg extension which is the one that we use when we take a picture
    img = Image.open(path)
    xsize,ysize = img.size
    #print(str(xsize))
    #print(str(ysize))
    x_center = math.ceil(xsize/2) # check ceil
    y_center = math.ceil(ysize/2)  # check ceil
    width = x_center
    height = y_center
    xy = [x_center,y_center]


# Verify cropping coordinates
print("------------------------ Image Processing ------------------------")
print(" -> Cropping image: "+file_name)
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
cropped_img_name=file_name+"_cropped.jpg"
img2.save(save_to+cropped_img_name)


