from filter import *

def avg(region):
    '''take the avg of the 3X3 region and return the agerage number'''
    x = sum(region)/len(region)

    return x

img = open(sys.argv)
img.show()
blurred = filter(img, avg)
blurred.show()