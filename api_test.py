import requests

# 定义请求的 URL
url = 'https://transport.cloudbrain2.pcl.ac.cn/mt/gateway/system/todo/queryTodoList?client=APP&userId=670ae7e6f27a488ab653b61e0161af91&_=1732166379360'

# 定义请求头
headers = {
    'Host': 'transport.cloudbrain2.pcl.ac.cn',
    'Connection': 'keep-alive',
    'Content-Length': '0',  # 若无需发送请求体，此字段可选
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Linux; U; Mobile; Android 9;SM-S9160 Build/FRF91 )',
    'DNT': '1',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Accept': '*/*',
    'Origin': 'chrome-extension://eejfoncpjfgmeleakejdcanedmefagga',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'HWWAFSESID=d8f828e2cb25d72367; HWWAFSESTIME=1732166379360',
    'authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50SWQiOiIxM2MzN2Q2ZjYwNzE0MDgzOWFhNDJlZTg4YzQwYTgyMCIsImVtYWlsIjoibXVuaWNpcGFsdHBucnRAc3pld2VjLmNvbSIsIm5hbWUiOiLljZflsbHlkIzpmYbkupHpg5Hph5HmtpsiLCJ1c2VybmFtZSI6InpqdHRndmZiMyIsInBob25lTnVtYmVyIjoiMTM1MzA4MTU5ODMiLCJhY2NvdW50VHlwZSI6IlBFUlNPTkFMIiwidXNlcklkIjoiNjcwYWU3ZTZmMjdhNDg4YWI2NTNiNjFlMDE2MWFmOTEiLCJjb21wYW55SWQiOiIwY2ZlM2ZjM2ZlM2U0YWY0OGYxNDc4MzcwYmU2YTY4ZSIsImNvbXBhbnlOYW1lIjoi5rex5Zyz5biC5Lqk6YCa6L-Q6L6T5bGAIiwiZXhwIjoxNzMyMjE2MDExfQ.N5U4_sC4tX4cbunZ2rRna7fVuL1URRDNEM_mmCSxz9M.MTM1MzA4MTU5ODM='
}

# 发送 POST 请求，并禁用 SSL 证书验证
response = requests.post(url, headers=headers, verify=False)

# 输出返回结果
if response.status_code == 200:
    print(response.json())
else:
    print(f'Error: {response.status_code}')
    print(response.text)