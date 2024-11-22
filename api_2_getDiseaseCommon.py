



# 根据设施名称获取 构建列表



import requests
import json

# 定义请求的 URL
url = 'https://transport.cloudbrain2.pcl.ac.cn/mt/gateway/repair/diseaseCommon/getDiseaseCommon'

# 读取保存的登录结果
try:
    with open('login_result.json', 'r', encoding='utf-8') as json_file:
        login_data = json.load(json_file)
        result = login_data['result']  # 提取 result
except FileNotFoundError:
    print("Login result file not found.")
    exit()  # 如果文件未找到，则终止程序

# 定义请求参数 (URL 查询参数)
params = {
    '_': '1732181574197'  # 时间戳参数
}

# 定义请求头
headers = {
    'Cookie': 'HWWAFSESID=83e6b19367dc3286721; HWWAFSESTIME=1732179936266',
    'User-Agent': 'Mozilla/5.0 (Linux; U; Mobile; Android 9;SM-S9160 Build/FRF91)',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate',
    'Charset': 'UTF-8',
    'Authorization': result,  # 使用读取的 result 作为 Authorization
    'Content-Type': 'application/json',
    'Connection': 'Keep-Alive',
    'appverify': 'md5=66c5bb1b6eb2d7d59bdb6000c45cdae5;ts=1732181574280',
    'x-mas-app-id': 'dss151624442110023',
    'Host': 'transport.cloudbrain2.pcl.ac.cn',
}

# 请求体内容
data = {
    "type": "2",
    "facilityType": "路基路面",
    "createUser": "670ae7e6f27a488ab653b61e0161af91",
    "limit": 12
}

# 将请求体转换为 JSON 格式
data_json = json.dumps(data)

# 发送 POST 请求
response = requests.post(url, headers=headers, params=params, data=data_json)#, verify='gy_api.pem')

# 输出返回结果
print(f'Status Code: {response.status_code}')  # 打印状态码

if response.status_code == 200:
    print(response.text)  # 打印原始响应文本
    try:
        print(response.json())  # 解析 JSON 响应
    except ValueError as e:
        print(f'Error parsing JSON: {e}')
else:
    print(f'Error: {response.status_code}')
    print(response.text)  # 输出错误信息