from celery import shared_task
from django.core.mail import send_mail
from assignment import settings

@shared_task(bind=True)
def send_mail_func(self, instance):
    email = instance.email
    mail_subject = f"Form submitted"
    message = f"""Your form is submitted successfully.\n\nYour data is:\nId = {instance.id}\nName = {instance.name}\nDob = {instance.date_of_birth}\nEmail = {instance.email}\nPhone number = {instance.phone_number}\n\nThank you"""
    to_email = email
    send_mail(
        subject = mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=False,
    )