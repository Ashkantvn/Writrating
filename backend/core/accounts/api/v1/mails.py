from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import os




def send_password_reset_email(user_email, digits):
    subject = "Password Reset"
    from_email = "testemail@example.com"
    recipient_list = [user_email]


    if digits == "-1":
        message = "We are sorry, we could not generate a recovery code for you. Please try again later."
        email = EmailMultiAlternatives(subject, message, from_email, recipient_list)
        email.send(fail_silently=False)
    else:
        message = f"Use these digits to recover your password: {digits}"
        html_message = f"""
        <html>
            <body>
                <h1>{subject}</h1>
                <p>Use these digits to recover your password: <strong>{digits}</strong></p>
            </body>
        </html>
        """
        
        email = EmailMultiAlternatives(subject, message, from_email, recipient_list)
        
        # Add the HTML content as an alternative
        email.attach_alternative(html_message, "text/html")
        
        email.send(fail_silently=False)
