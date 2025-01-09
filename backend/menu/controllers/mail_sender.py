from django.core.mail import send_mail
from django.conf import settings

def send_email(subject, message, recipient_list):
    try:
        send_mail(
            subject,              
            message,              
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,       
            fail_silently=False
        )
        print("Письмо отправлено успешно!")
    except Exception as e:
        print(f"Ошибка при отправке письма: {str(e)}")