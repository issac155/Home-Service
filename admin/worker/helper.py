# from django.conf import settings
# from twilio.rest import Client


# class MessageHandler:
#     phone_number=None
#     otp=None
#     def __init__(self,phone_number,otp) -> None:
#         self.phone_number=phone_number
#         self.otp=otp
#     def send_otp_via_message(self):     
#         client= Client(settings.ACCOUNT_SID,settings.AUTH_TOKEN)
#         message=client.messages.create(body=f'your otp is:{self.otp}',from_=f'{settings.TWILIO_PHONE_NUMBER}',to=f'{settings.COUNTRY_CODE}{self.phone_number}')
#     def send_otp_via_whatsapp(self):     
#         client= Client(settings.ACCOUNT_SID,settings.AUTH_TOKEN)
#         message=client.messages.create(body=f'your otp is:{self.otp}',from_=f'{settings.TWILIO_WHATSAPP_NUMBER}',to=f'whatsapp:{settings.COUNTRY_CODE}{self.phone_number}')

import requests

class MessageHandler:
    phone_number = None
    otp = None

    def __init__(self, phone_number, otp):
        self.phone_number = phone_number
        self.otp = otp

    def send_otp_via_message(self):
        url = 'https://www.smsgatewayhub.com/api/mt/SendSMS'
        params = {
            'APIKey': '9CWOwaMG6UGfeO6qZI5apQ',
            'senderid': 'SEASEN',
            'channel': '2',
            'DCS': '0',
            'flashsms': '0',
            'number': self.phone_number,
            'text': f'Dear {self.otp}, Many more happy returns of the day. With regards Sea Sense Group',
            'route': '31',
            'EntityId': '1701159125640974053',
            'dlttemplateid': '1707161044624969443'
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            print('OTP message sent successfully.')
        else:
            print('Failed to send OTP message.')
