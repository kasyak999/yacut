import re
from flask import jsonify, request, url_for

from . import app, db
from .models import URLMap
from .error_handlers import InvalidAPIUsage
from .views import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def post_add_url():
    data = request.get_json(silent=True)

    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')

    custom_id = data.get('custom_id')
    if custom_id:
        if URLMap.query.filter_by(short=custom_id).first() is not None:
            raise InvalidAPIUsage(
                'Предложенный вариант короткой ссылки уже существует.')

        if not re.fullmatch(r'^[A-Za-z0-9]+$', custom_id) \
                or len(custom_id) > 16:
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки')

    else:
        custom_id = get_unique_short_id()

    opinion = URLMap(
        original=data['url'], short=custom_id)
    db.session.add(opinion)
    db.session.commit()

    full_link = url_for('href_view', short_id=custom_id, _external=True)
    return jsonify({
        "url": data['url'],
        "short_link": full_link
    }), 201


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    result = URLMap.query.filter_by(short=short_id).first()
    if result is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({"url": result.original}), 200
