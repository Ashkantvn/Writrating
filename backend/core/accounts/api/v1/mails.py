from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def send_password_reset_email(user_email, digits):
    subject = "Password Reset"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    if digits == "-1":
        # Send plain text message
        message = "We are sorry, we could not generate a recovery code for you. Please try again later."
        email = EmailMultiAlternatives(subject, message, from_email, recipient_list)
        email.send(fail_silently=False)
    else:
        # HTML message
        html_message = f"""
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Writrating</title>
            </head>
            <body>
                <h1>{subject}</h1>
                <p>Use these digits to recover your password: <strong>{digits}</strong></p>
            </body>
        </html>
        """
        
        # Plain text message
        message = f"Use these digits to recover your password: {digits}"
        
        email = EmailMultiAlternatives(subject, message, from_email, recipient_list)
        
        # Add the HTML content as an alternative
        email.attach_alternative(html_message, "text/html")
        
        email.send(fail_silently=False)