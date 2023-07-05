import requests
import json

def send_data(target, **kwargs):
    requests.post(target, **kwargs)