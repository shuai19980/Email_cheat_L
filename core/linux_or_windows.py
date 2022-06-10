#!/usr/bin/python
# -*- coding: UTF-8 -*-
import platform

#判断当前是什么操作系统
class linux_or_windows:
    def linux_or_windows(self):
        if platform.system().lower() == 'linux':
            return "linux"
        elif platform.system().lower() == 'windows':
            return "windows"
