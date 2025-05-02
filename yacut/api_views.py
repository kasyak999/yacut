import random
import string

from flask import jsonify, request

from . import app, db
from .models import URLMap
from .error_handlers import InvalidAPIUsage

# from .views import random_opinion
# from .error_handlers import InvalidAPIUsage


# /api/id/<short_id>/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

LEN_SHORT_URL = 6


def get_unique_short_id():
    """Генерирует короткий идентификатор заданной длины"""
    chars = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    return ''.join(random.choices(chars, k=LEN_SHORT_URL))


@app.route('/api/id/', methods=['POST'])
def post_add_url():
    data = request.get_json(silent=True)

    if data is None or 'url' not in data:
        raise InvalidAPIUsage('url не указан')
    if URLMap.query.filter_by(original=data['url']).first() is not None:
        raise InvalidAPIUsage('Такое url уже есть в базе данных')
    if data.get('custom_id') and (
        URLMap.query.filter_by(short=data.get('custom_id')).first() is not None
    ):
        raise InvalidAPIUsage('Такое custom_id уже есть в базе данных')

    short = data.get('custom_id') if data.get('custom_id') \
        else get_unique_short_id()

    opinion = URLMap(
        original=data['url'], short=short)
    db.session.add(opinion)
    db.session.commit()

    return jsonify(opinion.to_dict()), 201
