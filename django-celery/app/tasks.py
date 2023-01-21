from django.core.mail import EmailMessage

from celery import shared_task
from celery.utils.log import get_task_logger

# from core.env import get_env_variable


logger = get_task_logger("core")


@shared_task
def send_email():
    logger.info("Executing periodic task")

    email_to = "fhuseynov803@gmail.com"

    EmailMessage(
        subject="Test email", body="This is a test email", to=(email_to,)
    ).send(fail_silently=False)

    logger.info("Email is sent")



@shared_task
def test_task():
    print("Hello My Friend")


@shared_task
def test_warehouse():
    print("For warehouse")