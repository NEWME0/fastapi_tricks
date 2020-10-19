from graphene import Node
from graphene_mongo import MongoengineObjectType

from ..mongo import models


class Author(MongoengineObjectType):
    class Meta:
        model = models.Author
        interfaces = (Node,)


class Article(MongoengineObjectType):
    class Meta:
        model = models.Article
        interfaces = (Node,)


class Comment(MongoengineObjectType):
    class Meta:
        model = models.Comment
        interfaces = (Node,)
