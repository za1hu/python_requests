import  requests
tonke = "2572260d01b94355a8528b385d5493c0"             #AccessToken
data= {"data":"{'NED':'2'}","CurrentDate":"20180101"}           #入参
r = requests.post("https://jdcdev-api.marykayintouch.com.cn/salesdevreport/v1/RCReport/1?AccessToken=%s"%tonke,data=data) #发送请求
f = open(r"C:\Users\Administrator\Desktop\test\EESD-ESD.txt","w")    #创建并打开一个txt
f.write(r.text)                                           #写入接口响应
f.close()                                                 #关闭保存txt
print(r.status_code)                                      #打印状态码