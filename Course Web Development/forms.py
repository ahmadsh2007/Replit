from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])

    submit = SubmitField('Create Event')