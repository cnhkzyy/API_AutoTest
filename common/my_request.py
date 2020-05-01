import requests


def send_request(method, url, **kwargs):
    result = requests.request(method, url, **kwargs).json()
    return result


if __name__ == "__main__":
    method = "post"
    url = "http://localhost:8099/futureloan/mvc/api/member/register"
    request_data = {"mobilephone": "13623456960", "pwd": "test123"}
    send_request(method, url, data=request_data)


