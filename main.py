#!/usr/bin/python
# -*- coding: UTF-8 -*-

from core.sendmail import sendmail

#填写相关信息

#邮件服务器，例如:smtp.163.com
mail_host="邮件服务器"

#邮件账号
mail_user="邮箱账号"

#邮件密码
mail_pass="邮箱授权码"

#伪造的邮箱名称即邮箱的Header,例如:管理员<huabei@alibaba.com>
mailheader = "邮箱header"

#邮件标题,例如:重要通知
subject = "邮件标题"

#邮件内容修改file目录下的邮件.html文件

#调用sendmail发送邮件
sendmail.sendmail(mail_host,mail_user,mail_pass,mailheader,subject)