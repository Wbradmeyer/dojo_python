
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
import re
from flask_bcrypt import Bcrypt
from datetime import date
bcrypt = Bcrypt(app)


class User:
    db = "log_and_reg_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        # self.age = 
        # self.ninja_turtle = data['ninja_turtle']
        # self.languages = data['']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


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
        session['user_name'] = f'{data["first_name"]} {data["last_name"]}'
        return user_id


    # Read Users Models
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

    @classmethod
    def get_all_users(cls):
        query = """
        SELECT * FROM users
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        all_users = []
        for entry in results:
            all_users.append(cls(entry))

    # Update Users Models

    # Delete Users Models

    # Helper methods
    @staticmethod
    def login_user(data):
        this_user = User.get_user_by_email(data['email'])
        if this_user:
            if bcrypt.check_password_hash(this_user.password, data['password']):
                session['user_id'] = this_user.id
                session['user_name'] = f'{this_user.first_name} {this_user.last_name}'
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
            # check password to see if all alpha characters are lowercase
        if user['password'].islower():
            flash('Password must contain one uppercase letter.')
            is_valid = False
            # loop through password and check for 'any' occurances of a 'digit'
        if not any(char.isdigit() for char in user['password']):
            flash('Password must contain a number.')
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash('Passwords do not match.')
            is_valid = False
        if (User.calculate_age(user['birthdate'])) < 10:
            flash('Must be at least 10 years old to register')
            is_valid = False
        if user['ninja_turtle'] == 'choose':
            flash('Please choose a favorite Ninja Turtle.')
            is_valid = False
        if ('language1' or 'language2' or 
                'language3' or 'language4' in user):
            flash('Please select at least one language learned.')
            is_valid = False
        return is_valid

    @staticmethod
    def calculate_age(birthdate):
        today = date.today()
        birth_date = birthdate.split('-')
        age = today.year - int(birth_date[0])
        if (today.month < int(birth_date[1])):
            age -= 1
        return age