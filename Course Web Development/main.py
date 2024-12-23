from wtforms import StringField, TextAreaField, SubmitField
from flask.templating import render_template
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for
from flask_wtf import FlaskForm
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'Ahmad Learns'
db = SQLAlchemy(app)


class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])

    submit = SubmitField('Create Event')


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    datePosted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Event('{self.title}', '{self.datePosted}')"


@app.route('/')
@app.route('/home')
def home():
    events = Event.query.all()
    return render_template('home.html', events=events)

@app.route('/event/<int:eventID>')
def eventDetails(eventID):
    event = Event.query.get_or_404(eventID)
    return render_template('eventDetails.html', event=event)

@app.route('/create', methods=['GET', 'POST'])
def createEvents():
    form = EventForm()
    if form.validate_on_submit():
        event = Event()
        event.title = form.title.data
        event.description = form.description.data

        db.session.add(event)
        db.session.commit()

        return redirect(url_for('home'))
    
    return render_template('createEvent.html', form=form)




if __name__ == '__main__':
  # Ensure that the database tables are created
#   with app.app_context():
#     db.create_all()
  # with app.app_context():
  app.run(host='0.0.0.0', port=5000, debug=True)