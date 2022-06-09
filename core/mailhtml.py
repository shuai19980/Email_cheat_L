#!/usr/bin/python
# -*- coding: UTF-8 -*-
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


class mailhtmltxt:
    def addmailhtml(mailhtml,message):

        #发送的内容（txt）
        #message = MIMEText('内容', 'plain', 'utf-8')
        #发送的html
        mailhtml= MIMEText(mailhtml, 'html', 'utf-8')
        # 添加正文到复合邮件对象中
        message.attach(mailhtml)
        return message