from flask_app import app
from flask import render_template, redirect, request, session

# Create Users Controller
@app.route('/process', methods=['POST'])
def survey_entry():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['platform'] = request.form['platform']
    session['stack'] = request.form.getlist('stack')
    session['comment'] = request.form['comment']
    print(session['stack'])
    return redirect('/result')

# Read Users Controller

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/result')
def entry_display():
    return render_template('result.html')

