from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email

class MyForm(FlaskForm):
 Name = StringField('Name',validators=[DataRequired()])
 mail = StringField('Email',validators=[DataRequired()])
 subject = StringField('Subject',validators=[DataRequired()])
 messages = TextAreaField('Message',validators=[DataRequired()])