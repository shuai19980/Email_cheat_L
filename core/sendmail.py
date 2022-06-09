#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from core.enclosure import enclosure
from core.mailhtml import mailhtmltxt

# 创建复合邮件对象
message = MIMEMultipart()

class sendmail:
    def sendmail(mail_host,mail_user,mail_pass,header,subject,enclosurepath):
        mail_host=mail_host
        mail_user=mail_user
        mail_pass=mail_pass
        number = 1
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

            #判断是否为第一次发送，如果是则添加message内容，如果不是则不添加
            if number == 1:

                #发送的html
                mailhtmltxt.addmailhtml(mailhtml,message)


                #如果附件不为空则,进行附件发送操作
                if len(enclosurepath) != 0:
                    #发送附件
                    enclosure.addenclosure(enclosurepath,message)

                    #需要伪造的邮箱
                    message['From'] = Header(header, 'utf-8')
                    message['To'] =  Header(receivers[0], 'utf-8')

                    subject = subject
                    message['Subject'] = Header(subject, 'utf-8')
                    number += 1


            try:
                smtpObj = smtplib.SMTP()
                smtpObj.connect(mail_host, 25)
                smtpObj.login(mail_user,mail_pass)
                smtpObj.sendmail(sender, receivers, message.as_string())
                smtpObj.close()
                print ("Success")
                Success +=1
            except smtplib.SMTPException:
                #print ("Error")
                print("发送成功")
                err += 1
        f.close()
        html.close()
        #邮件总数
        all = Success+err
        print("共发送"+str(all)+"封邮件，成功发送"+str(Success)+"封邮件，有"+str(err)+"封邮件产生错误。")
