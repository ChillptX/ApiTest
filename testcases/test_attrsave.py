import requests
import pytest
import json
import allure
from requests.exceptions import JSONDecodeError

@pytest.fixture
def base_url():
    return "http://localhost:8001"

@pytest.fixture
def attrsave_url(base_url):
    return f"{base_url}/product/attr/save"

def test_attrsave(attrsave_url):
    with allure.step("发起请求"):
        r = requests.post(attrsave_url,params={
        "attrGroupId": "0",
        "attrName": 'string',
        "attrType": "0",
        "catelogId": "0,",
        "enable": "0",
        "icon": 'string',
        "searchType": "0",
        "showDesc": "0",
        "valueSelect": 'string',
        "valueType": "0"
        })
    with allure.step("检查响应状态码"):
        assert r.status_code == 200

    try:
        result = r.json()
        assert "data" in result
        assert "total" in result
        assert "page" in result
        assert "limit" in result
    except json.JSONDecodeError as e:
        print("响应返回的内容并不是json格式")
        print("这个接口返回的状态码是：", r.status_code)
        print("这个接口的请求头是：", r.headers)
        print("解析失败:", e)

