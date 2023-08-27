from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import user


class Recipe:
    db = "recipes_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None


    #Create Recipes Models
    @classmethod
    def create_new_recipe(cls, data):
        if not cls.validate_recipe(data):
            return False
        query = """
        INSERT INTO recipes (name, description, instructions, date_cooked, under_30, user_id)
        VALUES (%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_30)s, %(user_id)s)
        ;"""
        recipe_id = connectToMySQL(cls.db).query_db(query, data)
        return recipe_id
    

    #Read Recipes Models
    @classmethod
    def get_recipe_by_id(cls, id):
        data = {'id': id}
        query = """
        SELECT * FROM recipes
        JOIN users ON recipes.user_id = users.id
        WHERE recipes.id = %(id)s
        ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        this_recipe = cls(result[0])
        this_recipe.creator = user.User(result[0])
        return this_recipe

    @classmethod
    def get_all_recipes_with_users(cls):
        query = """
        SELECT * FROM recipes
        JOIN users ON recipes.user_id = users.id
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        all_recipes = []
        if results:
            for row in results:
                this_recipe = cls(row)
                this_recipe.creator = user.User(row)
                all_recipes.append(this_recipe)
        return all_recipes

    # Update Recipes Models
    @classmethod
    def update_recipe(cls, data):
        if not cls.validate_recipe(data):
            return False
        query = """
        UPDATE recipes
        SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, 
                    date_cooked = %(date_cooked)s, under_30 = %(under_30)s
        WHERE id = %(id)s
        ;"""
        connectToMySQL(cls.db).query_db(query, data)
        return True

    # Delete Recipes Models
    @classmethod
    def delete_recipe_by_id(cls, id):
        data = {'id': id}
        this_recipe = cls.get_recipe_by_id(id)
        if session['user_id'] != this_recipe.user_id:
            return False
        query = """
        DELETE FROM recipes
        WHERE id = %(id)s
        ;"""
        connectToMySQL(cls.db).query_db(query, data)
        return True

    #Helper Recipes Methods
    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 2:
            flash('Name must be at least 3 characters.')
            is_valid = False
        if len(data['description']) < 2:
            flash('Description must be at least 3 characters.')
            is_valid = False
        if len(data['instructions']) < 2:
            flash('Please add instructions.')
            is_valid = False
        if data['date_cooked'] == '':
            flash('Please select the date cooked.')
            is_valid = False
        return is_valid