from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import OpinionForm
from .models import URLMap
from .api_views import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = OpinionForm()
    if form.validate_on_submit():
        short = form.custom_id.data if form.custom_id.data \
            else get_unique_short_id()

        if URLMap.query.filter_by(short=short).first() is not None:
            flash(
                'Предложенный вариант короткой ссылки уже существует.',
                'free-message')
            return render_template('index.html', form=form)

        opinion = URLMap(
            original=form.original_link.data,
            short=short,
        )
        db.session.add(opinion)
        db.session.commit()
        full_link = url_for('href_view', short_id=short, _external=True)
        flash(
            'Ваша новая ссылка готова: <br>'
            f'<a href="{full_link}" target="_blank">{full_link}</a>',
            'ok-message')
    return render_template('index.html', form=form)


@app.route('/<short_id>', methods=['GET'])
def href_view(short_id):
    return redirect(
        URLMap.query.filter_by(short=short_id).first_or_404().original
    )
