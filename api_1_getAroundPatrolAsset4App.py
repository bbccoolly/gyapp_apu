import requests
import json

# 定义请求的 URL
url = 'https://transport.cloudbrain2.pcl.ac.cn/mt/gateway/asset/roadSegmentation/getAroundPatrolAsset4App'

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
    'Authorization': result,  # 使用读取的 result 作为 Authorization
    'Content-Type': 'application/json',
    'Connection': 'Keep-Alive',
    'appverify': 'md5=3ff125fea11ec838ca71b73db13460be;ts=1732181062413',
    'x-mas-app-id': 'dss151624442110023',
    'Host': 'transport.cloudbrain2.pcl.ac.cn',
    # 'Content-Length': '2'  # 省略此行，requests 库会自动计算长度
}

# 请求体内容，当前为2字节的空 JSON 对象（{}）
data = json.dumps({})

# 发送 POST 请求
response = requests.post(url, headers=headers, params=params, data=data)#, verify='gy_api.pem')

# 输出返回结果
if response.status_code == 200:
    print(response.json())