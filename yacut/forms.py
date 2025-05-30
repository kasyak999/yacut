from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp


PATTERN = r'^[A-Za-z0-9]+$'


class OpinionForm(FlaskForm):
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16),
            Optional(),
            Regexp(
                PATTERN,
                message='Можно использовать только латинские буквы и цифры')
        ]
    )
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 256)
        ]
    )
    submit = SubmitField('Создать')
