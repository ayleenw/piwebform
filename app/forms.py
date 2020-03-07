from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class printNoteForm(FlaskForm):
    note = TextAreaField('Gib hier Deinen Text zum Ausdrucken ein:', validators=[DataRequired(message="Das Feld darf nicht leer sein.")])
    submit = SubmitField('Ausdrucken')