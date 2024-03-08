import requests
import pytest
import json
import allure
from requests.exceptions import JSONDecodeError

@pytest.fixture
def attrgroup_info_url():
    return "http://localhost:8001/product/attrgroup/info/1"

def test_groupinfo(attrgroup_info_url):
    with allure.step("发起请求"):
        r = requests.get(attrgroup_info_url)

    with allure.step("检查响应状态码"):
        assert r.status_code == 200

    try:
        result = r.json()
        assert result['msg'] == "success"
        assert 'code' in result
    except json.JSONDecodeError as e:
        print("响应返回的内容并不是json格式")
        print("这个接口返回的状态码是：", r.status_code)
        print("这个接口的请求头是：", r.headers)
        print("解析失败:", e)
