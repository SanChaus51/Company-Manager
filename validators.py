def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    return False


def is_valid_password(password):
    if len(password) >= 6:
        return True
    return False
