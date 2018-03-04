import sys
from PIL import Image
import numpy as np

def read_image(image_name): 
    """
    OpenCV defaults to BGR when it reads an image. The second line swaps blue 
    and red channels otherwise colors will be flipped.
    
    Input:
    image_name - name of image in the global path defined below
    
    Output:
    image that has Blue and Red channels swapped due to OpenCV's default properties
    """
    #os.path.join(image_path, image_name, image_name+'.png')
    im = Image.open(image_name)
    return im

num_grid = 8

def grid_image_template(im):
    score = {}
    row, col = im.shape
    len_of_grid = col/4
    wid_of_grid = row/2
    for i in range(num_grid):
        if i < 4:
            temp_im = np.array(im[0:wid_of_grid, len_of_grid*i:len_of_grid*(i+1)])
            score[i] = len(np.argwhere(temp_im == 255))
            #print len(np.argwhere(temp_im == 255))
            #print np.argwhere(temp_im == 255)[0:2]
            #sys.exit()
        else: #second row
            temp_im = im[wid_of_grid:row, len_of_grid*(i%4):len_of_grid*((i+1)%4)]
            score[i] = len(np.argwhere(temp_im == 255))
        
       # plt.figure()
       # plt.imshow(temp_im)
        
        
    grid_max, highest_score = max(score.items(), key= lambda x: x[1]) 
    
    #print grid_max, highest_score
    
    if grid_max < 4:
        cent = (wid_of_grid/2, (len_of_grid*grid_max+len_of_grid*(grid_max+1))/2)
        temp_im = im[0:wid_of_grid, len_of_grid*grid_max:len_of_grid*(grid_max+1)]
    else: #second row
        cent = ((wid_of_grid+row)/2, (len_of_grid*(grid_max%4)+len_of_grid*((grid_max+1)%4))/2)
        temp_im = im[wid_of_grid:row, len_of_grid*(grid_max%4):len_of_grid*((grid_max+1)%4)]
    
    return temp_im, cent
    
def main():
    # Path variables
    path="/home/pi/Documents/access/camera/"
    print("------------------------ Obtaining Best Template ------------------------")
    if len(sys.argv) == 2:
        image_name = sys.argv[1]+".jpg" 
        print("--> Obtaining template from: "+image_name)
    else:
        print("No input detected in better_template.py...")
        sys.exit()
    
    path_to_image = path+image_name
    im = read_image(path_to_image)
    template, cent = grid_image_template(np.array(im))
    
    #print template.shape[0], template.shape[1]
    template = Image.fromarray(template)
    template.save(path+"template.jpg")
    
    with open('/home/pi/Documents/access/camera/location.txt','a') as my_file:
        my_file.write('%d %d\n'%(cent[0], cent[1]))

    print("------------------------ Done ------------------------")
    
if __name__ == "__main__":
    main()




