#!/usr/bin/env python3
import os
import smtplib
import mimetypes
from   email.message import EmailMessage

message         = EmailMessage()
sender          = 'me@example.com'
recipient       = 'you@example.com'
body            = 'Hi there, am learning to send emails.'

att             = input('Enter file name:')
att_path        = os.path.abspath(att)
att_name        = os.path.basename(att_path)
mime_type, _            = mimetypes.guess_type(att_path)
mime_type, mime_subtype = mime_type.split('/',1)
print(f'The mime type is:{mime_type}')
print(f'The mime sub-type is:{mime_subtype}')

# with open(att_path, 'rb') as ap:
#       message.add_attachment(ap.read(),
#                             maintype = mime_type,
#                             subtype  = mime_subtype,
#                             filename = att_name)

message['From'] = sender
message['To']   = recipient
message['Subject'] = f'Greetings from {sender} to {recipient}.'
message.set_content(body)

print(message)

