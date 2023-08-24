from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import dojo
from flask_app.models import ninja

# Create Users Controller
@app.route('/ninjas', methods=['GET', 'POST'])
def add_ninja_form():
    if request.method == 'POST':
        new_ninja = ninja.Ninja.add_ninja(request.form)
        id = request.form['dojo_id']
        return redirect(f'/dojos/{id}')
    
    # if 'GET', show the form
    list_of_dojos = dojo.Dojo.get_all_dojos()
    return render_template('ninja.html', dojos=list_of_dojos)

# Read Users Controller
@app.route('/dojos', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dojo.Dojo.add_dojo(request.form)
        return redirect('/dojos')
    
    # if 'GET', get the list of dojos
    list_of_dojos = dojo.Dojo.get_all_dojos()
    return render_template('index.html', dojos=list_of_dojos)
    

@app.route('/dojos/<int:id>')
def display_ninjas_in_dojo(id):
    # get dojo by id for name
    dojo_name = dojo.Dojo.get_dojo_by_id(id)
    list_of_ninjas = dojo.Dojo.get_ninjas_in_dojo(id)
    return render_template('show_dojo.html', ninjas = list_of_ninjas, dojo = dojo_name)


# Update Controller
@app.route('/ninjas/<int:id>/update/<int:dojo_id>', methods=['GET', 'POST'])
def edit_ninja(id, dojo_id):
    if request.method == 'GET':
        ninja_data = ninja.Ninja.get_ninja_by_id(id)
        return render_template('edit.html', ninja = ninja_data)
    ninja.Ninja.update_ninja(request.form)
    return redirect(f'/dojos/{dojo_id}')


# Delete Controller
@app.route('/ninjas/<int:id>/delete/<int:dojo_id>')
def delete_ninja(id, dojo_id):
    ninja.Ninja.delete_ninja_by_id(id)
    return redirect(f'/dojos/{dojo_id}')