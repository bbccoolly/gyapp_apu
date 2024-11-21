#
#
# 设施名称
#
#

import requests
import json

# 定义请求的 URL
url = 'https://transport.cloudbrain2.pcl.ac.cn/mt/gateway/asset/roadSegmentation/getAroundPatrolAsset4App'
params = {
    'isDelete': 'N',
    'assetTypes': '路基路面,城市桥梁,地下通道,涌洞,隧道,边坡挡墙,电缆',
    'maintain': '是',
    'page': 1,
    'limit': 15,
    '_': 1732181062388
}

# 定义请求头
headers = {
    'Cookie': 'HWWAFSESID=83e6b19367dc3286721; HWWAFSESTIME=1732179936266',
    'User-Agent': 'Mozilla/5.0 (Linux; U; Mobile; Android 9;SM-S9160 Build/FRF91)',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate',
    'Charset': 'UTF-8',
    'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50SWQiOiIxM2MzN2Q2ZjYwNzE0MDgzOWFhNDJlZTg4YzQwYTgyMCIsImVtYWlsIjoibXVuaWNpcGFsdHBucnRAc3pld2VjLmNvbSIsIm5hbWUiOiLljZflsbHlkIzpmYbkupHpg5Hph5HmtpsiLCJ1c2VybmFtZSI6InpqdHRndmZiMyIsInBob25lTnVtYmVyIjoiMTM1MzA4MTU5ODMiLCJhY2NvdW50VHlwZSI6IlBFUlNPTkFMIiwidXNlcklkIjoiNjcwYWU3ZTZmMjdhNDg4YWI2NTNiNjFlMDE2MWFmOTEiLCJjb21wYW55SWQiOiIwY2ZlM2ZjM2ZlM2U0YWY0OGYxNDc4MzcwYmU2YTY4ZSIsImNvbXBhbnlOYW1lIjoi5rex5Zyz5biC5Lqk6YCa6L-Q6L6T5bGAIiwiZXhwIjoxNzMyMjE2MDExfQ.N5U4_sC4tX4cbunZ2rRna7fVuL1URRDNEM_mmCSxz9M.MTM1MzA4MTU5ODM=',
    'Content-Type': 'application/json',
    'Connection': 'Keep-Alive',
    'appverify': 'md5=3ff125fea11ec838ca71b73db13460be;ts=1732181062413',
    'x-mas-app-id': 'dss151624442110023',
    'Host': 'transport.cloudbrain2.pcl.ac.cn',
    'Content-Length': '2'  # 这里可以省略，因为 requests 库会自动计算长度
}

# 请求体内容
data = json.dumps({})  # 如果你的请求体实际需要数据，可以在这里填充数据。当前为2字节的空 JSON 对象（{}）

# 发送 POST 请求
response = requests.post(url, headers=headers, params=params, data=data, verify='gy_api.pem')

# 输出返回结果
if response.status_code == 200:
    print(response.json())  # 假设返回的是 JSON 数据
else:
    print(f'Error: {response.status_code}')
    print(response.text)  # 输出错误信息
