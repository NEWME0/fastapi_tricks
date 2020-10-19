from graphene import ObjectType, Schema
from graphene_mongo import MongoengineConnectionField

from .nodes import *


class Query(ObjectType):
    node = Node.Field()
    all_authors = MongoengineConnectionField(Author)
    all_articles = MongoengineConnectionField(Article)
    all_comments = MongoengineConnectionField(Comment)


schema = Schema(query=Query, types=[Author, Article, Comment])
