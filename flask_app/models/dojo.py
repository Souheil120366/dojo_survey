from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__( self , data ):
        self.id= data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # we assume this is true
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['location']) < 1:
            flash("You have to input location.")
            is_valid = False 
        if len(dojo['language']) < 1:
            flash("You have to input language.")
            is_valid = False   
        
        return is_valid    

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
  
        return dojos
    
    @classmethod
    def get_one(cls):
        query = "SELECT * FROM dojos ORDER BY ID DESC LIMIT 1"
        result = connectToMySQL('dojo_survey_schema').query_db(query)
       
        return cls(result[0])
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name, location,language,comment, created_at, updated_at ) VALUES ( %(name)s ,%(location)s, %(language)s, %(comment)s, NOW() , NOW() );"
        return connectToMySQL('dojo_survey_schema').query_db( query, data )        
