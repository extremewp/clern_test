import requests

y = requests.get("https://www.baidu.com")
#   查看请求返回请求错误状态码
print(y.status_code)
# 查看请求字体编码如UTF-8
print(y.encoding)
# 查看txt文档
# print(y.text)
# 设置字体为utf-8
y.encoding = "utf-8";
print(y.text)