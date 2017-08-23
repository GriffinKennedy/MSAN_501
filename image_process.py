import sys
from PIL import Image
if len(sys.argv) != 2:
    print"$ python view.py imagefilename"
    sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L") #grayscale
img.show()
