from flask import render_template, jsonify
from . import app, db


# # Тут декорируется обработчик и указывается код нужной ошибки:
# @app.errorhandler(500)
# def internal_error(error):
#     # Ошибка 500 возникает в нештатных ситуациях на сервере. 
#     # Например, провалилась валидация данных.
#     # В таких случаях можно откатить изменения, не зафиксированные в БД,
#     # чтобы в базу не записалось ничего лишнего.
#     db.session.rollback()
#     # Пользователю вернётся страница, сгенерированная на основе шаблона 500.html.
#     # Этого шаблона пока нет, но сейчас мы его тоже создадим.
#     # Пользователь получит и код HTTP-ответа 500.
#     return render_template('500.html'), 500


# @app.errorhandler(404)
# def page_not_found(error):
#     # При ошибке 404 в качестве ответа вернётся страница, созданная
#     # на основе шаблона 404.html, и код HTTP-ответа 404:
#     return render_template('404.html'), 404


class InvalidAPIUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message = self.message)


# Обработчик кастомного исключения для API.
@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    # Возвращает в ответе текст ошибки и статус-код:
    return jsonify(error.to_dict()), error.status_code
