from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class APIKeyForm(FlaskForm):

	#email = StringField('Your Close.io Email', validators=[DataRequired(), Email()])
	api_key = StringField('Your Close.io API Key', validators=[DataRequired()])

	list_type = SelectField(
		'Choose a sample lead list:',
		choices=[
			('b2b', 'B2B (Your leads are businesses)'),
			('b2c', 'B2C (Your leads are people)')
		],
		validators=[DataRequired()]
	)

	submit = SubmitField('Import Leads')