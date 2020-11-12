# AR_VR
Creating a star map in modero_lab02_starmap.py

In creating a starmap:
  create an all black image
  load the star_data_lots.csv file which contains the locations of stars in space
  linearly scale the brightness intensities
  calculate the latitude from the declination angles
  claculate the longitude from the right ascension
  compute the PICS coordinates (row and column) from the latitude and longitude values
  at the PICS coordinate of the row, col pair, change the pixel intensity to the corresponding intensity
  
  
Padding a stereopair onto a black image in modero_lab02_stereopair.py
To pad the images on the black image:
  load the left and right images
  resize the left and right images
  create a black image on which the right and left will be padded
  determine the pixel positions on the black image where the upper left corners of the left and right iages will be mapped
  paste the two images onto the black image
  

