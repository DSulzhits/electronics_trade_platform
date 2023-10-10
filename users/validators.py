import re
from django.core.exceptions import ValidationError


class PasswordValidator:
    """Add password validation params
    (Добавлены параметры валидации для пароля)"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('^[a-zA-Z0-9]+$')
        tmp_val = dict(value).get(self.field)
        if not bool(reg.match(tmp_val)):
            raise ValidationError('Password must contain only english letters and numbers')
