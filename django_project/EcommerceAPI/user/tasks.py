from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from EcommerceAPI import settings
import random

@shared_task(bind=True)
def email_verify_otp(self,user_data):
    #Operations
    user = user_data['user']
    email = user_data['email']
    otp = random.randint(100000,999999)
    mail_subject = 'Email Verification - Action Required'
    message = f"Dear {user},\nTo complete your email verification process, please use the following verification code: {otp}\nThank you,\nSuresh Lama"
    to_email = email
    send_mail(
        subject = mail_subject,
        message= message,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list= [to_email],
        fail_silently= True,
    )  
    return 'Done'