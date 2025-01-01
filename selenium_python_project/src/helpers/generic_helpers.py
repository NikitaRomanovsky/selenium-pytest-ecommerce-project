import random
import string
import logging as logger


def generate_random_email(domain=None, email_prefix=None):
    if not domain:
        domain = "testdomain.com"
    if not email_prefix:
        email_prefix = "nikitatestuser"

    random_email_string_length = 10
    random_string = "".join(
        random.choices(string.ascii_lowercase, k=random_email_string_length)
    )

    email = f"{email_prefix}_{random_string}@{domain}"
    logger.info(f"Generated random email is {email}")

    return email


def generate_random_password():
    random_password_string_length = 10
    random_string = "".join(
        random.choices(string.ascii_letters, k=random_password_string_length)
    )

    password = f"TEST_{random_string}_12345"
    logger.info(f"Generated random password is {password}")

    return password
