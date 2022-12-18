from django.db import models
from django.utils import timezone

import datetime

CATEGORY = (('study', '勉強'),(('programming', 'プログラミング')),('other', 'その他'))  

class Card(models.Model):
  created_at = models.DateTimeField('登録日時', auto_now_add=True)
  updated_at = models.DateTimeField('更新日時', auto_now=True)
  review = models.IntegerField('復習回数',default = 0)
  review_count = models.IntegerField('やり直し回数',default = 0)
  question = models.TextField('問題',default='問題')
  answer_fake1 = models.CharField('選択肢1',max_length=100,default='選択肢1')
  answer_fake2 = models.CharField('選択肢2',max_length=100,default='選択肢2')
  answer = models.CharField('回答',max_length=100,default='回答')
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  category = models.CharField( 
              max_length=100, 
              choices = CATEGORY 
  )
  def __str__(self):
    return self.question