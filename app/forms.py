from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class APIKeyForm(FlaskForm):

	email = StringField('Your Close.io Email', validators=[DataRequired(), Email()])
	api_key = StringField('Your Close.io API Key', validators=[DataRequired()])

	list_type = SelectField(
		'Which type of sample list do you want to import?',
		choices=[
			('b2b', 'B2B (You sell to companies)'),
			('b2c', 'B2C (You sell to individuals)')
		],
		validators=[DataRequired()]
	)

	submit = SubmitField('Import Leads')