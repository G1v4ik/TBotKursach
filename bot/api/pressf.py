import json

import requests
import pyotp

class PressF:

    def __init__(self, url, base_32):
        self.url = url
        self.token = pyotp.TOTP(base_32).now()
    