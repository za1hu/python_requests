import  requests,json
tonke = "2572260d01b94355a8528b385d5493c0"             #AccessToken
esdkey = "7"                                                #ESDKey
bcflag = "2"                                                #BCFlag
numberflag = "0"                                            #LineNumberFlag
cl = "0"                                                    #CL
kpi = "0"                                                   #KPI
condition = "0"                                             #Condition
valuse = "0"                                                #Values
data= \
    {'data':{'{"ESDKey":%s,"BCFlag":%s,"LineNumberFlag":%s,"CL":%s,"KPI":%s,"Condition":%s,"Values":%s}'\
             %(esdkey,bcflag,numberflag,cl,kpi,condition,valuse)},'CurrentDate':'20180101'}    #入参
r = requests.post("https://jdcdev-api.marykayintouch.com.cn/salesdevreport/v1/RCReport/3?AccessToken=%s"%tonke,data=data) #发送请求
# f = open(r"C:\Users\Administrator\Desktop\test\RC报表区域明细.txt","w")    #创建并打开一个txt
#
# f.write(r.text)                                           #写入接口响应
# f.close()                                                 #关闭保存txt

# print(r.status_code)                                      #打印状态码
# print(r.headers)
print(r.raw)