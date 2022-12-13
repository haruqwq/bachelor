from django.urls import path
from . import views
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore,register_events,register_job
# from customer.customerUpdate import testfunc
from line_bot import notice_message

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

@register_job(scheduler, "interval", seconds = 300, id = 'test_job', replace_existing=True)
def test_job():
    print("test")
    notice_message.periodic_execution()
register_events(scheduler)
scheduler.start()

urlpatterns = [
    #path('line_bot/', views.ListCardView.as_view()),
    # path('card/', views.ListCardView.as_view()), 
    path('', views.index, name='callback')
    ]