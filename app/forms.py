from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class APIKeyForm(FlaskForm):

	api_key = StringField('Your Close.io API Key', validators=[DataRequired()])
	submit = SubmitField('Import Leads')