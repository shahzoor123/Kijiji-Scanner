import smtplib
from email.mime.text import MIMEText


def send_email(ad_data, url):
    

    # Set up your email configuration
    sender_email = 'temporary98778@gmail.com'
    receiver_email = 'juiceofprogramming@gmail.com'
    subject = 'Ad Listing'

    # Compose the email content
    body = f"Title:There is a ad listed today title is: {ad_data}  please check on the following link {url}"
    
    print(body)
    
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email

    # Connect to the SMTP server and send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, 'meml pxij bged qaee')
    server.sendmail(sender_email, receiver_email, message.as_string())
    print('Email is sended')
        
        
        
import pywhatkit


pywhatkit.sendwhatmsg("+923138409209" , "Hi", 9, 53 )        
