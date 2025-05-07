import random
import string
from .models import URLMap


LEN_SHORT_URL = 6


def get_unique_short_id():
    """Генерирует короткий идентификатор заданной длины"""
    chars = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    while True:
        new_id = ''.join(random.choices(chars, k=LEN_SHORT_URL))
        if URLMap.query.filter_by(short=new_id).first() is None:
            return new_id