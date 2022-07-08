import algorithm
import mailing
import cv2
import numpy as np
import pandas as pd

# Essentially Required Variables:
sender_address = "noreply.iosd@gmail.com"
format_of_certificate = "jpeg"

# Certificate Properties
font_style = cv2.FONT_HERSHEY_DUPLEX
font_color_in_BRG = (236, 235, 250)
font_thickness = 2
font_size = 4;

# Variation Variables
# Email Variables

# Insert the name of the prototye with the file extension
image = cv2.imread("Prototype.png");

information = pd.read_csv("Names&Emails.csv");

for index , participant in information.iterrows():
    name_on_certificate = participant["Name"];
    receiver_address = participant["Email"];

    subject = "IOSD BPIT : Testing #2 : Certificate for " + name_on_certificate;
    body_text = f'''
    Hello {name_on_certificate}
    
    Testing #2
    
    Hope you are doing well.
    This is the certificate.
    
    '''
    # print(body_text)
    sample = algorithm.PrintNames(image , name_on_certificate , font_style , font_size , font_color_in_BRG , font_thickness , format_of_certificate);
    emailSample = mailing.Mailing(sender_address , receiver_address , subject , body_text , name_on_certificate + "." + format_of_certificate)
    image = cv2.imread("Prototype.png");    

print("Congratulations: All Mailing is done")