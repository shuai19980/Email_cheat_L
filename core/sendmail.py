#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email import message
from email.mime import text
from email.mime.text import MIMEText
from email.header import Header


class sendmail:
    def sendmail(mail_host,mail_user,mail_pass,header,subject):
        mail_host=mail_host
        mail_user=mail_user
        mail_pass=mail_pass
        err = 0
        Success = 0
        #打开邮箱.txt
        f=open("./file/邮箱账号.txt", "rt", encoding ='utf-8', errors='ignore')

        #打开发送的邮件内容.html
        html=open("./file/邮件内容.html", "rt", encoding ='utf-8', errors='ignore')
        mailhtml = html.read()

        for i in f:

            #每个换行符为一个
            c=i.split('\n\n')[0]

            sender = mail_user
            receivers = [c]

            #发送的内容（txt）
            #message = MIMEText('内容', 'plain', 'utf-8')

            #发送的html
            message = MIMEText(mailhtml, 'html', 'utf-8')



            #需要伪造的邮箱
            message['From'] = Header(header, 'utf-8')
            message['To'] =  Header(receivers[0], 'utf-8')

            subject = subject
            message['Subject'] = Header(subject, 'utf-8')


            try:
                smtpObj = smtplib.SMTP()
                smtpObj.connect(mail_host, 25)
                smtpObj.login(mail_user,mail_pass)
                smtpObj.sendmail(sender, receivers, message.as_string())
                print ("Success")
                Success +=1
            except smtplib.SMTPException:
                print ("Error")
                err += 1
        f.close()
        html.close()
        #邮件总数
        all = Success+err
        print("共发送"+str(all)+"封邮件，成功发送"+str(Success)+"封邮件，有"+str(err)+"封邮件产生错误。")