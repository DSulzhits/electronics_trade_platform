import re
from django.core.exceptions import ValidationError


class PasswordValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('^[a-zA-Z0-9]+$')
        tmp_val = dict(value).get(self.field)
        if not bool(reg.match(tmp_val)):
            raise ValidationError('Пароль должен содержать только латинские буквы и цифры')
