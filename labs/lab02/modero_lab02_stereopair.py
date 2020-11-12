#Importing the necessary libraries
import sys
import PIL
import numpy as np
import pandas as pd
from PIL import Image
from scipy import signal

# provide three arguments: the name of the left_image.jpg, 
# right_image.jpg, and the name of the padded_image.jpg
if ( len( sys.argv ) != 4 ):
    print( "usage is: %s left_image.jpg right_image.jpg padded_image.jpg" % (sys.argv[0]) )
    print( "        left_image.jpg is the left image" )
    print( "        right_image.jpg is the right image" )
    print( "        padded_image is the processed image" )
    sys.exit()
    
# load the left and right image
left_im         = Image.open( sys.argv[1] )
left_im_arr     = np.asarray( left_im, np.float )
left_resized    = left_im.resize( (2048, 1020) )

right_im        = Image.open( sys.argv[2] )
right_im_arr    = np.asarray( right_im, np.float )
right_resized   = right_im.resize( (2048, 1020) )

# creating the black  image for stereoscope
rows            = 4096
cols            = 4096
black_array     = np.zeros( [ rows, cols, 3 ], dtype=np.uint8 )
black_array.fill(0)
black           = Image.fromarray( black_array )

#paste
black.paste( left_resized, (1024, 514) )
black.paste( right_resized, (1024, 2562) )
black.save( sys.argv[3]  )
black.show()
