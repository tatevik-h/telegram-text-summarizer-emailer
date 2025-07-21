user_emails = {}


def set_user_email(user_id: int, email: str):
    user_email[user_id] = email


def get_user_email(user_id: int) -> str:
    return user_emails.get(user_id)

