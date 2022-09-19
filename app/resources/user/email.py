from flask_restful import Resource
from mailjet_rest import Client
import os

api_key = os.environ.get('MAILJET_API_KEY')
api_secret = os.environ.get('MAILJET_API_SECRET')
mailjet = Client(auth=(api_key, api_secret), version='v3.1')


class Email(Resource):
    def get(self):
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": "info@physai.com",
                        "Name": "Dzmitry"
                    },
                    "To": [
                        {
                            "Email": "dzmitry.ashkinadze@gmail.com",
                            "Name": "Dzmitry"
                        }
                    ],
                    "Subject": "Greetings from Mailjet.",
                    "TextPart": "My first Mailjet email",
                    "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
                    "CustomID": "AppGettingStartedTest"
                }
            ]
        }
        result = mailjet.send.create(data=data)
        print(result.status_code)
        print(result.json())
