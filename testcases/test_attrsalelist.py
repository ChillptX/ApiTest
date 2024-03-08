import requests
import pytest
import json
import allure
from requests.exceptions import JSONDecodeError

@pytest.fixture
def base_url():
    return "http://localhost:8001"

@pytest.fixture
def attr_salelist_url(base_url):
    return f"{base_url}/product/attr/sale/list/4"

def test_grouplist(attr_salelist_url):

    with allure.step("发起请求"):
        r = requests.get(attr_salelist_url)

    with allure.step("检查响应状态码"):
        assert r.status_code == 200

    try:
        content_type = r.headers.get('content-type', '')
        if 'application/json' not in content_type:
            raise ValueError("响应内容不是 JSON 格式")

        result = r.json()
        assert result['msg'] == "success"
        assert result['code'] == "0"
    except requests.RequestException as e:
        print("请求失败:", e)
        allure.attach(str(e), name="Request Exception")
    except ValueError as e:
        print("响应返回的内容不是json格式:", e)
        print("这个接口返回的状态码是：", r.status_code)
        print("这个接口的请求头是：", r.headers)
        allure.attach(f"Response Content Type: {content_type}", name="Response Content Type")
        allure.attach(f"Response Status Code: {r.status_code}", name="Response Status Code")
        allure.attach(str(r.headers), name="Response Headers")
    except json.JSONDecodeError as e:
        print("解析失败:", e)
        allure.attach(str(e), name="JSON Decode Error")

