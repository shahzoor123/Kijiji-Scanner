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
    url_to_scrape_actual_data = 'https://www.kijiji.ca/b-cars-trucks/city-of-toronto/acura__honda__lexus__nissan__toyota__mazda-2000__2016/c174l1700273a54a68?kilometers=100000__300000&for-sale-by=ownr&radius=176.0&price=700__2500&address=434+Bay+St.%2C+Toronto%2C+ON+M5G+1P5%2C+Canada&ll=43.653466%2C-79.38323'

    # Scrape new ads
    new_ads = scrape_data(url_to_scrape_actual_data)

    # Update the seen ads file
    seen_ads_file = 'all_seen_ads.txt'
    if not os.path.exists(seen_ads_file):
        print(f"The file '{seen_ads_file}' does not exist. Creating in the script's directory.")
        with open(seen_ads_file, 'w', encoding='utf-8') as file:
            for ad in new_ads:
                file.write(f"{ad['title']} - {ad['link']}\n")
    else:
        with open(seen_ads_file, 'r', encoding='utf-8') as file:
            seen_ads = set(line.strip() for line in file)

        # Check for new ads
        unseen_ads = [ad for ad in new_ads if f"{ad['title']} - {ad['link']}" not in seen_ads]

        if unseen_ads:
            # Print and add new ads to the seen ads file
            print("New ads found:")
            for ad in unseen_ads:
                print(f"Ad Title: {ad['title']}")
                print(f"Ad Link: {ad['link']}")

            # Write new ads to the seen ads file
            with open(seen_ads_file, 'a', encoding='utf-8') as file:
                for ad in unseen_ads:
                    file.write(f"{ad['title']} - {ad['link']}\n")

            # Send SMS with new ad titles and links
            for ad in unseen_ads:
                Send_SMS(ad['link'], ad['title'])


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
            # Extract title and href from the ad
            ad_title = ad.get_text(strip=True)
            ad_link = ad.get('href')

            # # Print ad information
            # print(f"Ad Title: {ad_title}")
            # print(f"Ad Link: {ad_link}")
            
              # Create a dictionary for each ad
            ad_dict = {'title': ad_title, 'link': ad_link}
            
            # Append the dictionary to the list
            ad_list.append(ad_dict)
        
        # for ad_dict in ad_list:
        #     print(ad_dict)



    return ad_list



# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\




def Send_SMS(url, ad_data):
    
    print("i am sending sms" , url)
    
    account_sid = "AC96d42f46854b5cf18cd371b2a556c7cb"
    account_token = "7c21d0985a5e2831da3200bf21f38153"
    twillio_number = "+16184214328"
    receipiant_number = "+16477161092"

    client = Client(account_sid, account_token)

    # message = client.messages.create(
    #     body = f'Hi Sameer we found new Ads post of your interest Here it is : \n \n {ad_data} \n \n Link : https://www.kijiji.ca{url}',
    #     from_=twillio_number,
    #     to=receipiant_number
    # )

    print('sended')
    
   


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
    
# Schedule the checking function to run every 5 minutes
schedule.every(.01).minutes.do(checking)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)