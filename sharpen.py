from filter import *

def laplace(region):
    if (len(region) == 9):
        me, N, S, E, W = region[0:5]
        x = (N + S + E + W) - 4 * me
        return x
    else:
        return region[0]


def minus(A, B):
    '''the purpose of this function is to take the matrix of our original image and the matrix of our image from our
    edges function and suctract the two. then apply this new matrix to our copied image.'''
    width, height = img.size  # we need the w and h to itterate over the pixels of the img
    imgcopy = img.copy()  # it's easier to permute a copy than the original.
    A_imgmatrix = img.load()
    B_imgmatrix = edges.load()
    copymatrix = imgcopy.load()

    for x in range(width):
        for y in range(height):
            copymatrix[x,y] = A_imgmatrix[x,y] - B_imgmatrix[x,y] #subtract the two matrix.

    return imgcopy



img = open(sys.argv)
img.show()#print original

edges = filter(img, laplace)
edges.show() # print the edges image

minus = minus(img, edges)
minus.show() #show the minus



