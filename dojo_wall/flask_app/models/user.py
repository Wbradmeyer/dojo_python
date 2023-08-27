
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import post
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


class User:
    db = "wall_post_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.posts = []


    # Create Users Models
    @classmethod
    def create_new_user(cls, data):
        if not cls.validate_user(data):
            return False
        data = data.copy()
        data['password'] = bcrypt.generate_password_hash(data['password'])
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
        ;"""
        user_id = connectToMySQL(cls.db).query_db(query, data)
        session['user_id'] = user_id
        session['first_name'] = f'{data["first_name"]}'
        return user_id


    # Read User Models
    @classmethod
    def get_user_by_id(cls, id):
        data = {'id': id}
        query = """
        SELECT * FROM users
        WHERE id = %(id)s
        ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_user_by_email(cls, email):
        user_data = {'email' : email}
        query = """
        SELECT *
        FROM users 
        WHERE email = %(email)s
        ;"""
        result = connectToMySQL(cls.db).query_db(query, user_data)
        if result:
            return cls(result[0])
        return False


    # Update User Models

    # Delete User Models

    # Helper Methods
    @staticmethod
    def login_user(data):
        this_user = User.get_user_by_email(data['email'])
        if this_user:
            if bcrypt.check_password_hash(this_user.password, data['password']):
                session['user_id'] = this_user.id
                session['first_name'] = f'{this_user.first_name}'
                return True
        flash('The email or password entered does not match our records.')
        return False

    @staticmethod
    def validate_user(user):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if len(user['first_name']) < 2:
            flash('First name must be at least 2 characters.')
            is_valid = False
        if len(user['last_name']) < 2:
            flash('Last name must be at least 2 characters.')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Not a valid email address!')
            is_valid = False
        if User.get_user_by_email(user['email']):
            flash('Email already in use.')
            is_valid = False
        if len(user['password']) < 8:
            flash('Password must be at least 8 characters.')
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash('Passwords do not match.')
            is_valid = False
        return is_valid