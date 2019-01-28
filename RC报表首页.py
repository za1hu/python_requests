import  requests
tonke = "249744a44f7e483a8a28a98cf8368a44"             #AccessToken
data= {"data":"{}","CurrentDate":"20180101"}              #入参
r = requests.post("https://jdcdev-api.marykayintouch.com.cn/salesdevreport/v1/RCReport/1?AccessToken=%s"%tonke,data=data) #发送请求
# f = open(r"C:\Users\Administrator\Desktop\test\首页.txt","w")    #创建并打开一个txt
# f.write(r.text)                                           #写入接口响应
# f.close()                                                 #关闭保存txt
# print(r.status_code)                                      #打印状态码
print(r.status_code)