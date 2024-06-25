import requests

def send_data(target, **kwargs):
    requests.post(target, **kwargs)