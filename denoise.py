import sys
from PIL import Image

#define your blur function here

def getpixel(img, x, y):
    '''this function is to get the coordinates of each pixel in the image'''
    imgmatrix = img.load()
    width, height = img.size
    if x < 0 or x > width - 1 or y < 0 or y > height - 1: #this line is a buffer to fix possible problems the region3x3 function could cause.
        return None #we want to return None if the pixel is outside the image range.
    else:
        return imgmatrix[x,y]

def region3x3(img, x, y):
    '''goal: return list of values for a 3X3 region of each pixel'''
    me = getpixel(img, x, y)
    N = getpixel(img, x, y - 1) #these -1 are why we needed the caviot in the aboce function
    S = getpixel(img, x, y + 1)
    E = getpixel(img, x + 1, y)
    W = getpixel(img, x - 1, y)
    NW = getpixel(img, x - 1, y - 1)
    NE = getpixel(img, x + 1, y - 1)
    SW = getpixel(img, x - 1, y + 1)
    SE = getpixel(img, x + 1, y + 1)

    full_list = [me, N, S, E, W, NW, NE, SW, SE]
    appended_list = []
    for values in full_list: # this for loop filters out the none values so I can later take the average without issues
        if values is not None:
            appended_list.append(values)

    return appended_list


def median(region):
    '''take the median of the 3X3 region and return the median number.'''
    region.sort()
    if len(region) < 1:
        return None
    elif len(region) % 2 == 1:
        x = int(len(region)/2) #using int as a floor function can do int then add one for a ceiling
        w = region[x]
        return w
    else:
        y = (len(region)/2)-1
        z = len(region)/2

        output = round((region[y] + region[z]) /2, 3)
        return output



def denoise(img):
    '''input an image and blur it by first copying the image then changing the pixel values of the copy to the mean of the mapping from the original image. return copied image.'''
    width, height = img.size # we need the w and h to itterate over the pixels of the img
    imgcopy = img.copy() # it's easier to permute a copy than the original.
    imgmatrix = img.load()
    copymatrix = imgcopy.load()

    for x in range(width):
        for y in range(height):
            r = region3x3(img, x, y)
            copymatrix[x,y] = int(median(r)) #pixels need to be integers

    return imgcopy



if len(sys.argv)<=1:
    print "missing image filename"
    sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")

imageblurred = denoise(img)

img.show()
imageblurred.show()

