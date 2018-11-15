from django.test import TestCase
from .models import Location,Profile,Post,Comment
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.Moringa = Location(location='Moringa')

    def test_instance(self):
        self.assertTrue(isinstance(self.Moringa,Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_method(self):
        self.Moringa.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        self.Moringa.delete_location('Moringa')
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)

class CommentTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='donald',password='password123')
        self.comment = Comment(comment='Test Comment',username=self.new_user,post=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def tearDown(self):
        Comment.objects.all().delete()

    def test_save_method(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments)>0)

    # def test_delete_method(self):
    #     self.comment.delete_comment()
    #     comments = Comment.objects.all()
    #     self.assertTrue(len(comments)==0)
