from filter import *

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

img = open(sys.argv)
img.show()
denoised = filter(img, median)
denoised.show()