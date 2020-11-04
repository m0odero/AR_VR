#Importing the necessary libraries

import numpy as np
import sys
import PIL
from PIL import Image

# The four points chosen from the distorted image
# (c1, d1), c2, d2), (c3, d3), (c4, d4)
c1 = 413; d1 = 209
c2 = 439; d2 = 428
c3 = 185; d3 = 428
c4 = 314; d4 = 209

# The four points of the processed image are the corners of a rectangle
# (a1, b1) is the upper left 
# (a2, b2) is the upper right
# (a3, b3) is the lower left
# (a4, b4) is the lower right
# (c1, d1) becomes (a1, b1), (c2, d2) becomes (a2, b2), 
# (c3, d3) becomes (a3, b3), (c4, d4) becomes (a3, b3)
a1 = 320; b1 = 200
a2 = 320; b2 = 820
a3 = 200; b3 = 820
a4 = 200; b4 = 200

# The expression: A.h = b
# The expression in inverse: A_prime.b = h

# The matrix 
A = np.array( [[c1, d1, 1, 0, 0, 0, -1*a1*c1, -1*a1*d1],
                [0, 0, 0, c1, d1, 1, -1*b1*c1, -1*b1*d1], 
                [c2, d2, 1, 0, 0, 0, -1*a2*c2, -1*a2*d2],
                [0, 0, 0, c2, d2, 1, -1*b2*c2, -1*b2*d2],
                [c3, d3, 1, 0, 0, 0, -1*a3*c3, -1*a3*d3],
                [0, 0, 0, c3, d3, 1, -1*b3*c3, -1*b3*d3],
                [c4, d4, 1, 0, 0, 0, -1*a4*c4, -1*a4*d4],
                [0, 0, 0, c4, d4, 1, -1*b4*c4, -1*b4*d4]   
                ] )

# The inverse of the matrix
A_prime = np.linalg.inv(A)

# The vector b
b = np.array( [[a1], 
               [b1], 
               [a2], 
               [b2], 
               [a3], 
               [b3], 
               [a4], 
               [b4]
               ] )

# Solving for h
h = np.dot(A_prime, b)

# adding 1 to make the values 9
one = np.array( [[1]] )
h = np.vstack( (h,one) )

# Reshaping the 8 by 1 column vesctor to a 3 by 3 matrix
H = h.reshape( (3,3) )

# obtaining the inverse of H
H_prime = np.linalg.inv(H)

# load the distorted image
distorted_im = Image.open( sys.argv[1] )
distorted_im_arr = np.asarray( distorted_im, np.float )

# obtaining the size (rows and columns) of the distorted image
rows = distorted_im_arr.shape[0]
cols = distorted_im_arr.shape[1]

print("rows: ",rows, "columns: ", cols)
# creating the black  image
black_img_array = np.zeros([rows,cols,3],dtype=np.uint8)
black_img_array.fill(0)
black_img = Image.fromarray( black_img_array )


# looping through the black image and inserting the correct pixel values

for row in range(1, rows):
    for col in range (1, cols):
        c_d = np.array( [ [row], [col] ] )
        c_d = np.vstack( ( c_d, one ) )      
        v = np.dot( H_prime, c_d )
        
        if ( v[2][0] != 0 ):
            a_b = np.array( [ [ int( np.round( v[0][0]/v[2][0] ))], [ int( np.round( v[1][0]/v[2][0] )) ] ] )
            
             
            if ( 0 < a_b[0][0] and a_b[0][0] < rows and 0 < a_b[1][0] and a_b[1][0] < cols ):
                black_img_array[ row, col ] = distorted_im_arr[ int(a_b[0][0]), int(a_b[1][0]) ]
                
               

processed_img = Image.fromarray( black_img_array )
processed_img.save( sys.argv[2] )
processed_img.show()

#distorted_im.show()

#print(distorted_im_arr[0, 0:-1])
#print(np.dot(distorted_im_arr[0, 0:-1], H_prime))
#print(np.round(np.dot(distorted_im_arr[0, 0:-1], H_prime)).astype(int))

