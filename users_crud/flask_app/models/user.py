
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

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
        return int(user_id)

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

    @classmethod
    def get_user_by_id(cls, id):
        user_id = {'id' : id}
        query = """
        SELECT *
        FROM users 
        WHERE id = %(id)s
        ;"""
        result = connectToMySQL(cls.db).query_db(query, user_id)
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
        return cls(result[0])

    # Update Users Models
    @classmethod
    def update_user(cls, user_info):
        query = """
        UPDATE users
        SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
        WHERE id = %(id)s
        ;"""
        connectToMySQL(cls.db).query_db(query, user_info)
        return

    # Delete Users Models
    @classmethod
    def delete_user_by_id(cls, id):
        data = {'id' : id}
        query = """
        DELETE
        FROM users
        WHERE id = %(id)s
        ;"""
        connectToMySQL(cls.db).query_db(query, data)
        return 
    
    @staticmethod
    def validate_user(user):
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
        if user['email'] == User.get_user_by_email(user['email']).email:
            flash('Email already in use.')
            is_valid = False
        return is_valid