import requests
import pytest
import allure
import json
from requests.exceptions import JSONDecodeError

@pytest.fixture
def base_url():
    return "http://localhost:8001"

@pytest.fixture
def spuinfo_save_url(base_url):
    return f"{base_url}/product/spuinfo/save"


def test_spuinfosave(spuinfo_save_url):
    with allure.step("发起请求"):
        r = requests.post(spuinfo_save_url,params={
        "spuName": "iphone 14 pro",
        "spuDescription": "iphone 14 pro",
        "catalogId": "225",
        "brandId": "12",
        "weight": "0.2",
        "publishStatus": "0",
        "decript": [
            "https://gulimall-hello.oss-cn-beijing.aliyuncs.com/2019-11-22//66d30b3f-e02f-48b1-8574-e18fdf454a32_f205d9c99a2b4b01.jpg"],
        "images": [
            "https://gulimall-hello.oss-cn-beijing.aliyuncs.com/2019-11-22//dcfcaec3-06d8-459b-8759-dbefc247845e_5b5e74d0978360a1.jpg",
            "https://gulimall-hello.oss-cn-beijing.aliyuncs.com/2019-11-22//5b15e90a-a161-44ff-8e1c-9e2e09929803_749d8efdff062fb0.jpg"],
        "bounds": {
            "buyBounds": "500",
            "growBounds": "6000"
        },
        "baseAttrs": [{
            "attrId": "7",
            "attrValues": "aaa;bb",
            "showDesc": "1"
        }, {
            "attrId": "8",
            "attrValues": "2019",
            "showDesc": "0"
        }],
        "skus": [{
            "attr": [{
                "attrId": "9",
                "attrName": "颜色",
                "attrValue": "黑色"
            }, {
                "attrId": "10",
                "attrName": "内存",
                "attrValue": "6GB"
            }],
            "skuName": "Apple XR 黑色 6GB",
            "price": "1999",
            "skuTitle": "Apple XR 黑色 6GB",
            "skuSubtitle": "Apple XR 黑色 6GB",
            "images": [{
                "imgUrl": "https://gulimall-hello.oss-cn-beijing.aliyuncs.com/2019-11-22//dcfcaec3-06d8-459b-8759-dbefc247845e_5b5e74d0978360a1.jpg",
                "defaultImg": "1"
            }, {
                "imgUrl": "https://gulimall-hello.oss-cn-beijing.aliyuncs.com/2019-11-22//5b15e90a-a161-44ff-8e1c-9e2e09929803_749d8efdff062fb0.jpg",
                "defaultImg": "0"
            }],
            "descar": ["黑色", "6GB"],
            "fullCount": "5",
            "discount": "0.98",
            "countStatus": "1",
            "fullPrice": "1000",
            "reducePrice": "10",
            "priceStatus": "0",
            "memberPrice": [{
                "id": 1,
                "name": "aaa",
                "price": "1998.99"
            }]
        }, {
            "attr": [{
                "attrId": "9",
                "attrName": "颜色",
                "attrValue": "黑色"
            }, {
                "attrId": "10",
                "attrName": "内存",
                "attrValue": "12GB"
            }],
            "skuName": "Apple XR 黑色 12GB",
            "price": "2999",
            "skuTitle": "Apple XR 黑色 12GB",
            "skuSubtitle": "Apple XR 黑色 6GB",
            "images": [{
                "imgUrl": "",
                "defaultImg": "0"
            }, {
                "imgUrl": "",
                "defaultImg": "0"
            }],
            "descar": ["黑色", "12GB"],
            "fullCount": "0",
            "discount": "0",
            "countStatus": "0",
            "fullPrice": "0",
            "reducePrice": "0",
            "priceStatus": "0",
            "memberPrice": [{
                "id": "1",
                "name": "aaa",
                "price": "1998.99"
            }]
        }, {
            "attr": [{
                "attrId": "9",
                "attrName": "颜色",
                "attrValue": "白色"
            }, {
                "attrId": "10",
                "attrName": "内存",
                "attrValue": "6GB"
            }],
            "skuName": "Apple XR 白色 6GB",
            "price": "1998",
            "skuTitle": "Apple XR 白色 6GB",
            "skuSubtitle": "Apple XR 黑色 6GB",
            "images": [{
                "imgUrl": "",
                "defaultImg": "0"
            }, {
                "imgUrl": "",
                "defaultImg": "0"
            }],
            "descar": ["白色", "6GB"],
            "fullCount": "0",
            "discount": "0",
            "countStatus": "0",
            "fullPrice": "0",
            "reducePrice": "0",
            "priceStatus": "0",
            "memberPrice": [{
                "id": "1",
                "name": "aaa",
                "price": "1998.99"
            }]
        }, {
            "attr": [{
                "attrId": "9",
                "attrName": "颜色",
                "attrValue": "白色"
            }, {
                "attrId": "10",
                "attrName": "内存",
                "attrValue": "12GB"
            }],
            "skuName": "Apple XR 白色 12GB",
            "price": "2998",
            "skuTitle": "Apple XR 白色 12GB",
            "skuSubtitle": "Apple XR 黑色 6GB",
            "images": [{
                "imgUrl": "",
                "defaultImg": "0"
            }, {
                "imgUrl": "",
                "defaultImg": "0"
            }],
            "descar": ["白色", "12GB"],
            "fullCount": "0",
            "discount": "0",
            "countStatus": "0",
            "fullPrice": "0",
            "reducePrice": "0",
            "priceStatus": "0",
            "memberPrice": [{
                "id": 1,
                "name": "aaa",
                "price": "1998.99"
            }]
        }]
    })

    with allure.step("检查响应状态码"):
        assert r.status_code == 200

    try:
        result = r.json()
        print(result)
    except json.JSONDecodeError as e:
        print("响应返回的内容并不是json格式")
        print("这个接口返回的状态码是：", r.status_code)
        print("这个接口的请求头是：", r.headers)
        print("解析失败:", e)