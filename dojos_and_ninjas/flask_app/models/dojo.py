
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import ninja


class Dojo:
    db = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    # Create Models
    @classmethod
    def add_dojo(cls, data):
        query = """
        INSERT INTO dojos (name)
        VALUES (%(name)s)
        ;"""
        connectToMySQL(cls.db).query_db(query, data)
        return


    # Read Models
    @classmethod
    def get_dojo_by_id(cls, id):
        data = {'id' : id}
        query = """
        SELECT * FROM dojos
        WHERE id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        return results[0]

    @classmethod
    def get_all_dojos(cls):
        query = """
        SELECT *
        FROM dojos
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        all_dojos = []
        for dojo in results:
            all_dojos.append(cls(dojo))
        return all_dojos
    
    @classmethod
    def get_ninjas_in_dojo(cls, id):
        data = {'id': id}
        query = """
        SELECT * FROM dojos
        LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id
        WHERE dojos.id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        dojo = cls( results[0] )
        for db_row in results:
            ninja_data = {
                'id' : db_row['ninjas.id'],
                'first_name' : db_row['first_name'],
                'last_name' : db_row['last_name'],
                'age' : db_row['age'],
                'created_at' : db_row['ninjas.created_at'],
                'updated_at' : db_row['ninjas.updated_at'],
                'dojo_id' : db_row['dojo_id']
            }
            dojo.ninjas.append( ninja.Ninja(ninja_data) )
        return dojo.ninjas

