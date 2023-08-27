from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user
from flask_app.models import post


# Create Posts Controller
@app.route('/posts/create', methods=['POST'])
def create_post():
    data = {
        'content': request.form['content'],
        'user_id': session['user_id']
    }
    post.Post.create_new_post(data)
    return redirect('/users/profile')

# Read Posts Controller

# Update Posts Controller

# Delete Posts Controller
@app.route('/posts/<int:id>/delete')
def delete_post(id):
    post.Post.delete_post_by_id(id)
    return redirect('/users/profile')