# importing necessary files
import sys
import math
import numpy as np
from PIL import Image

if len( sys.argv ) != 4:
    print( "usage is: %s image_in resized_im image_out" % (sys.argv[0]) )
    print( "        smaller values make detection more sensitive" )
    sys.exit()
    
# load the image
im          = Image.open( sys.argv[1] )

# determining the dimensions of the image
test_arr = np.asarray( im, np.float)
shape    = test_arr.shape
print(test_arr.shape)

# resizing the image
dim2 = int( (shape[0]/shape[1]) * 1024  )
im_resized  = im.resize( (1024, dim2) )

# obtaining the image array
im_arr      = np.asarray( im_resized, np.float )

# saving the resized image
im_resized.save( sys.argv[2]  )

# creating a 2048 by 2048 black image
black_img_array = np.zeros( [ 2048, 2048, 3 ], dtype=np.uint8 )
black_img_array.fill(0)

N     = 2048
d     = 256
delta = np.pi/N
z     = d

phi   = -(np.pi)/2
for i in range (N+1):
    
    theta = -(np.pi)/2
    for j in range (N+1):
    
        r = z/( np.cos(phi) * np.cos(theta) )
        x = r * np.cos(phi) * np.sin(theta)
        y = r * np.sin(phi)
        
        # converting to PICS. 512 and 317 are the PICS coordinates of the center of the image
        col = x + 512
        row = y + 307
        
        if ( col >= 0 and col <= 1024 and row >=0 and row <= 614):
            black_img_array[ i, j ] = im_arr[ int( row ), int( col )   ]
        
        theta = theta + delta
        
    phi = phi + delta

black_img       = Image.fromarray( black_img_array )
black_img.save( sys.argv[3]  )
black_img.show()

