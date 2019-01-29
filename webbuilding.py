import  requests
url = "http://www.w3school.com.cn/w.asp"
header="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
r = requests.get(url=url,params=header)
print(r.status_code)