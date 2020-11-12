# AR_VR
Creating a star map in modero_lab02_starmap.py

In creating a starmap: <br/>
<ul>
  <li>create an all black image </li><br/>
  <li>load the star_data_lots.csv file which contains the locations of stars in space</li> <br/>
  <li>linearly scale the brightness intensities</li> <br/>
  <li>calculate the latitude from the declination angles</li> <br/>
  <li>claculate the longitude from the right ascension </li><br/>
  <li>compute the PICS coordinates (row and column) from the latitude and longitude values </li><br/>
  <li>at the PICS coordinate of the row, col pair, change the pixel intensity to the corresponding intensity</li> <br/>
</ul>
  <br/>
  
Padding a stereopair onto a black image in modero_lab02_stereopair.py <br/>

To pad the images on the black image: <br/>
<ul>
  <li>load the left and right images </li><br/>
  <li>resize the left and right images </li><br/>
  <li>create a black image on which the right and left will be padded </li><br/>
  <li>determine the pixel positions on the black image where the upper left corners of the left and right iages will be mapped </li><br/>
  <li>paste the two images onto the black image </li><br/>
</ul>  

