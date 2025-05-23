from celery import shared_task
from django.core.mail import send_mail
from kavenegar import KavenegarAPI, APIException, HTTPException
import os 
from decouple import config

KAVENEGAR_API_KEY = config("KAVENEGAR_API_KEY")
KAVENEGAR_SENDER = config("KAVENEGAR_SENDER")


@shared_task
def send_email_task(email , subject , message):
    send_mail(
        subject ,
        message ,
        'kelassor@gmail.com' ,
        [email] ,
        fail_silently= False
                )
    

@shared_task 
def send_sms_task(phone_number , message):
    try:
        api = KAVENEGAR_SENDER ,
        params = {
            'sender':KAVENEGAR_SENDER , 
            'recpetor' : phone_number ,
            'message': message

        }
        response = api.sms_send(params)
        return  response
    except APIException as e :
        print(f"SMS Error:{e}")
        return str(e)