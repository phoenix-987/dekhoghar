from os import environ
from django.core.mail import EmailMessage


class SendMail:
    @staticmethod
    def send_email(user_name, user_email, reset_uri):
        email_subject = 'GharDekho: Link to Reset Password'
        email_body = (f'Hi {user_name},\nWe have received your request to reset the password. You can click on the '
                      f'link to reset your password: {reset_uri}')

        try:
            email = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email=environ.get('EMAIL_USER'),
                to=[user_email]
            )

            email.send()

            return {'message': 'Email sent', 'status': True}

        except Exception as e:
            return {'message': str(e), 'status': False}
