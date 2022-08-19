# Getting nessesary libraries
import cv2

# Implementing the class to print the name on the certificate

class PrintNames:
    
    def __init__(self , image , text , font , fontScale , color_BRG , thickness , format):
        
        textsize = cv2.getTextSize(str.title(text)  , font, fontScale, thickness)[0];
        # print(textsize);
        textX = round((image.shape[1] - textsize[0]) / 2)
        textY = round((image.shape[0] + textsize[1]) / 2)
        
        image = cv2.putText(image, str.title(text) , (textX , textY), font, fontScale, color_BRG, thickness)

        '''
            Note: If you have to change the directory where all the certificates are being stored...
            Renama the directory mentioned below
        '''

        path = "All Certificates/" + str.title(text) + "." + format;
        cv2.imwrite(path , image)
        cv2.waitKey(0);

'''
    Note #1:
        Color format in OpenCV is BRG and not RGB
        When you add a custom color... Please take care of this thing
'''

'''
    Note #2:
        The textsize function returns a tuple as follows:
        (width_of_the_text , height_of_the_text , baseline)

        The image.shape returns the tuple as follows:
        (height_of_the_image , width_of_the_image , channels)

        So, the variables below is the difference in the width and height of both image and text
        The round function is mandatory since pixels cant' be floating numbers
'''

'''
    Note #3:
        Add the file extension at the end of the filename
        So that the file is saved in the image format.
'''

# >>>>>>>>> Testing the Class

# image = cv2.imread("Certi Proto.png");
# Sample = PrintNames(image , "Ishaan Joshi" , cv2.FONT_HERSHEY_DUPLEX , 4 , (236, 235, 250) , 2 , "png");
