from PIL import Image
import sys
import numpy as np
from PIL import ImageFilter
import math

def crop(np_img,path_to_send):
    x,y,z = np_img.shape
    midHeight = x//2
    midWidth = y//2
    cropped_img = np_img[int(0.5*midHeight):int(1.5*midHeight)][int(0.5*midWidth):int(1.5*midWidth)][:]
    
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


def ip(np_img):
    # Path variables
    m = [255 * 0.246405, 255 * 0.879411765, 255 * 0.061];
    T = 0.20 * 255;

    I_np = colorSeg(np_img, m, T)
    I = Image.fromarray(I_np).convert('L')
    b_w_img_filtered = I.filter(ImageFilter.MedianFilter(size=7))
    b_w_img_filtered = b_w_img_filtered.filter(ImageFilter.MedianFilter(size=7))
    b_w_img_filtered = b_w_img_filtered.filter(ImageFilter.MedianFilter(size=7))
    b_w_img_filtered = b_w_img_filtered.filter(ImageFilter.MedianFilter(size=7))

    template, cent = grid_image_template(np.array(b_w_img_filtered)) #I_np)

    template = Image.fromarray(template)#.convert('L')
    
    
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

def main():
    path_to_image = r"C:\Users\Hassaan\Desktop\School related\Fall 2017\SDP\Real data\ID 11/8888_cropped_bw.jpg"
    im = Image.open(path_to_image)
    ip()
    
if __name__=="__main__":
    main()



