from flask import jsonify, request

from . import app, db
from .models import URLMap
# from .views import random_opinion
# from .error_handlers import InvalidAPIUsage

# /api/id/ — POST-запрос на создание новой короткой ссылки;
# /api/id/<short_id>/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.


@app.route('/api/id/', methods=['POST'])
def post_add_url():
    data = request.get_json(silent=True)

    return jsonify(data), 201