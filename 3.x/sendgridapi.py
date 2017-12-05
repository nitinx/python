# 05 Dec 2017 | SendGrid API

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *

API_KEY = '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'

print(os.environ.get('SENDGRID_API_KEY'))

#sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
#sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('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'))
sg = sendgrid.SendGridAPIClient(apikey='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')
from_email = Email("from@gmail.com")
to_email = Email("pai.nitin@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
