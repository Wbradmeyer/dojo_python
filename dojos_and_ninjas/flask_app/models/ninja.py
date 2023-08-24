
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session


class Ninja:
    db = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    # Create Ninja Models
    @classmethod
    def add_ninja(cls, data):
        query = """
        INSERT INTO ninjas (first_name, last_name, age, dojo_id)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)
    
    # Read Ninja Models
    @classmethod
    def get_ninja_by_id(cls, id):
        ninja_id = {'id' : id}
        query = """
        SELECT *
        FROM ninjas 
        WHERE id = %(id)s
        ;"""
        result = connectToMySQL(cls.db).query_db(query, ninja_id)
        return cls(result[0])

    # Update Ninja Models
    @classmethod
    def update_ninja(cls, ninja_info):
        query = """
        UPDATE ninjas
        SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s
        WHERE id = %(id)s
        ;"""
        connectToMySQL(cls.db).query_db(query, ninja_info)

    #Delete Ninja Models
    @classmethod
    def delete_ninja(cls, id):
        data = {'id' : id}
        query = """
        DELETE FROM ninjas
        WHERE id = %(id)s
        ;"""
        connectToMySQL(cls.db).query_db(query, data)
        return