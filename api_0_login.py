import requests
import json

# 定义请求的 URL
url = 'https://platform-gateway.gcnao.cn/account/appLoginV1'

# 定义查询参数 (URL 查询参数)
params = {
    '_': 1732237520193  # 根据你的消息，更新为适当的值
}

# 定义请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Mobile; Android 9;SM-S9160 Build/FRF91)',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate',
    'Charset': 'UTF-8',
    'Connection': 'Keep-Alive',
    'appverify': 'md5=4cd8047264b5180bd17ac3098e9bf13f;ts=1732237520311',
    'x-mas-app-id': 'dss151624442110023',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'platform-gateway.gcnao.cn'
}

# 定义请求体内容
data = {
    'data': '+qDzqmLX02BP1qe0hE04X6+DSK52yj3LFYWUJ4hBvIOfaK7Arbxwn/9CrRU9PTs9hbSPR4QRaKlV4m+N4b2kq8gcJDFy+AwX98AjWhKXs2WDUzoWPwJyDsepvIjb7dzNB+k+/HkSoKR44tmjNoGyUQ3sD9UMq6h1YQ5NXPMEeCc='
}

# 发送 POST 请求
response = requests.post(url, headers=headers, params=params, data=data)#, verify='gy_api.pem')

# 输出返回结果
print(f'Status Code: {response.status_code}')  # 打印状态码
if response.status_code == 200:
    try:
        json_response = response.json()  # 尝试解析 JSON 响应
        print(json.dumps(json_response, indent=4, ensure_ascii=False))  # 美化输出 JSON 数据

        # 提取所需的结果
        result = json_response.get('result')
        if result:
            # 将结果保存到 JSON 文件
            with open('login_result.json', 'w', encoding='utf-8') as json_file:
                json.dump({'result': result}, json_file, ensure_ascii=False, indent=4)

            print("Login result saved to 'login_result.json'")
        else:
            print("No result found in the response.")

    except ValueError as e:
        print(f'Error parsing JSON: {e}')
else:
    print(f'Error: {response.status_code}')  # 打印错误状态码
    print(response.text)  # 输出错误信息

# 读取保存的登录结果
try:
    with open('login_result.json', 'r', encoding='utf-8') as json_file:
        login_data = json.load(json_file)
        print("Loaded login data:", login_data)
except FileNotFoundError:
    print("Login result file not found.")