#!/usr/bin/python3.5 -tt
# -*- coding: utf-8 -*-
import sqlite3
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config


def sendmail(target):
    me = config.email_login
    msg = MIMEMultipart('alternative')
    msg['Subject'] = config.email_subject
    msg['From'] = me
    msg['To'] = target

    # Create the body of the message (a plain-text and an HTML version).
    text = config.email_excerpt
    f = open(config.email_file, 'r', encoding="utf-8").read()
    html = f


    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(me, config.email_pass)
    mail.sendmail(me, target, msg.as_string())
    mail.quit()
