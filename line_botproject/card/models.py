from django.db import models
from django.utils import timezone

import datetime

class Card(models.Model):
  created_at = models.DateTimeField('登録日時', auto_now_add=True)
  updated_at = models.DateTimeField('更新日時', auto_now=True)
  review = models.IntegerField('復習回数,')
  review_count = models.IntegerField('やり直し回数')
  question = models.TextField('問題',default='問題')
  answer_fake1 = models.CharField('選択肢1',max_length=100,default='選択肢1')
  answer_fake2 = models.CharField('選択肢2',max_length=100,default='選択肢2')
  answer = models.CharField('回答',max_length=100,default='回答')
  def __str__(self):
    return self.question