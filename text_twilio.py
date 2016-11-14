from twilio.rest import TwilioRestClient


def text(content, phone_num):
    ACCOUNT_SID = "YOUR ACCOUNT SID" 
    AUTH_TOKEN = "YOUR AUTH TOKEN"
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
    to= phone_num, 
    from_="THE NUMBER YOU RECEIVE HERE", 
    body= content, 

    )


