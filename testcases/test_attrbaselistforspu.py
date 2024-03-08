import requests
import pytest
import allure
import json
from requests.exceptions import JSONDecodeError

@pytest.fixture
def base_url():
    return "http://localhost:8001"

@pytest.fixture
def attrbase_listforspu_url(base_url):
    return f"{base_url}/product/attr/base/listforspu/11"


def test_grouplist(attrbase_listforspu_url):
    with allure.step("发起请求"):
        r = requests.get(attrbase_listforspu_url)

    with allure.step("检查响应状态码"):
        assert r.status_code == 200

    with allure.step("解析 JSON 数据"):
        data = r.text

    try:
        result = r.json()
        print(result)
        json_data = json.loads(data)
        print("解析成功",json_data)
    except json.JSONDecodeError as e:
        print("响应返回的内容并不是json格式")
        print("这个接口返回的状态码是：",r.status_code)
        print("这个接口的请求头是：",r.headers)
        print("解析失败:",e)
