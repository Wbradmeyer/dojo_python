from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import user


class Post:
    db = "wall_post_schema"
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator = None

    # Create Post Models
    @classmethod
    def create_new_post(cls, post):
        if post['content'] == '':
            flash('Post content must not be blank.')
            return False
        query = """
        INSERT INTO posts (content, user_id)
        VALUES (%(content)s, %(user_id)s)
        ;"""
        post_id = connectToMySQL(cls.db).query_db(query, post)
        return post_id
    
    # Read Post Models
    @classmethod
    def get_all_posts_with_users(cls):
        query = """
        SELECT * from posts
        JOIN users ON posts.user_id = users.id
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        all_posts = []
        for row in results:
            one_post = cls(row)
            one_posts_creator = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            author = user.User(one_posts_creator)
            one_post.creator = author
            all_posts.insert(0, one_post)
        return all_posts
    
    # Delete Post Models
    @classmethod
    def delete_post_by_id(cls, id):
        post_id = {'id': id}
        query = """
        DELETE FROM posts
        WHERE id = %(id)s
        ;"""
        connectToMySQL(cls.db).query_db(query, post_id)
        return