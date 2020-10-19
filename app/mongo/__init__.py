import random

from mongoengine import connect, disconnect

from .models import *


def fixture():
    tags = ['aot', 'fastapi', 'graphql', 'rest']

    authors = [
        Author(
            first_name=f'FN {i}',
            last_name=f'LN {i}',
        ).save() for i in range(10)
    ]
    comments = [
        Comment(
            comment=f'Nice article {i}',
            author=random.choice(authors),
        ).save() for i in range(20)
    ]
    articles = [
        Article(
            title=f'Article title {i}',
            content=f'Article content {i}',
            author=random.choice(authors),
            tags=random.sample(tags, 2),
            comments=random.sample(comments, 5),
        ).save() for i in range(5)
    ]


async def init_database():
    connect('fastapi_tricks', host='mongomock://localhost', alias='default')
    fixture()


async def finalize_database():
    disconnect(alias='default')
