from twilio.rest import Client  


account_sid = "AC96d42f46854b5cf18cd371b2a556c7cb"
account_auth = "a90f655fbb8cffcdb381f084a4d90fac"
twillio_number = "+16184214328"
receipiant_number = "+16478820415"

client = Client(account_sid, account_auth)

message = client.messages.create(
    body = 'Hello Sameer this is me shahzoor sending you the msg for testing',
    from_=twillio_number,
    to=receipiant_number
)

print('sended')




# import requests

# """
#  * Send WhatsApp template message directly by calling HTTP endpoint.
#  *
#  * THIS CODE EXAMPLE IS READY BY DEFAULT. HIT RUN TO SEND THE MESSAGE!
#  *
#  * Send WhatsApp API reference: https://www.infobip.com/docs/api#channels/whatsapp/send-whatsapp-template-message
#  *
#  * See Readme file for details.
# """

# BASE_URL = "https://e1dnv2.api.infobip.com"
# API_KEY = "App 817d4fca5c9b842ecd3a84853d30389c-41014eca-2dd2-4ecd-b677-4a2653fc02b9"

# SENDER = "447860099299"
# RECIPIENT = "+923138409209"

# payload = {
#     "messages":
#         [
#             {
#                 "from": SENDER,
#                 "to": RECIPIENT,
#                 "content": {
#                     "templateName": "registration_success",
#                     "templateData": {
#                       "body": {
#                         "placeholders": [
#                           "sender",
#                           "message",
#                           "delivered",
#                           "testing"
#                         ]
#                       },
#                       "header": {
#                         "type": "IMAGE",
#                         "mediaUrl": "https://api.infobip.com/ott/1/media/infobipLogo"
#                       },
#                       "buttons": [
#                         {
#                           "type": "QUICK_REPLY",
#                           "parameter": "yes-payload"
#                         },
#                         {
#                           "type": "QUICK_REPLY",
#                           "parameter": "no-payload"
#                         },
#                         {
#                           "type": "QUICK_REPLY",
#                           "parameter": "later-payload"
#                         }
#                       ]
#                   },
#                   "language": "en"
#                }
#            }
#         ]
#     }

# headers = {
#     'Authorization': API_KEY,
#     'Content-Type': 'application/json',
#     'Accept': 'application/json'
# }

# response = requests.post(BASE_URL + "/whatsapp/1/message/template", json=payload, headers=headers)

# print(response.json())
# print("Sended")