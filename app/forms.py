from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class APIKeyForm(FlaskForm):

	api_key = StringField('Enter your Close.io API Key:', validators=[DataRequired()])
	list_type = SelectField(
		'Choose a lead list type:',
		choices=[
			('B2B', 'B2B (You sell to companies)'),
			('B2C', 'B2C (You sell to individuals)')
		],
		validators=[DataRequired()]
	)
	submit = SubmitField('Import Leads')