import pytest
from jsonpath import jsonpath

from test_request_po.api.tag import Tag


class TestTag():
    def setup_class(self):
        self.tag = Tag()

    @pytest.mark.parametrize('group_id, old_tag_name, new_tag_name', [('g1', 't1', 't1111')])
    def test_tag(self, group_id, old_tag_name, new_tag_name):
        # 首先删除垃圾数据
        json_data = self.tag.get_alltag()
        names=jsonpath(json_data, f"$..tag[*].name")
        if old_tag_name in names:
            tag_id = jsonpath(json_data, f"$..tag[?(@.name=='{old_tag_name}')].id")[0]
            assert self.tag.delete_tag(tag_id)['errcode'] == 0
        if new_tag_name in names:
            tag_id = jsonpath(json_data, f"$..tag[?(@.name=='{new_tag_name}')].id")[0]
            assert self.tag.delete_tag(tag_id)['errcode'] == 0
        # 新增企业标签
        assert self.tag.add_tag(group_id, old_tag_name)['errcode'] == 0
        # 更新企业标签
        json_data = self.tag.get_alltag()
        tag_id = jsonpath(json_data, f"$..tag[?(@.name=='{old_tag_name}')].id")[0]
        assert self.tag.update_tag(tag_id, new_tag_name)['errcode'] == 0
