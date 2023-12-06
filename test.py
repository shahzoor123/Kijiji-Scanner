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



