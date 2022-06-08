# Email-cheat-L
###此项目主要功能:
  1.邮件伪造
  2.批量邮件
  
可以进行批量发送邮件进行钓鱼

###文件结构如下:  
    
    core  
        --sendmail.py
    file
        --邮箱账号.txt
        --邮件内容.html
     main.py
     
     邮件内容直接修改"邮件内容.html"的内容即可
###如何运行  
在main.py中填写邮件服务器,邮箱账号,邮箱授权码,邮箱header(填写你要伪造的邮箱),邮箱标题即可。  
![](images/使用方法1.jpg)  
####邮件授权码获取
这里以163邮箱举例:  
![](images/授权码1.jpg)  
![](images/授权码2.jpg)  
####启动
    执行命令:
        python3 main.py
###效果
企业邮箱:  
![](images/企业邮箱.jpg)
QQ邮箱:  
![](images/qq邮箱.jpg)
由于各企业邮箱显示不同,所以部分邮箱达不到邮件伪造的目的,自行测试。