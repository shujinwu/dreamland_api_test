import yaml
import requests
import os


def read_config():
    base_path = os.path.dirname(os.path.abspath(__file__))
    print(base_path)
    path = base_path + '/config/config.yaml'
    # print(path)
    with open(path, 'r') as file:
        f = yaml.load(file, Loader=yaml.FullLoader)
    return f
print(read_config())

def get_token():
    user_id = read_config().get("demo").get("user_id")
    headers = {
        "MAuthorization": read_config().get("demo").get("mauthorization"),
    }
    param = {
        "m": "Api",
        "c": "User",
        "a": "token",
        "id": user_id
    }
    res = requests.get(url=read_config().get("demo").get("host"), params=param, headers=headers).json()
    return res["data"]["install_token"]
# print(get_token())

def req_headers():
    headers = {
        "mauthorization": read_config().get("demo").get("mauthorization") + ":" + get_token() + ":1",
        "apptype": read_config().get("demo").get("apptype"),
        "versioncode": read_config().get("demo").get("versioncode")
    }
    return headers
# print(req_headers())

def get_url():
    host = read_config().get("demo").get("host")
    return host

# print(get_url())