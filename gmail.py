# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 12:51:43 2020

@author: wcobern
"""

import smtplib


def send_email(to, subject, message):
    """ Send email from designated gmail account.
    # Inputs:
        to = list of email addresses
        subject = subject of email
        body = message

    
    Note by default gmail doesn't allow connections from "Less Secure Apps"
    This setting can be changed https://support.google.com/accounts/answer/6010255
    But I wouldn't recommend doing it on you main account!
    """
    
    gmail_user = 'xxxxx@gmail.com'
    gmail_password = 'yyyyy'
    
 
    # format the email text
    email_text = ''
    email_text += f'From: {gmail_user} \n'
    email_text += f'To: {", ".join(to)} \n'
    email_text += f'Subject: {subject}\n'
    email_text += f'{message}\n'


    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to, email_text)
        server.close()

    except:
       raise
       
def main():
    # Send a test email
    send_email(['me@my_email.com'],'test','Body')
    
if __name__ == '__main__':
    main()