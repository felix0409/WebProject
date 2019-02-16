from mongoengine import Document, StringField, IntField

class Subscribers(Document):
    email = StringField()