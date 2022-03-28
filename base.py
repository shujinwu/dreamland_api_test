import common
import requests


def api_get(url, params):
    headers = common.req_headers()
    return requests.get(url=url, headers=headers, params=params)


def api_post(url, data):
    headers = common.req_headers()
    respone = requests.get(url=url, headers=headers, data=data).json()
    return respone
