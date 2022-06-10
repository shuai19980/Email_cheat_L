#!/usr/bin/python
# -*- coding: UTF-8 -*-

from core.sendmail import sendmail

#填写相关信息

#邮件服务器，例如:smtp.163.com
mail_host="邮件服务器"

#邮件账号
mail_user="邮件账号"

#邮件密码
mail_pass="邮件密码"

#伪造的邮箱名称即邮箱的Header,例如:管理员<admin@alibaba.com>
mailheader = "伪造的邮箱名称即邮箱的Header"

#邮件标题,例如:重要通知
subject = "邮件标题"

#邮件内容修改file目录下的邮件.html文件

#不需要附件时,请不要删除改字段,保持为空即可,enclosurepath为属组,如果只有一个文件请保持字段为数组状态
#支持本地路径和url
#支持本地路径和url并存
#举例：
#linux：/root/桌面/测试.txt
#windows: C:/Users/administrator/Desktop/测试.txt
#url为文件的下载url
enclosurepath = ['./file/测试.doc','http://www.tup.tsinghua.edu.cn/upload/books/yz/044819-01.pdf']

#调用sendmail发送邮件
sendmail.sendmail(mail_host,mail_user,mail_pass,mailheader,subject,enclosurepath)
