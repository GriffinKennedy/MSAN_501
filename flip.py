import sys
from PIL import Image

#define your flip function here

def flip(img):
    width, height = img.size # we need the w and h to itterate over the pixels of the img
    imgcopy = img.copy() # it's easier to permute a copy than the original.
    imgmatrix = img.load()
    copymatrix = imgcopy.load()


    for x in range(width):
        for y in range(height):
            copymatrix[x,y] = imgmatrix[width -x-1, y]
    return imgcopy

if len(sys.argv)<=1:
    print "missing image filename"
    sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()

imageflipped = flip(img)

img.show()
imageflipped.show()