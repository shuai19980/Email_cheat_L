#!/usr/bin/python
# -*- coding: UTF-8 -*-
from email.mime.application import MIMEApplication
from core.getfile import getfile


class enclosure:
    def addenclosure(enclosurepath,message):

        for filepath in enclosurepath:
            # 获取文件名称
            filename = filepath.split('/')[-1]
            #判断是否为url
            if filepath[0:4] == 'http':
                urlfile = getfile.getfile(filepath, filename)
                filepath = urlfile[0]
                filename = urlfile[1]

                # 调用currencyfile方法
                message.attach(enclosure.currencyfile(filepath,filename))
            else:
                #获取后缀
                #suffix = name.split('.')[-1]

                #调用currencyfile方法
                message.attach(enclosure.currencyfile(filepath,filename))

                #如果是图片类型,执行imagefile方法
                #if suffix == "jpg" or suffix == "png" or suffix == "gif":
                    #添加附件（word文档）
                    #message.attach(enclosure.imagefile(i,name))
                #其他文件,执行currencyfile方法
                #else:
                    #message.attach(enclosure.currencyfile(i,name))
        return message

    #通用文件类型
    def currencyfile(currencyfile,filename):
        word = MIMEApplication(open(currencyfile, 'rb').read())
        word.add_header('Content-Disposition', 'attachment', filename=filename) #设置附件信息
        return word

    #图片类型
    #def imagefile(imagefile,filename):
        #image = MIMEImage(open(imagefile, 'rb').read(), _subtype='octet-stream')
        #image.add_header('Content-Disposition', 'attachment', filename="1.png")
        #return image
