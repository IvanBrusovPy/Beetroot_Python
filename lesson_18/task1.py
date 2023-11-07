import re


class Email:
    def __init__(self, email):
        if self.validate(email):
            self.email = email

    @staticmethod
    def validate(email):
        if isinstance(email, str):
            email_validate_pattern = (r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9]("
                                      r"?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
            if re.match(email_validate_pattern, email):
                return 1
        raise ValueError("Wrong email format")


email_1 = Email("abc@mail")


