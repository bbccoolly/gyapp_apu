import requests

# 定义请求的 URL
url = 'https://transport.cloudbrain2.pcl.ac.cn/mt/gateway/app/patrols/userProfile?_=' + str(1732180572799)

# 定义请求头
headers = {
    'Cookie': 'HWWAFSESID=83e6b19367dc3286721; HWWAFSESTIME=1732179936266',
    'User-Agent': 'Mozilla/5.0 (Linux; U; Mobile; Android 9;SM-S9160 Build/FRF91)',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate',
    'x-mas-app-id': 'dss151624442110023',
    'appverify': 'md5=6e9bdf9c56229f31a6ba1ee02a76cd16;ts=1732180572833',
    'Charset': 'UTF-8',
    'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50SWQiOiIxM2MzN2Q2ZjYwNzE0MDgzOWFhNDJlZTg4YzQwYTgyMCIsImVtYWlsIjoibXVuaWNpcGFsdHBucnRAc3pld2VjLmNvbSIsIm5hbWUiOiLljZflsbHlkIzpmYbkupHpg5Hph5HmtpsiLCJ1c2VybmFtZSI6InpqdHRndmZiMyIsInBob25lTnVtYmVyIjoiMTM1MzA4MTU5ODMiLCJhY2NvdW50VHlwZSI6IlBFUlNPTkFMIiwidXNlcklkIjoiNjcwYWU3ZTZmMjdhNDg4YWI2NTNiNjFlMDE2MWFmOTEiLCJjb21wYW55SWQiOiIwY2ZlM2ZjM2ZlM2U0YWY0OGYxNDc4MzcwYmU2YTY4ZSIsImNvbXBhbnlOYW1lIjoi5rex5Zyz5biC5Lqk6YCa6L-Q6L6T5bGAIiwiZXhwIjoxNzMyMjE2MDExfQ.N5U4_sC4tX4cbunZ2rRna7fVuL1URRDNEM_mmCSxz9M.MTM1MzA4MTU5ODM=',
    'Connection': 'Keep-Alive',
    'Host': 'transport.cloudbrain2.pcl.ac.cn'
}

# 发送 GET 请求并使用证书文件进行 SSL 验证
response = requests.get(url, headers=headers, verify='gy_api.pem')  # 替换为你的证书路径

# 输出返回结果
if response.status_code == 200:
    print(response.json())  # 假设返回的是 JSON 数据
else:
    print(f'Error: {response.status_code}')
    print(response.text)  # 输出错误信息