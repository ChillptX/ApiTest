import requests
import pytest
import json
import allure
from requests.exceptions import JSONDecodeError

@pytest.fixture
def base_url():
    return "http://localhost:8001"

@pytest.fixture
def purchasedetail_list_url(base_url):
    return f"{base_url}/ware/purchasedetail/list"

def test_wareskulist(purchasedetail_list_url):
    with allure.step("发起请求"):
        r = requests.get(purchasedetail_list_url,params={
        "page": "1",
        "limit": "10",
        "sidx": 'id',
        "order": 'asc/desc',
        "key": '华为',
        "status": "0",
        "wareId": "1"
        })

    with allure.step("检查响应状态码"):
        assert r.status_code == 200

    try:
        result = r.json()
        assert result['msg'] == "success"
        assert result['code'] == "0"
    except json.JSONDecodeError as e:
        print("响应返回的内容并不是json格式")
        print("这个接口返回的状态码是：", r.status_code)
        print("这个接口的请求头是：", r.headers)
        print("解析失败:", e)
