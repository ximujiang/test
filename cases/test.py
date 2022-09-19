# -*- coding: utf-8 -*-
import requests

result = requests.request(method='get', url="https://github.com/",timeout=500)
# print(result.content)
print(result.status_code)