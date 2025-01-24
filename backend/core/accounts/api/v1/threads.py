import random
from accounts.models import RecoveryCode
from accounts.api.v1.mails import send_password_reset_email


def generate_digits(user):
    attempts = 0
    max_attempts = 1000
    target_digits = random.randint(1000, 9999)

    while RecoveryCode.objects.filter(digits=target_digits).exists():
        attempts += 1
        if attempts >= max_attempts:
            target_digits = "-1"
            break
        target_digits = random.randint(1000, 9999)

    if target_digits != "-1":
        target_digits = str(target_digits)
        RecoveryCode.objects.create(digits=target_digits, user=user)

    send_password_reset_email(user.email, target_digits)
