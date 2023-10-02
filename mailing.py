# Getting nessesary libraries
import passwords
import smtplib 
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Implementing the class to mail the certificate

class Mailing:
    def __init__(self , sender_email , reciever_email , mailSubject , bodyText , sending_image_name):
        sender_address = sender_email;
        reciever_address = reciever_email;
        subject = mailSubject;
        text = bodyText;
        image_name = sending_image_name;

        # Entering the passcode for safety
        password = passwords.Passwords.returningPassword();

        # Putting server Details
        smtp_server = "smtp.gmail.com" 
        port = 587

        # Setting up the message
        message = MIMEMultipart();
        message['Subject'] = subject;
        message['From'] = sender_address;
        message['To'] = reciever_address;  

        # # Giving the body to the email
        body_text = MIMEText(text, 'plain')  
        message.attach(body_text)

        # Adding the image as an attachment in the mail
        '''
            Note: If you change the directory where all the certificates are storing...
            Please change the file directory below
        '''

        with open('All Certificates/' + image_name, 'rb') as fp:
            img = MIMEImage(fp.read())
            # Addint the file as attachment
            img.add_header('Content-Disposition', 'inline', filename=image_name)
            message.attach(img)
        
        # Connecting to the server for mailing 
        context = ssl.create_default_context()

        try:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()  # check connection
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # check connection
            server.login(sender_address, password)

            # Send email here
            server.sendmail(sender_address, reciever_address, message.as_string())

        except Exception as e:
            print(e)
        finally:
            server.quit()


# >>>> Testing

# sub = "Certificate for Ishaan Joshi";
# text = "Hello World. I hope you are doing well. Here's a certificate which you might like"
# emailSample = Mailing("noreply.iosd@gmail.com" , "joshi.ishaan.2001@gmail.com" , sub , text , "Ishaan Joshi.jpeg")

