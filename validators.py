def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    return False


def is_valid_password(password):
    if len(password) >= 6:
        return True
    return False


games = ["CS2", "PUBG", "Ready or not", "Roblox"]
for game in games:
    print(f" i wanna complate: {game}")