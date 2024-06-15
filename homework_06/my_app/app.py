"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""

from flask import (
    Flask,
    render_template,
)

from flask_migrate import Migrate

from my_app.models import db

from my_app.views.about.about import app_about
from my_app.views.products import products_app


app = Flask(
    __name__,
    template_folder="templates",
)

app.config.update(
    SECRET_KEY="616b2180ee260174500b1042c648dff4fe3476137dd0c7b32792a9f8efb1c3b5",
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://user:example@localhost:5432/blog",
    SQLALCHEMY_ECHO=True,
)

app.register_blueprint(app_about)
app.register_blueprint(products_app)

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/", endpoint="index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
