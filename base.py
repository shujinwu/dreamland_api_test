import common
import requests


def api_get(url, params):
    headers = common.req_headers()
    return requests.get(url=url, headers=headers, params=params).json()


def api_post(url, params, data):
    headers = common.req_headers()
    respone = requests.post(url=url, params=params, headers=headers, data=data).json()
    return respone
