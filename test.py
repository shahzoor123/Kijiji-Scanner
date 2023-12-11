import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import schedule
import time
import os
from twilio.rest import Client

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

            # Print ad information
            print(f"Ad Title: {ad_title}")
            print(f"Ad Link: {ad_link}")
            
              # Create a dictionary for each ad
            ad_dict = {'title': ad_title, 'link': ad_link}
            
            # Append the dictionary to the list
            ad_list.append(ad_dict)
        
        for ad_dict in ad_list:
            print(ad_dict)



    return ad_list


url_to_scrape_actual_data = 'https://www.kijiji.ca/b-cars-trucks/city-of-toronto/acura__honda__lexus__nissan__toyota__mazda-2000__2016/c174l1700273a54a68?kilometers=100000__300000&for-sale-by=ownr&radius=176.0&price=700__2500&address=434+Bay+St.%2C+Toronto%2C+ON+M5G+1P5%2C+Canada&ll=43.653466%2C-79.38323'

scrape_data(url_to_scrape_actual_data)