from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user # import entire file, rather than class, to avoid circular imports

# Create Users Controller



# Read Users Controller

@app.route('/', defaults = {'x': 8, 'y': 8, 'color1': 'red', 'color2': 'black'})
@app.route('/<int:x>', defaults = {'y': 8, 'color1': 'red', 'color2': 'black'})
@app.route('/<int:x>/<int:y>', defaults = {'color1': 'red', 'color2': 'black'})
@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def create_checkerboard(x, y, color1, color2):
    return render_template('index.html', x=x, y=y, color1=color1, color2=color2)


# Update Users Controller



# Delete Users Controller


# Notes:
# 1 - Use meaningful names
# 2 - Do not overwrite function names
# 3 - No matchy, no worky
# 4 - Use consistent naming conventions 
# 5 - Keep it clean
# 6 - Test every little line before progressing
# 7 - READ ERROR MESSAGES!!!!!!
# 8 - Error messages are found in the browser and terminal




# How to use path variables:
# @app.route('/<int:id>')
# def index(id):
#     user_info = user.User.get_user_by_id(id)
#     return render_template('index.html', user_info)

# Converter -	Description
# string -	Accepts any text without a slash (the default).
# int -	Accepts integers.
# float -	Like int but for floating point values.
# path 	-Like string but accepts slashes.