#Importing the necessary libraries
import sys
import PIL
import numpy as np
import pandas as pd
from PIL import Image
from scipy import signal

# provide one argument: the name of the star_image.jpg
if ( len( sys.argv ) != 2 ):
    print( "usage is: %s star_image_out " % (sys.argv[0]) )
    print( "        image_out is the processed image" )
    sys.exit()
    
# loading the star csv
stars           = pd.read_csv( "star_data_lots.csv" )
stars           = stars.iloc[1:, :] # remove the sun from the list of stars

# linear function values for y = mx + c for scaling intensities
# y is the scaled intensity, x is the mag column
m_int           = -36.49
c_int           = 202.45
intensities     = [] # initialize the scaled intensities
longitudes      = []
latitudes       = []
for i in range ( len(stars) ): 
    # converting intensity values greater than 5 to 5
    if ( stars["mag"].iloc[i] > 5 ):
       stars["mag"].iloc[i] = 5 
    
    # linearly scaling the intensities
    x   = stars["mag"].iloc[i]
    y   = m_int*x + c_int
    intensities.append(int(round(y)))
    
    # converting ra column to longitude
    lng = 360 - ( stars["ra"].iloc[i] * 15 )
    longitudes.append( lng )
    
    # converting dec column to latitudes
    lat = -1 * stars["dec"].iloc[i]
    latitudes.append( lat )

stars[ "intensities" ] = intensities
stars[ "longitudes" ]  = longitudes
stars[ "latitudes" ]   = latitudes

# creating the black  image for star map
rows            = 2048
cols            = 4096
black_img_array = np.zeros( [ rows, cols, 3 ], dtype=np.uint8 )
black_img_array.fill(0)
black_img = Image.fromarray( black_img_array )
pixels = black_img.load()

# inserting the stars into the black image
for i in range( len(stars) ):
    col = stars["longitudes"].iloc[i] * ( 4096/360 )
    row = stars["latitudes"].iloc[i] * ( 2048/180 ) + 1024
    
    int_ = stars["intensities"].iloc[i]
    pixels[col, row] = ( int_, int_, int_ )

black_img_array = np.asarray( black_img, np.float32 )

# convolution to spread out the intensities into neighboring pixels
convK = np.asarray( [(0.0, 0.5, 0.0), (0.5, 1.0, 0.5), (0.0, 0.5, 0.0)], np.float )
    
for i in range(len(black_img_array)):
    black_img_array[i] =  signal.convolve2d(black_img_array[i], convK, 'same', 'fill', fillvalue=0)

black_img_array = black_img_array.astype( np.uint8 )
black_img       = Image.fromarray( black_img_array )

black_img.save(sys.argv[1] )
black_img.show()