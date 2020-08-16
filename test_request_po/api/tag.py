from test_request_po.api.base_api import BaseApi
from test_request_po.api.wework import Wework


class Tag(BaseApi):
    secret = 'vFtNYzIjsNZ_dVAYTq7vYTsnJEGh0wRCtM1k1sWx70I'

    def __init__(self):
        self.token = Wework().get_token(self.secret)

    def add_tag(self, group_name, tag_name):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            'params': {
                'access_token': self.token
            },
            'json': {
                "group_name": group_name,
                "tag": [{"name": tag_name}]
            }

        }
        return self.send_api(data)

    def get_alltag(self):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            'params': {
                'access_token': self.token
            }
        }
        return self.send_api(data)

    def delete_tag(self, tag_id):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            'params': {
                'access_token': self.token
            },
            'json': {
                "tag_id": [tag_id]
            }
        }
        return self.send_api(data)

    def update_tag(self, tag_id, new_tag_name):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            'params': {
                'access_token': self.token
            },
            'json': {
                'id': tag_id,
                'name': new_tag_name
            }
        }
        return self.send_api(data)
