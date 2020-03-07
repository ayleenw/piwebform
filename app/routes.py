from flask import render_template, redirect, flash, request
from app import app
from app.forms import printNoteForm
import time

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = printNoteForm()
    if form.validate_on_submit():
        flash('Diese Notiz wurde an den Drucker gesendet:')
        # return redirect('/index')
        notetext = request.form['note']
        # return redirect('/index')
        return render_template('success.html', title='Drucken', notetext=notetext)

    return render_template('index.html', title='Home', form=form)

@app.route('/success')
def success():
    time.sleep(3)
    return redirect('/index')


