from celery import shared_task

@shared_task
def my_celery_task():
    print("РАБОТАЕТ")