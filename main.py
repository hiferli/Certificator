import algorithm
import mailing
import cv2
import pandas as pd

# Essentially Required Variables:
sender_address = "noreply.iosd@gmail.com"
# contact_mail = "iosdbpit@gmail.com"
contact_mail = "joshi.ishaan.2001@gmail.com"
format_of_certificate = "png"

# Certificate Properties
font_style = cv2.FONT_HERSHEY_TRIPLEX
font_color_in_BRG = (0 , 0 , 0)
font_thickness = 6
font_size = 4;

# Variation Variables
# Email Variables

# Insert the name of the prototye with the file extension
image = cv2.imread("Certi Proto.png");

information = pd.read_csv("Names&Emails.csv");

for index , participant in information.iterrows():
    name_on_certificate = str.title(participant["Name"]);
    receiver_address = participant["Email"];

    subject = "[Auto-Generated] Greetings"
    body_text = f'''
    Hello {name_on_certificate},
    
    I hope the mail reaches you good and fine. 
    This is the sample working of the script.

    Please contact {contact_mail} for any issue regarding this certificate.

    Regards,
    Ishaan Joshi   
    '''
    # print(body_text)
    sample = algorithm.PrintNames(image , name_on_certificate , font_style , font_size , font_color_in_BRG , font_thickness , format_of_certificate);
    emailSample = mailing.Mailing(sender_address , receiver_address , subject , body_text , name_on_certificate + "." + format_of_certificate)
    image = cv2.imread("Certi Proto.png");    

print("Congratulations: All Mailing is done")