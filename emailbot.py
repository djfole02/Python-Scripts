# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 20:20:18 2020

@author: Danny
"""

###################
#CHANGE THIS EMAIL
receiver = ''
###################

###################
###################
import smtplib, ssl

def msg(msg_num):
    port = 465
    password = ''
    
    SUBJECT1 = "VPN RESET"
    TEXT1 = "You need to change the vpn"
    msg1 = 'Subject: {}\n\n{}'.format(SUBJECT1, TEXT1)
    
    SUBJECT2 = "Added to Cart"
    TEXT2 = "You added an item to cart"
    msg2 = 'Subject: {}\n\n{}'.format(SUBJECT2, TEXT2)

    SUBJECT3 = "Checked Out"
    TEXT3 = "You have completed checkout"
    msg3 = 'Subject: {}\n\n{}'.format(SUBJECT3, TEXT3)
    
    SUBJECT4 = "Something Broke"
    TEXT4 = "Something has gone wrong with the bot"
    msg4 = 'Subject: {}\n\n{}'.format(SUBJECT4, TEXT4)
    
    context = ssl.create_default_context()
    sender = 'pyth0n4b0t@gmail.com'

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        if msg_num == 1:
            server.sendmail(sender,receiver,msg1)
        elif msg_num == 2:
            server.sendmail(sender,receiver,msg2)
        elif msg_num == 3:
            server.sendmail(sender,receiver,msg3)
        else: 
            server.sendmail(sender,receiver,msg4)
            