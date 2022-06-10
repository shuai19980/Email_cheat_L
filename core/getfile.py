#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from core.linux_or_windows import linux_or_windows

class getfile:
    def getfile(httpurl,filename):
        if linux_or_windows.linux_or_windows(None) == "windows":
            filepath = 'C:/Windows/Temp/'+filename

        elif linux_or_windows.linux_or_windows(None) == "linux":
            filepath = '/tmp' + filename
        """
                    下载文件到指定目录
                    :param url: 文件下载的url
                    :param filename: 要存放的目录及文件名，例如：./test.xls
                    :return:
                    """
        down_res = requests.get(httpurl)
        with open(filepath, 'wb') as file:
            file.write(down_res.content)
        return filepath, filename
