from mongoengine import *


__all__ = ['Author', 'Comment', 'Article']


class Author(Document):
    meta = {'collection': 'author'}
    first_name = StringField(required=True)
    last_name = StringField(required=True)


class Comment(Document):
    meta = {'collection': 'comment'}
    comment = StringField(required=True)
    author = ReferenceField(Author, reverse_delete_rule=NULLIFY, null=True)


class Article(Document):
    meta = {'collection': 'article'}
    content = StringField(required=True)
    author = ReferenceField(Author, reverse_delete_rule=NULLIFY, null=True)
    title = StringField(required=True)
    tags = ListField(StringField())
    comments = ListField(ReferenceField(Comment))
