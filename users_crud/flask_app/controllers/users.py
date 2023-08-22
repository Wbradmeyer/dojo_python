from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user

# Create Users Controller
@app.route('/users/create')
def display_user_form():
    return render_template('create.html')

@app.route('/users/create/account', methods=['POST'])
def create_user():
    if not user.User.validate_user(request.form):
        session['first_name'] = request.form['first_name']
        session['last_name'] = request.form['last_name']
        session['email'] = request.form['email']
        return redirect('/users/create')
    user_id = user.User.create_user(request.form)
    session.clear()
    return redirect('/')

# Read Users Controller

@app.route('/')
def all_users():
    list_of_users = user.User.get_all_users()
    return render_template('index.html', users = list_of_users)


@app.route('/users/<int:id>/show')
def show_user(id):
    user_data = user.User.get_user_by_id(id)
    return render_template('show_user.html', user = user_data)

# Update Users Controller
@app.route('/users/<int:id>/update', methods=['POST', 'GET'])
def update_user_by_id(id):
    if request.method == 'GET':
        user_to_update = user.User.get_user_by_id(id)
        return render_template('edit.html', user = user_to_update)
    else:
        check = user.User.update_user(request.form)
        return redirect(f'/users/{id}/show')


# Delete Users Controller
@app.route('/users/<int:id>/delete')
def delete_user_by_id(id):
    user_data = user.User.delete_user_by_id(id)
    return redirect('/')
