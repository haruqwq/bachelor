from card.models import *
import json

from django.forms.models import model_to_dict

import datetime

import re

JST = datetime.timezone(datetime.timedelta(hours=9), "JST")

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

def isint(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True

message_list = ["全部の問題","全部の答え","学習中","学習済み"]

# カード数のカウント
all_card = Card.objects.all().count()

# データベースにあるidの判定
all = Card.objects.all().values("id")
all_str = str(all)
m = re.findall(r'\d+', all_str)

def last_check(message, reviews, answers):
    for i in range(0,all_card):
        if reviews[i] == 6 and answers[i] == message:
            return True

def study(message, answers):
    for i in range(0,all_card):
        if answers[i] == message:
            return True

def check_review_study(reviews):
    for i in range(0,all_card):
        print(reviews)
        if 0 <= reviews and reviews < 7:
            return True
        elif reviews == 7:
            return False

def create_single_text_message(message):

    reviews = []
    for i in range(0,all_card):
        post = Card.objects.get(id=m[i])
        # ディクショナリ型に変換
        post_dict = model_to_dict(post)
        # 辞書型からJSON型の文字列に変換
        json.dumps(post_dict)
        reviews.append(post_dict['review'])

    questions = []
    for i in range(0,all_card):
        post = Card.objects.get(id=m[i])
        # ディクショナリ型に変換
        post_dict = model_to_dict(post)
        # 辞書型からJSON型の文字列に変換
        json.dumps(post_dict)
        questions.append(post_dict['question'])

    answers = []
    for i in range(0,all_card):
        post = Card.objects.get(id=m[i])
        # ディクショナリ型に変換
        post_dict = model_to_dict(post)
        # 辞書型からJSON型の文字列に変換
        json.dumps(post_dict)
        answers.append(post_dict['answer'])
    
    if message == message_list[0]:
        message+=':'
        for i in range(0,all_card):
            message+='\n\n'+questions[i]
        test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
        return test_message

    elif message == message_list[1]:
        message+=':'
        for i in range(0,all_card):
            message+='\n\n'+answers[i]
        test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
        return test_message

    elif message == message_list[2]:
        message+=':'
        for i in range(0,all_card):
            if check_review_study(reviews[i]):
                message+='\n\n'+questions[i]
        test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
        return test_message

    elif message == message_list[3]:
        message+=':'
        for i in range(0,all_card):
            if not check_review_study(reviews[i]):
                message+='\n\n'+questions[i]
        test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
        return test_message

    elif isint(message)==True and message in m:
        message_int = int(message)

        # Modelオブジェクトを取得
        post = Card.objects.get(id=message)
        
        start = post.created_at  # 開始時刻を取得
        end = datetime.datetime.now(JST)  # 終了時刻を取得
        
        dif = end - start

        # 成形
        start2 = change1(start)
        start3 = utc_to_jst(start2)
        start4 = change2(start3)
        end4 = change2(end)
        dif4 = change2(dif)

        # ディクショナリ型に変換
        post_dict = model_to_dict(post)
        # 辞書型からJSON型の文字列に変換
        json.dumps(post_dict)

        t =str(post.created_at)
        x=change1(t)
        create_time=utc_to_jst(x)
        create_time=change2(create_time)

        test_message = [
                    {
                        'type': 'text',
                        'text': '問題:' + post_dict['question'] + '\n登録日時:' + create_time 
                    }
                ]
        return test_message

    elif study(message,answers) == True:
        for i in range(0,all_card):
            post = Card.objects.get(id=m[i])
            # ディクショナリ型に変換
            post_dict = model_to_dict(post)
            # 辞書型からJSON型の文字列に変換
            json.dumps(post_dict)
            if post.answer == message:
                message = '問題:' + post_dict['question'] + '\n解答:' + post_dict['answer']
                if post.review == 7:
                    message2 = '\n\n学習済みです'
                elif post.review == 6:
                    message2 = '\n\n学習完了!'
                    post.review=7
                    post.save()
                else:
                    message2 = '\n\n正解'
        test_message = [
                    {
                        'type': 'text',
                        'text': message + message2
                    }
                ]
        return test_message

    # elif study(message, answers) == True:
    #     for i in range(0,all_card):
    #         if answers [i]== message:
    #             message = '問題:' + questions[i] + '\n解答:' + answers[i]
    #     test_message = [
    #                 {
    #                     'type': 'text',
    #                     'text': message + '\n\n正解'
    #                 }
    #             ]
    #     return test_message

    else:
        message+="は期待されないメッセージです"+'\n\n'+"～以下から選択してください～"+'\n'
        message+=str(m)+"のいずれかの数字"
        for i in message_list:
            message+='\n'+i
        test_message = [
                    {
                        'type': 'text',
                        'text': message
                    }
                ]
        return test_message