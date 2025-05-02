from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


class OpinionForm(FlaskForm):
    custom_id = StringField(
        'Вариант короткого идентификатора',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 128), Optional()]
    )
    original_link = URLField(
        'Оригинальная ссылка',
        validators=[Length(1, 256)]
    )
    submit = SubmitField('Добавить')
