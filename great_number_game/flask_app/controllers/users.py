from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user
import random



@app.route('/')
def show_guess_page():
    if 'num' not in session:
        session['num'] = random.randint(1, 100)
        session['count'] = 5
        session['message'] = None
        session['correct'] = False
    return render_template('index.html')

@app.route('/game_over')
def clear_session():
    session.clear()
    return redirect('/')

@app.route('/guess', methods=['POST'])
def take_a_guess():
    if session['count'] == 0:
        return redirect('/')
    if session['num'] == int(request.form['num']):
        session['message'] = 'That was the number!'
        session['correct'] = True
        session['count'] = 0
        return redirect('/')
    elif session['num'] < int(request.form['num']):
        session['message'] = 'Too high.'
        session['count'] -= 1
    else:
        session['message'] = 'Too low.'
        session['count'] -= 1
    if session['count'] == 0:
        session['message'] = 'Game Over.'
    return redirect('/')
