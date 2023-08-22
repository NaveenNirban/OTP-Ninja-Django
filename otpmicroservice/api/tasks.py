from celery import shared_task
from django.core.mail import EmailMessage
from otpmicroservice.settings import EMAIL_HOST, EMAIL_HOST_USER
import logging
logging.basicConfig(level='DEBUG')


@shared_task()
def  send_mail_func(mail_body,toMail):
    #operations
    try:
        email = EmailMessage(
                    "OTP for into PocketHR",
                    mail_body,
                    EMAIL_HOST_USER,
                    [toMail],
                    [],                
        )
        email.send()
        return "Done"
    except Exception as e:
        logging.debug(e+" : send_mail_func()")
        return str(e)