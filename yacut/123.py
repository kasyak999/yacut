import random
import string

def get_unique_short_id(length=6, used_ids=None):
    """Генерирует короткий идентификатор заданной длины"""
    if used_ids is None:
        used_ids = set()
        
    chars = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    print(chars)
    random_chars = ''.join(random.choices(chars, k=length))
    print(random_chars)


    # while True:
    #     short_id = ''.join(random.choices(chars, k=length))
    #     if short_id not in used_ids:
    #         used_ids.add(short_id)
    #         return short_id

get_unique_short_id()