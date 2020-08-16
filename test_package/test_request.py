import json

import requests
from jsonpath import jsonpath


class TestRequest():

    def setup_class(self):
        secret = 'G1IFNUioR6z86QbclcYsW1uVkPLLhYm-yMdNUrTlGHE'
        corpid = 'wwed02ee7e67aa4a02'
        url = f' https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={secret}'
        r = requests.get(url)
        self.token = r.json()['access_token']
        print(r.json())

    def test_gettoken(self):
        name = '部门1'
        # 获取部门列表
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}')
        json_path = f"$.department[?(@.name=='{name}')].id"
        name_id = jsonpath(r.json(), json_path)[0]
        if name_id:
            # 删除部门
            r = requests.get(
                f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={name_id}')
            print(r.json())
            assert r.json()['errcode'] == 0

        # 新建部门
        data = {
            "name": name,
            "parentid": 1
        }
        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}', json=data)
        assert r.json()['errcode'] == 0

        # 更新部门
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}')
        json_path = f"$.department[?(@.name=='{name}')].id"
        name_id = jsonpath(r.json(), json_path)[0]
        data= {
            "id": name_id,
            "name": "部门11"
        }
        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}', json=data)
        assert r.json()['errcode'] == 0

        # print(name_id)
        # # print('name_id ======' + str(name_id))
        # # print(r.json())
        # print(json.dumps(r.json(), indent=1))
