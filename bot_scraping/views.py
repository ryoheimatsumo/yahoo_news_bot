from django.shortcuts import render
import json
import random
import requests
import scraping as sc
import re

from django.shortcuts import render
from django.http import HttpResponse


REPLY_ENDPOINT = 'https://sample-bot-line111.herokuapp.com/callback/'
ACCESS_TOKEN = 'coWmXP5AQuEvAXR+dVPQlsjLUGbRJqyyO5KoDt4JIaLSrOjbakB+O5ZxOYIb9x77nPDXppgXaJ12+G93QQepUV6QR+Yk4oAB+kS3LFZPSSmCFnVJGlD1ZPDbpfYFTTPO7f0X7utim2C2S+3UifM0bQdB04t89/1O/w1cDnyilFU='
HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}

def index(request):
    return HttpResponse("This is bot api.")


def reply_text(reply_token,text):
    if text == re.compile("all", re.IGNORECASE):
        reply = sc.getAllTopics()
    else:
        reply = sc.getNews(text)
        payload = {
        "replyToken":reply_token,
        "messages":[
        {
        "type":"text",
        "text": reply
        }
        ]
        }

    requests.post(REPLY_ENDPOINT, headers=HEADER, data=json.dumps(payload)) # LINEにデータを送信
    return reply

def callback(request):
    reply = ""
    request_json = json.loads(request.body.decode('utf-8')) # requestの情報をdict形式で取得
    for e in request_json['events']:
        reply_token = e['replyToken']  # 返信先トークンの取得
        message_type = e['message']['type']   # typeの取得

        if message_type == 'text':
            text = e['message']['text']    # 受信メッセージの取得
            reply += reply_text(reply_token, text)   # LINEにセリフを送信する関数
    return HttpResponse(reply)  # テスト用
