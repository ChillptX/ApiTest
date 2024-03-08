import allure
import requests
import pytest
import json
from requests.exceptions import JSONDecodeError

@pytest.fixture
def base_url():
    return "http://localhost:8001"

@pytest.fixture
def spuinfo_list_url(base_url):
    return f"{base_url}/product/spuinfo/list"


def test_spuinfolist(spuinfo_list_url):
    with allure.step("发起请求"):
        r = requests.get(spuinfo_list_url,params={
        "page": "1",
        "limit": "10",
        "sidx": 'id',
        "order": 'asc/desc',
        "key": '华为',
        "catelogId": "6",
        "brandId": "1",
        "status": "0"
        })

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
