from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import json

REPLY_ENDPOINT_URL = "https://api.line.me/v2/bot/message/reply"
ACCESSTOKEN = 'aQ+HOulA6x9FVHUnNsXbzi1eys7D3rDjNkLw1UDakXCZLS1R3ZNpQMxpysVTY7wa3z31MIbNtFAU5OG844diB8FO7n3i4Un9SVMNkFc4y23q/ek8P7DPbSA3t3E6Sx98aF0mlh/JWNOH0t0CjY+3pAdB04t89/1O/w1cDnyilFU='
HEADER = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + ACCESSTOKEN
}

class LineMessage():
    def __init__(self, messages):
        self.messages = messages

    def reply(self, reply_token):
        body = {
            'replyToken': reply_token,
            'messages': self.messages
        }
        print(body)
        req = urllib.request.Request(REPLY_ENDPOINT_URL, json.dumps(body).encode(), HEADER)
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read()
        except urllib.error.HTTPError as err:
            print(err)
        except urllib.error.URLError as err:
            print(err.reason)