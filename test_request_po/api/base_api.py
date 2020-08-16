import requests


class BaseApi():
    # 这里对requests再进行封装，那其他地方就不用重复导入requests,
    # 同时要是换另外的语言也可以直接使用此项目源码，只要把底层修改即可
    def send_api(self, data):
        return requests.request(**data).json()
