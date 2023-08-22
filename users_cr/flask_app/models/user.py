
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt


class User:
    db = "users_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # Create Users Models
    @classmethod
    def create_user(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s)
        ;"""
        user_id = connectToMySQL(cls.db).query_db(query, data)
        return user_id 

    # Read Users Models
    @classmethod
    def get_all_users(cls):
        query = """
        SELECT *
        FROM users
        ;"""
        
        results = connectToMySQL(cls.db).query_db(query)
        all_users = []
        for user in results:
            all_users.append(cls(user))
        return all_users


    # Update Users Models



    # Delete Users Models