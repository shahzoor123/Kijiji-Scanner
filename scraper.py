import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import schedule
import time
import os
from twilio.rest import Client



# Set the current working directory to the script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

def scrape_data(url):
    # Make a request to the website
    response = requests.get(url)
    
    print(response.url)
    
    ad_list = []
    
    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        ads = soup.find_all('a', class_='sc-2e07e5ea-0 gpxjNR')
        
        img = soup.find_all('img', class_='sc-92b4b92a-0 kFFtpF sc-388271ae-2 fugJbm')
        
        for ad in ads:
            ad_list.append(ad.text)
            print(ad.text)
            
        for i in img:
            print(i)    
            
        print("f1")    

    return ad_list





def send_whatsapp_msg(ad_data, url):
    
    account_sid = "AC96d42f46854b5cf18cd371b2a556c7cb"
    account_auth = "a90f655fbb8cffcdb381f084a4d90fac"
    twillio_number = "+14155238886"
    receipiant_number = "+923138409209"
    
    client = Client(account_sid, account_auth)
    
    message = client.messages.create(
        body = 'Hello',
        from_=twillio_number,
        to=receipiant_number
    )
    
    print('sended')
    

    # Set up your email configuration
    sender_number = '03362131109'
    receiver_number = '03138409209'
    subject = 'Ad Listing'

    # Compose the number content
    body = f"Title:There is a ad listed today title is: {ad_data}  please check on the following link {url}"
    
    print(body)
    
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_number
    message['To'] = receiver_number

    # Connect to the SMTP server and send the number
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_number, 'meml pxij bged qaee')
    server.sendmail(sender_number, receiver_number, message.as_string())
    print('Whatsapp msg is sended')
        


        
def checking():
    url_to_scrape_actual_data = 'https://www.kijiji.ca/b-cars-trucks/city-of-toronto/2000__2016/c174l1700273a68?kilometers=100000__300000&for-sale-by=ownr&radius=176.0&price=700__2500&address=434+Bay+St.%2C+Toronto%2C+ON+M5G+1P5%2C+Canada&ll=43.6534662%2C-79.38323009999999'
    
    # Check for new ads
    new_ads = scrape_data(url_to_scrape_actual_data)

    # Update the seen ads file
    seen_ads_file = 'all_seen_ads.txt'
    if not os.path.exists(seen_ads_file):
        print(f"The file '{seen_ads_file}' does not exist. Creating in the script's directory.")
        with open(seen_ads_file, 'w') as file:
            file.write('\n'.join(new_ads))
    else:
        with open(seen_ads_file, 'r') as file:
            seen_ads = set(file.read().splitlines())

        # Check for new ads
        new_ads_set = set(new_ads)
        unseen_ads = new_ads_set - seen_ads

        if unseen_ads:
            # Send email notification
            
            
            # send_email(list(unseen_ads), url_to_scrape_actual_data)

            # Update the seen ads file
            with open(seen_ads_file, 'a') as file:
                file.write('\n'.join(new_ads_set))





# Schedule the checking function to run every 5 minutes
schedule.every(.1).minutes.do(checking)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)