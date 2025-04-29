from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/')
def root():
    return {"message": "Welcome to the Blog API!"}

@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from list'}
    else:
        return {'data': f'{limit} blogs from list'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id: int):
    return {'data': f'comments for blog {id}'}

@app.post('/blog')
def create_blog():
    return {'data': 'blog is created'}
