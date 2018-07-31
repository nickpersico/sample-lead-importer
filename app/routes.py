from flask import render_template, redirect, url_for, flash, request
from app import app
from app.forms import APIKeyForm
import time

# Close.io
from _closeio import run_import

@app.route('/', methods=['GET', 'POST'])
def index():

    form = APIKeyForm()

    return render_template('index.html', form=form)


@app.route('/importing-leads')
def ajax_index():

    form = APIKeyForm()

    closeio_import = run_import(
        api_key=form.api_key.data,
        list_type=form.list_type.data
    )

    flash('{}'.format(
            closeio_import
        )
    )

    return redirect(url_for('lead_import'))

# Lead Import View
@app.route('/lead-import')
def lead_import():
    return render_template('lead_import.html', title="Importing Leads into Close.io")