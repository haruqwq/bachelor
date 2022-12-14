from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

from apscheduler.schedulers.background import BackgroundScheduler

from card.models import *
import json

from django.forms.models import model_to_dict

import datetime

from utils import message_creater

JST = datetime.timezone(datetime.timedelta(hours=9), "JST")

def answer_check(ID):
    print('呼び出し成功')
    list = []
    post = Card.objects.get(id=ID)
    # ディクショナリ型に変換
    post_dict = model_to_dict(post)
    # 辞書型からJSON型の文字列に変換
    json.dumps(post_dict)
    message = ['選択肢1'+post.answer_fake1, '選択肢2'+post.answer_fake2, '選択肢3'+post.answer]
    for i in range (0,3):
        line_bot_api.broadcast(TextSendMessage(text = message[i]))

def utc_to_jst(timestamp_utc):
    datetime_utc = datetime.datetime.strptime(timestamp_utc + "+0000", "%Y-%m-%d %H:%M:%S.%f%z")
    datetime_jst = datetime_utc.astimezone(datetime.timezone(datetime.timedelta(hours=+9)))
    timestamp_jst = datetime.datetime.strftime(datetime_jst, '%Y-%m-%d %H:%M:%S.%f')
    return timestamp_jst

def change1(original_time):
    s = str(original_time)
    target = '+'
    idx = s.find(target)
    r = s[:idx]
    return r

def change2(changed_time):
    s = str(changed_time)
    target = '.'
    idx = s.find(target)
    r = s[:idx]
    return r

# 総カード枚数の計測
all = Card.objects.all().count()

line_bot_api = LineBotApi('aQ+HOulA6x9FVHUnNsXbzi1eys7D3rDjNkLw1UDakXCZLS1R3ZNpQMxpysVTY7wa3z31MIbNtFAU5OG844diB8FO7n3i4Un9SVMNkFc4y23q/ek8P7DPbSA3t3E6Sx98aF0mlh/JWNOH0t0CjY+3pAdB04t89/1O/w1cDnyilFU=')

# 経過時間の判定
def spend_time(spend_check, i):

    one_day = 86400 #1日の秒数

    # 実際に使用する時間
    # if spend_check > one_day*30: # 6回目の復習
    #     print("30日経過:" + post_dict['question'])
    # elif spend_check > one_day*14: # 5回目の復習
    #     print("14日経過:" + post_dict['question'])
    # elif spend_check > one_day*7: # 4回目の復習
    #     print("7日経過:" + post_dict['question'])
    # elif spend_check > one_day7: # 3回目の復習
    #     print("2日経過:" + post_dict['question'])
    # elif spend_check > one_day*24: # 2回目の復習
    #     print("1日経過:" + post_dict['question'])
    # elif spend_check > one_day//72: # 1回目の復習
    #     print("1時間経過:" + post_dict['question'])
    # else:
    #     print("作成直後")    
    # 開発用の時間
    one_minute = 60
    post = Card.objects.get(id=message_creater.m[i])
    if spend_check > one_minute*60 and post.review>=5:
        post.review=6
        post.save()
        print("1時間経過:" + post.question)
        print("学習回数:" + str(post.review))
        line_bot_api.broadcast(TextSendMessage(text = "6回目の学習:\n" + post.question))
    elif spend_check > one_minute*50:
        post.review=5
        post.save()
        print("50分経過:" + post.question)
        print("学習回数:" + str(post.review))
        line_bot_api.broadcast(TextSendMessage(text = "5回目の学習:\n" + post.question))
        answer_check(message_creater.m[i])
    elif spend_check > one_minute*40:
        post.review=4
        post.save()
        print("40分経過:" + post.question)
        print("学習回数:" + str(post.review))
        line_bot_api.broadcast(TextSendMessage(text = "4回目の学習:\n" + post.question))
        answer_check(message_creater.m[i])
    elif spend_check > one_minute*30:
        post.review=3
        post.save()
        print("30分経過:" + post.question)
        print("学習回数:" + str(post.review))
        line_bot_api.broadcast(TextSendMessage(text = "3回目の学習:\n" + post.question))
        answer_check(message_creater.m[i])
    elif spend_check > one_minute*20:
        post.review=2
        post.save()
        print("20分経過:" + post.question)
        print("学習回数:" + str(post.review))
        line_bot_api.broadcast(TextSendMessage(text = "2回目の学習:\n" + post.question))
        answer_check(message_creater.m[i])
    elif spend_check > one_minute*10:
        post.review=1
        post.save()
        print("10分経過:" + post.question)
        print("学習回数:" + str(post.review))
        line_bot_api.broadcast(TextSendMessage(text = "1回目の学習:\n" + post.question))
        answer_check(message_creater.m[i])
    elif spend_check > one_minute*60:
        print('学習済みです')
    else:
        print("まだ学習時期にあるカードはありません")


def periodic_execution():
    for i in range(0,message_creater.all_card):
        post = Card.objects.get(id=message_creater.m[i])
        # ディクショナリ型に変換
        post_dict = model_to_dict(post)
        # 辞書型からJSON型の文字列に変換
        json.dumps(post_dict)

        start = post.created_at  # 開始時刻を取得
        end = datetime.datetime.now(JST)  # 終了時刻を取得
        
        # 経過時間
        dif = end - start

        # 成形(end4とdif4をmessageへの代入に用いる)
        start2 = change1(start)
        start3 = utc_to_jst(start2)
        start4 = change2(start3)
        end4 = change2(end)
        dif4 = change2(dif)
        
        # 確認用
        print('id:'+str(message_creater.m[i]))
        print('経過時間(秒):'+str(dif.total_seconds()))
        
        spend_time(dif.total_seconds(), i)



# def start():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(periodic_execution, 'interval', seconds=10)
#     scheduler.start()