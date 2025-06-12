import json
import time

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, init, migrate, upgrade
from environs import Env
import os

env = Env()
env.read_env('.env')
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = env.str('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = env.bool('SQLALCHEMY_TRACK_MODIFICATIONS', False)

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate_obj = Migrate(app, db)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    json = db.Column(db.PickleType)

@app.template_filter('to_nice_json')
def to_nice_json(value):
    return json.dumps(value, indent=2)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        form_data = request.form.to_dict()
        new_entry = Form(json=form_data)
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('results'))

    return render_template("index.html")

@app.route("/results")
def results():
    data = Form.query.all()
    return render_template("results.html", data=data)

def apply_migrations():
    with app.app_context():
        time.sleep(5)  # Ждём подключения к БД
        migrations_folder = os.path.join(os.path.dirname(__file__), 'migrations')
        if os.path.exists(migrations_folder):
            print("Применяю миграции...")
            try:
                upgrade()
            except Exception as e:
                print(f"Ошибка применения миграции: {e}")
        else:
            print("Инициализирую миграции...")
            init()
            migrate()
            upgrade()

def create_app():
    # apply_migrations()
    return app

if __name__ == "__main__":
    create_app().run(debug=True)