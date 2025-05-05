from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from feed.models import Post
from django.core.files.uploadedfile import SimpleUploadedFile


#Test for views.py
class TestFeedPostCreateView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.test_image = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')

    #Test case for creating a post
    def test_create_post(self):
        data = {
            'sandwich': 'Test Sandwich',
            'about': 'Delicious test sandwich',
            'vegan': 'Vegan',
            'size': '6-inch',
            'bread': 'White Italian',
            'meat': 'Turkey',
            'cheese': 'Cheddar',
            'sauce_1': 'Mayonnaise',
            'sauce_2': 'Mustard',
            'sauce_3': 'Honey Mustard',
            'veggie_1': 'Lettuce',
            'veggie_2': 'Tomato',
            'veggie_3': 'Onion',
            'temp': 'Hot',
            'price': 5.00,
        }
        files = {'sandwich_image': self.test_image}

        response = self.client.post(reverse('post-create'), data=data, files=files)

        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEqual(post.sandwich, 'Test Sandwich')
        self.assertEqual(post.author, self.user)
        self.assertEqual(response.status_code, 302)  
