from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import recipe
import calendar

# Create Recipes Controller
@app.route('/recipes/new', methods=['POST', 'GET'])
def create_recipe():
    if 'user_id' not in session: return redirect('/')
    if request.method == 'POST':
        recipe_id = recipe.Recipe.create_new_recipe(request.form)
        if recipe_id:
            return redirect('/recipes')
    return render_template('create_recipe.html', data = request.form)


# Read Recipes Controller
@app.route('/recipes')
def show_recipes():
    if 'user_id' not in session: return redirect('/')
    all_recipes = recipe.Recipe.get_all_recipes_with_users()
    return render_template('recipes.html', recipes = all_recipes)

@app.route('/recipes/<int:id>')
def recipe_card(id):
    if 'user_id' not in session: return redirect('/')
    this_recipe = recipe.Recipe.get_recipe_by_id(id)
    month = calendar.month_name[this_recipe.date_cooked.month]
    return render_template('one_recipe.html', recipe = this_recipe, month = month)


# Update Recipes Controller
@app.route('/recipes/edit/<int:id>', methods=['POST', 'GET'])
def edit_recipe(id):
    if 'user_id' not in session: return redirect('/')
    if request.method == 'POST':
        updated = recipe.Recipe.update_recipe(request.form)
        if updated:
            return redirect('/recipes')
    recipe_to_update = recipe.Recipe.get_recipe_by_id(id)
    if recipe_to_update.user_id == session['user_id']:
        return render_template('edit_recipe.html', recipe = recipe_to_update)
    else:
        return redirect('/users/logout')


# Delete Recipes Controller
@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    if 'user_id' not in session: return redirect('/')
    if recipe.Recipe.delete_recipe_by_id(id):
        return redirect('/recipes')
    else:
        return redirect('/users/logout')