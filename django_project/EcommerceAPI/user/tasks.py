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


@shared_task(bind=True)
def password_reset_task(self,detail):
    #Operations
    username = detail['username']
    email = detail['email']
    reset_url = detail['reset_url']
    mail_subject = 'Password Reset Request for Your Account.'
    message = f'''
Dear {username},

We have received a request to reset the password for your account. To initiate the password reset process, please click on the link below:

{reset_url}

Please note that this link is valid for a limited time and can only be used once. If you did not request this password reset, you can safely ignore this email. Your account security is important to us, so please do not share this link with anyone.

If you encounter any issues or need further assistance, please don't hesitate to contact our support team at [Support Email] or [Support Phone Number].

Thank you for your attention to this matter.

Best regards,
[Your Company Name] Support Team

'''
    send_mail(
        subject = mail_subject,
        message= message,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list= [email],
        fail_silently= True,
    )  
    return 'Password Reset Email Sent'