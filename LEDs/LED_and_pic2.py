
import RPi.GPIO as GPIO
import time,os,sys
sys.path.insert(0,"/home/pi/Documents/access/Image_processing")
from PIL import Image
import numpy as np
#import crop_new
from PIL import ImageFilter

'''
This script blinks green light 10 times using pin 12
'''

def LED_and_img():
    #initialize the GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21,GPIO.OUT)

    if len(sys.argv) < 2:
        sys.exit("No input detected! Name of the file without extension must be provided as input through console")

    file_name = sys.argv[1]
    code = file_name
    file_name = file_name+".jpg"



    print("------------------------ Taking Image ------------------------")
    GPIO.output(21, True)
    print("UV LED on!")
    # time.sleep(30) #0.5
    temp = "raspistill -ISO 400 -ss 160000 -br 80 -co 100 -vf -o ~/Documents/access/camera/" + file_name
    os.system(temp)
    GPIO.output(21, False)
    print("UV LED off and Img taken")
    print("------------------------ Done ------------------------")

    GPIO.cleanup()

    # Open image and convert to numpy array
    path = "/home/pi/Documents/access/camera/"
    # Load image:
    path_new = path + file_name
    path_to_send = path + code
    img = Image.open(path_new)

    img = np.array(img, dtype=np.float64)
    crop(img, path_to_send)


def crop(np_img, path_to_send):
    row, col, channel = np_img.shape
    midHeight = row/2.
    midWidth = col/2.
    
    cropped_img = np_img[int(0.5*midHeight):int(1.5*midHeight), int(0.5*midWidth):int(1.5*midWidth), :]
    
    r = Image.fromarray(np_img[:][:][0]).convert('L')
    g = Image.fromarray(np_img[:][:][1]).convert('L')
    b = Image.fromarray(np_img[:][:][2]).convert('L')
    img2= Image.merge('RGB', (r, g, b))

    cropped_img_name = path_to_send+"_cropped.jpg"
    print(cropped_img_name)
    img2.save(cropped_img_name)

    ip(cropped_img,path_to_send)

def colorSeg(f, m, T):
    '''
    Using Numpy and vectorizing 3D distance equation

    :param f: Image in obtained from  Image.open(path)
    :param m: vector of size 3 having mean values for R G B.
    :param T: Threshold or radious of the sphere in the RGB space
    :return: Returns matrix I for BW img --> Usin
    '''

    #rgb_im = f.convert('RGB')
    #r, g, b = rgb_im.split()

    r = f[:][:][0]
    g = f[:][:][1]
    b = f[:][:][2]

    # Average R G B values on the spheres
    ar = m[0]
    ag = m[1]
    ab = m[2]

    # Converting to Numpy arrays
    #r = np.array(r)
    #g = np.array(g)
    #b = np.array(b)

    # From distance equation D = sqrt(math.pow((zr - ar) , 2) + math.pow((zg - ag),2) + math.pow((zb - ab),2)) in a vectorized version
    # (r - ar)^2  (g - ag)^2  (b - ab)^2
    I = pow((r - ar), 2)
    A = pow((g - ag), 2)
    B = pow((b - ab), 2)
    C = pow(T, 2) - A - B
    # now we can use the inequality equation derived from the 3d distance eq and say that I < C to bei n the sphere

    # create zeros matrix
    rows = r.shape[0]
    cols = r.shape[1]
    g = np.zeros((rows, cols))

    # Assign white pixels to pixels within threshold
    g[np.where(I < C)] = 255

    return g


def ip(np_img,path_to_send):
    # Path variables
    path = "/home/pi/Documents/access/camera/"  # "C:/Users/Victor/Documents/UMass Amherst/Fall 2017 (senior)/SDP/images/" #"/home/pi/Documents/access/camera/" # path without image name
    save_to = path  # "/home/pi/Documents/access/camera/" #"" for same directory

    # m = [255*0.14412,255*0.707508,255*0.115358]
    # T = 0.25*255;

    m = [255 * 0.246405, 255 * 0.879411765, 255 * 0.061];
    T = 0.20 * 255;

    I_np = colorSeg(np_img, m, T)
    I = Image.fromarray(I_np).convert('L')
    # I.show()

    b_w_img_filtered = I.filter(ImageFilter.MedianFilter(size=7))
    b_w_img_filtered = b_w_img_filtered.filter(ImageFilter.MedianFilter(size=7))
    b_w_img_filtered = b_w_img_filtered.filter(ImageFilter.MedianFilter(size=7))
    b_w_img_filtered = b_w_img_filtered.filter(ImageFilter.MedianFilter(size=7))

    bw_img_path = path_to_send + "_bw.jpg"
    # I.save(save_to+bw_img_name)
    b_w_img_filtered.save(bw_img_path)
    print("------------------------ Done ------------------------")

    template, cent = grid_image_template(np.array(b_w_img_filtered)) #I_np)

    # print template.shape[0], template.shape[1]
    template = Image.fromarray(template).convert('L')
    template.save(path + "template.jpg")

    with open('/home/pi/Documents/access/camera/location.txt', 'a') as my_file:
        my_file.write('%d %d\n' % (cent[0], cent[1]))

    print("------------------------ Done ------------------------")



def grid_image_template(im):
    num_grid = 8
    score = {}
    row, col = im.shape
    len_of_grid = col / 4
    wid_of_grid = row / 2
    for i in range(num_grid):
        if i < 4:
            temp_im = np.array(im[0:wid_of_grid, len_of_grid * i:len_of_grid * (i + 1)])
            score[i] = len(np.argwhere(temp_im == 255))
            # print len(np.argwhere(temp_im == 255))
            # print np.argwhere(temp_im == 255)[0:2]
            # sys.exit()
        else:  # second row
            temp_im = im[wid_of_grid:row, len_of_grid * (i % 4):len_of_grid * ((i + 1) % 4)]
            score[i] = len(np.argwhere(temp_im == 255))

            # plt.figure()
            # plt.imshow(temp_im)

    grid_max, highest_score = max(score.items(), key=lambda x: x[1])

    # print grid_max, highest_score

    if grid_max < 4:
        cent = (wid_of_grid / 2, (len_of_grid * grid_max + len_of_grid * (grid_max + 1)) / 2)
        temp_im = im[0:wid_of_grid, len_of_grid * grid_max:len_of_grid * (grid_max + 1)]
    else:  # second row
        cent = ((wid_of_grid + row) / 2, (len_of_grid * (grid_max % 4) + len_of_grid * ((grid_max + 1) % 4)) / 2)
        temp_im = im[wid_of_grid:row, len_of_grid * (grid_max % 4):len_of_grid * ((grid_max + 1) % 4)]

    return temp_im, cent



if __name__ == "__main__":
    LED_and_img()
