# import necessary libraries
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# opening image and obtaining the image array
img = Image.open("Rwanda_SRTM30meters.tif")
img_arr = np.asarray(img, np.uint16)

# finding the max and min values
initial_max = np.amax(img_arr)
initial_min = np.amin(img_arr)

'''
# debug print
print("initial max: ",initial_max)
print("initial min:", initial_min)
'''

# coverting all max values to 0
img_arr = np.where(img_arr < initial_max, img_arr, 0)

# finding max and min after culling
max_val = np.amax(img_arr)
min_val = np.amin(img_arr)

'''
# debug print
print("final max: ",max_val)
print("final min: ",min_val)
'''

rows = img_arr.shape[0]
cols = img_arr.shape[1]

monochr_arr = np.zeros( (rows, cols), np.float )

# linear scaling: 0 -> 0; max -> 255
for i in range ( rows ):
    for j in range ( cols ):
        monochr_arr[i][j] = (255/max_val)* img_arr[i][j]

# outputing monochrome image
img_monochrome = monochr_arr.astype( np.uint8 )
a = Image.fromarray( img_monochrome )
a.save( "img_monochrome.jpeg" )
a.show()

# open object file for writing
obj = open("modero_lab03_1.obj","w")
obj.write("mtllib modero_lab03.mtl \n")
obj.write(" \n")

# subsampling

# creating an array of all zeros and size row/10, col/10
sub_rows = int(rows/10)
sub_cols = int( cols/10 )
subsample = np.zeros( [sub_rows, sub_cols, 3], np.float )

start_row = 0
stop_row = 9
for i in range ( sub_rows-1 ):
    start_col = 0
    stop_col = 9
    for j in range ( sub_cols-1 ):
        elevation = np.amax ( img_arr [start_row:stop_row, start_col:stop_col] )
        if ( elevation < initial_min ):
            subsample[i,j] = (0, 128, 0)
            obj.write("usemtl green \n")
        elif ( elevation >= initial_min and elevation < max_val/2 ):
            subsample[i,j] = (128, 0, 0)
            obj.write("usemtl red \n")
        else:
            subsample[i,j] = (0, 0, 128)
            obj.write("usemtl blue \n")
        
        obj.write(f"v {-i} {j} {elevation/300} \n")
        obj.write(f"v {-i} {(j+1)} {elevation/300} \n")
        obj.write(f"v {-(i+1)} {j} {elevation/300} \n")
        obj.write(f"f {-3} {-2} {-1} \n")
        obj.write(" \n")
        
        k = j + 1 
        obj.write(f"v {-i} {k} {elevation/300} \n")
        obj.write(f"v {-(i+1)} {k} {elevation/300} \n")
        obj.write(f"v {-(i+1)} {k-1} {elevation/300} \n")
        obj.write(f"f {-3} {-2} {-1} \n")
        obj.write(" \n")
        
        start_col = start_col + 10
        stop_col = stop_col + 10
        
    start_row = start_row + 10
    stop_row = stop_row + 10


# opening the material file for writing and writing to it        
mtl = open("modero_lab03.mtl", "w")
mtl.write("newmtl red \n")
mtl.write( f"Ka {1.000000} {0.000000} {0.000000} \n" )
mtl.write( f"Kd {1.000000} {0.000000} {0.000000} \n" )
mtl.write( f"Ks {0.000000} {0.000000} {0.000000} \n" )
mtl.write( f"Ns {10.0} \n" )
mtl.write( f"d {1.0} \n" )
mtl.write(" \n")

mtl.write("newmtl green \n")
mtl.write( f"Ka {0.000000} {1.000000} {0.000000} \n" )
mtl.write( f"Kd {0.000000} {1.000000} {0.000000} \n" )
mtl.write( f"Ks {0.000000} {0.000000} {0.000000} \n" )
mtl.write( f"Ns {10.0} \n" )
mtl.write( f"d {1.0} \n" )
mtl.write(" \n")

mtl.write("newmtl blue \n")
mtl.write( f"Ka {0.000000} {0.000000} {1.000000} \n" )
mtl.write( f"Kd {0.000000} {0.000000} {1.000000} \n" )
mtl.write( f"Ks {0.000000} {0.000000} {0.000000} \n" )
mtl.write( f"Ns {10.0} \n" )
mtl.write( f"d {1.0} \n" )
mtl.write(" \n")