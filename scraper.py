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



# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        
# Function to check for new ads
def checking():
    url_to_scrape_actual_data = 'https://www.kijiji.ca/b-cars-trucks/city-of-toronto/2000__2016/c174l1700273a68?kilometers=100000__300000&for-sale-by=ownr&radius=176.0&price=700__2500&address=434+Bay+St.%2C+Toronto%2C+ON+M5G+1P5%2C+Canada&ll=43.6534662%2C-79.38323009999999'

    # Scrape new ads
    new_ads = scrape_data(url_to_scrape_actual_data)

    # Update the seen ads file
    seen_ads_file = 'all_seen_ads.txt'
    if not os.path.exists(seen_ads_file):
        print(f"The file '{seen_ads_file}' does not exist. Creating in the script's directory.")
        with open(seen_ads_file, 'w') as file:
            file.write('\n'.join(new_ads))
    else:
        with open(seen_ads_file, 'r', encoding='utf-8') as file:
            seen_ads = set(file.read().splitlines())

        # Check for new ads
        new_ads_set = set(new_ads)
        unseen_ads = new_ads_set - seen_ads

        if unseen_ads:
            # Print and add new ads to the seen ads file
            print("New ads found:")
            for ad in unseen_ads:
                print(ad)
            with open(seen_ads_file, 'a', encoding='utf-8') as file:
                file.write('\n'.join(unseen_ads))
                file.write('\n')
                Send_SMS(url_to_scrape_actual_data, unseen_ads)


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


def scrape_data(url):
    # Make a request to the website
    response = requests.get(url)
    
    print(response.url)
    
    ad_list = []
    
    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

      
        ads = soup.find_all('a', class_='sc-388271ae-0 hLAAKW')
        
        
        for ad in ads:
            ad_list.append(ad.text)
            # print(ad.text)


    return ad_list



# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\




def Send_SMS(url, ad_data):
    
    print("i am sending sms")
    
    account_sid = "AC96d42f46854b5cf18cd371b2a556c7cb"
    account_token = "9b69946ab8fb2519af85ae9b97ba6e13"
    twillio_number = "+16184214328"
    receipiant_number = "+16477161092"

    client = Client(account_sid, account_token)

    message = client.messages.create(
        body = f'Hi Sameer We Found New Ads Post of your interest Here it is Title : {ad_data} Link : {url}',
        from_=twillio_number,
        to=receipiant_number
    )

    print('sended')
    
   


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
    
# Schedule the checking function to run every 5 minutes
schedule.every(1).minutes.do(checking)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(.3)