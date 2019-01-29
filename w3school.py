import  requests
url = "http://www.w3school.com.cn"
r = requests.get(url=url)
print(r.status_code)