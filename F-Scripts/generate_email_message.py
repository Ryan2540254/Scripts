# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:25:59 2023

@author: ADMIN
"""

#!/usr/bin/env python3

import email.message
import mimetypes
import smtplib
import os.path

def generate(sender,recipient, subject, body, att_path):
    """"Creates an email with attachments."""
    #Basic email formatting
    message = email.message.EmailMessage()
    message["From"]    = sender
    message["To"]      = recipient
    message["Subject"] = subject
    message.set_content(body)
    
    #Process the Attachment & Add it to Email
    att_filename            = os.path.basename(att_path)
    mime_type, _            = mimetypes.guess_type(att_path)
    mime_type, mime_subtype = mime_type.split("/",1)
    
    with open(att_path, "rb") as ap:
        message.add_attachment(
            ap.read(),
            maintype = mime_type,
            subtype  = mime_subtype,
            filename = att_filename,
        )
    return message  

def send(message):
    """Sends the message to th configured SMTP Server."""
    mail_server = smtplib.SMTP("localhost")
    mail_server.send_message(message)
    mail_server.quit()
    
    