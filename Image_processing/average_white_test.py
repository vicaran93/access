
from PIL import Image
import sys
import numpy as np
from datetime import datetime


def average_white(img):
    img_np = np.array(img)
    rows = img_np.shape[0]
    cols = img_np.shape[1]
    num_whites = np.count_nonzero(img_np)

    avr = num_whites / (rows*cols)
    return avr



def main():
    '''
    ::arg: From console, input argument with the name of the BLACK AND WHITE  image to analyze
    :return: Warn if threshold is not met.
    '''

    # Path variables
    path="/home/pi/Documents/access/camera/"#"C:/Users/Victor/Documents/UMass Amherst/Fall 2017 (senior)/SDP/images/" # path without image name
    save_to=path# "/home/pi/Documents/access/camera/" #"" for same directory

    # Check input name
    if len(sys.argv) < 2:
        print("No input detected!")
        sys.exit("No input detected! Name of the file without extension must be provided as input through console")


    file_name = sys.argv[1]

    # Load image:
    path = path+file_name+".jpg" # assuming jpg extension which is the one that we use when we take a picture

    img = Image.open(path)

    avr_w  = average_white(img)

    print("Average white pixels amount: ") #+str(avr_w)
    print("{0:.2f}".format(round(avr_w, 2)))


    '''
    if avr_w > MIN_WHITE_AVERAGE and avr_w < MAX_WHIRE_AVERAGE:
        return 1
    else:
        return 0

    '''




if __name__ == '__main__':
    main()


