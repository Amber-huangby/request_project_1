from jsonpath import jsonpath

from test_request_po.api.tag import Tag
from test_request_po.api.wework import Wework


class Test1():
    def setup_class(self):
        self.tag = Tag()

    def test_token(self):
        print(Wework().get_token('vFtNYzIjsNZ_dVAYTq7vYTsnJEGh0wRCtM1k1sWx70I'))

    def test_add(self):
        json_data = self.tag.get_alltag()
        tag_id = jsonpath(json_data, f"$..tag[?(@.name=='t1')].id")
        print(tag_id)
        assert self.tag.update_tag(tag_id, 't1111')['errcode'] == 0