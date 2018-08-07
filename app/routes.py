from flask import render_template, redirect, url_for, flash, request
from app import app
from app.forms import APIKeyForm

# Close.io
from _closeio import run_import

@app.route('/', methods=['GET', 'POST'])
def index():
    form = APIKeyForm()
    if form.validate_on_submit():

        import_result = run_import(api_key=form.api_key.data, list_type=form.list_type.data)

        # Janky error handling
        if import_result == 'custom_field_error':
            flash('Please delete the Sample Custom Fields from your Close.io organization', 'error')

        if import_result == 'bad_api_key':
            flash('Your API key was invalid', 'error')

        if import_result == 'smartview_create_error':
            flash('There was an error creating your smartview', 'error')

        # Send the URL to the leads
        else:
            flash('{}'.format(import_result), 'success')

    return render_template('index.html',  title='Close.io Sample Lead Importer', form=form)
