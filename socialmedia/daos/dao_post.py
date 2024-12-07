from socialmedia.post import Post
from socialmedia.daos.dao_abstract import DAO

class PostsDAO(DAO):
    def __init__(self):
        super().__init__('posts.pkl')

    def adicionarPost(self, post: Post):
        if((post is not None) and isinstance(post, Post) and isinstance(post.id, str)):
            super().add(post.id, post)

    def updatePost(self, post: Post):
        if((post is not None) and isinstance(post, Post) and isinstance(post.id, str)):
            super().update(post.id, post)

    def getPost(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def removePostxs(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)