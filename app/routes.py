from flask import render_template, redirect, url_for, flash, request
from app import app
from app.forms import APIKeyForm

# Close.io
from _closeio import run_import

@app.route('/', methods=['GET', 'POST'])
def index():

	form = APIKeyForm()

	if form.validate_on_submit():

		closeio_import = run_import(
			email=form.email.data,
			api_key=form.api_key.data,
			list_type=form.list_type.data
		)

		flash('email={}, api_key={}, list_type={}, new_lead_id_created:{}'.format(
				form.email.data,
		    	form.api_key.data,
		    	form.list_type.data,
		    	closeio_import
		    )
		)

		return redirect(url_for('lead_import'))

	return render_template('index.html', title="Index page", form=form)

# Lead Import View
@app.route('/lead-import')
def lead_import():
	return render_template('lead_import.html', title="Importing Sample Leads into Close.io")