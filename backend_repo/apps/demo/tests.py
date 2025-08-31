from django.test import TestCase
from rest_framework.test import APIClient
from apps.demo.models import Post, Comment
from django.contrib.auth.models import User
import random


def create_random_posts(num_posts):    
    #  students_list = []    
    for i in range(num_posts):
        student = Post.objects.create(text=f"post{random.randint(100, 1000)}", user=User.objects.filter().first()),


class StudentListTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        num_posts = 10
        self.posts_list = create_random_posts(num_posts)


