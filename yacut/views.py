from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import OpinionForm
from .models import URLMap
from .api_views import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = OpinionForm()
    # return render_template('index.html')
    if form.validate_on_submit():
        short = form.custom_id.data if form.custom_id.data \
            else get_unique_short_id()
 
        if URLMap.query.filter_by(short=short).first() is not None:
            flash('Такая короткая ссылка уже используется!', 'free-message')
            return render_template('index.html', form=form)

        # opinion = URLMap(
        #     title=form.title.data,
        #     text=form.text.data,
        #     source=form.source.data
        # )
    #     # Затем добавить его в сессию работы с базой данных:
    #     db.session.add(opinion)
    #     # И зафиксировать изменения:
    #     db.session.commit()
    #     # Затем переадресовать пользователя на страницу добавленного мнения:
    #     return redirect(url_for('opinion_view', id=opinion.id))
    # # Если валидация не пройдена — просто отрисовать страницу с формой:
    return render_template('index.html', form=form)


@app.route('/<short_id>/', methods=['GET'])
def href_view(short_id):
    result = URLMap.query.filter_by(short=short_id).first()
    if result is None:
        abort(404)
    return redirect(result.original)
