
from test_request_po.api.base_api import BaseApi


class Wework(BaseApi):
    # vFtNYzIjsNZ_dVAYTq7vYTsnJEGh0wRCtM1k1sWx70I
    corpid = 'wwed02ee7e67aa4a02'

    def get_token(self, secret):
        data = {
            'method':'get',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            'params': {
                'corpid': self.corpid,
                'corpsecret': secret
            }
        }
        return self.send_api(data)['access_token']

