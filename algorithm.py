# Getting nessesary libraries
import cv2

# Getting the certificate as an Image
image = cv2.imread("Prototype.png");

#### Describing Parameters
# Text to be printed on the certificate
text = "Sample Name"

# Font
font = cv2.FONT_HERSHEY_DUPLEX

# Font Scale
fontScale = 5

# Color in RGB
'''
Note:
Color format in OpenCV is BRG and not RGB
When you add a custom color... Please take care of this thing
'''
color = (236, 235, 250)
  
# Thichness of the Text
thickness = 3
   
# Getting the text size
textsize = cv2.getTextSize(text.capitalize()  , font, fontScale, thickness)[0]

# Setting the coordinates 
'''
Note:
The textsize function returns a tuple as follows:
(width_of_the_text , height_of_the_text , baseline)

The image.shape returns the tuple as follows:
(height_of_the_image , width_of_the_image , channels)

So, the variables below is the difference in the width and height of both image and text
The round function is mandatory since pixels cant' be floating numbers
'''

textX = round((image.shape[1] - textsize[0]) / 2)
textY = round((image.shape[0] + textsize[1]) / 2)

# Finally putting the text on the center of the image.
image = cv2.putText(image, text.capitalize() , (textX , textY), font, fontScale, color, thickness, cv2.LINE_AA)

# Saving this as a new image
cv2.imwrite("Testing.jpg", image)

# Printing the image
# cv2.imshow("Names" , image);

cv2.waitKey(0);