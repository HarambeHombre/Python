from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from sqlalchemy.orm import DeclarativeBase
from wtforms.fields.simple import SubmitField

app = Flask(__name__)

bootstrap = Bootstrap5(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.secret_key = 'thisisasecretkey'

class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)

db.init_app(app)

class CafeForm(FlaskForm):
    name = StringField('Cafe Name')
    map_url = StringField('Map URL')
    img_url = StringField('Image URL')
    location = StringField('Location')
    seats = StringField('Seats')
    coffee_price = StringField('Coffee Price')
    has_sockets = BooleanField('Extra sockets')
    has_toilet = BooleanField('Toilets')
    has_wifi = BooleanField('WiFi')
    can_take_calls = BooleanField('Take Calls')
    submit = SubmitField('Add')

@app.route('/')
def main():
    cafes = db.session.query(Cafe).all()

    return render_template('index.html', cafes=cafes)

@app.route('/delete/<int:id>')
def delete(id):
    result = db.get_or_404(Cafe, id)
    db.session.delete(result)
    db.session.commit()
    return redirect(url_for('main'))

@app.route('/add', methods=["GET", "POST"])
def add():
    form = CafeForm()
    if request.method == "POST":
        cafe_to_add = Cafe(
        name = form.name.data,
        map_url = form.map_url.data,
        img_url = form.img_url.data,
        location = form.location.data,
        seats = form.seats.data,
        coffee_price = form.coffee_price.data,
        has_sockets = form.has_sockets.data,
        has_toilet = form.has_toilet.data,
        has_wifi = form.has_wifi.data,
        can_take_calls = form.can_take_calls.data
        )
        db.session.add(cafe_to_add)
        db.session.commit()
        return redirect(url_for('main'))

    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)