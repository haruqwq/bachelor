from django.apps import AppConfig

class LineBotConfig(AppConfig):
  default_auto_field = 'django.db.models.BigAutoField'
  name = 'line_bot'

  # def ready(self):
  #   from .notice_message import start
  #   start()