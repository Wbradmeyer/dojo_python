from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user



@app.route('/')
def show_counter():

    if 'num' not in session:
        session['num'] = 1
    else:
        session['num'] += 1

    if 'visit' not in session:
        session['visit'] = 1
    else:
        session['visit'] += 1

    return render_template('index.html')

@app.route('/destroy_session')
def clear_session():
    session.clear()
    return redirect('/')

@app.route('/reset')
def reset_counter():
    session.pop('num')
    return redirect('/')

@app.route('/add_two')
def add_two():
    session['num'] += 1
    return redirect('/')

@app.route('/choose_count', methods=['POST'])
def user_add():
    session['num'] += (int(request.form['user_count']) - 1)
    return redirect('/')
