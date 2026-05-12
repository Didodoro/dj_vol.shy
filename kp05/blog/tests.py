from django.test import TestCase
from django.urls import reverse
from .models import Post
from django.utils import timezone

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.title = 'New title'
        cls.body = 'Body content'
        cls.post = Post.objects.create(
            text="Перше вимірювання",
            date=timezone.now(),
            temperature=12.0,
            pressure=747.0,
            wind_speed=3.5,
            precipitation_prob=10.0
        )

    def test_model_content(self):
        self.assertEqual(self.post.text, "Перше вимірювання")
        self.assertEqual(self.post.temperature, 12.0)
        self.assertEqual(self.post.get_absolute_url(), f'/post/{self.post.pk}/')

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get(f"/post/{self.post.pk}/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Перше вимірювання")
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detailview(self):
        response = self.client.get(reverse('post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Перше вимірювання")
        self.assertTemplateUsed(response, 'post_detail.html')

    #def test_post_deleteview(self):
    #    response = self.client.post(
    #        reverse('post_delete', args=['1'])
    #    )
    #    self.assertEqual(response.status_code, 302)

    #def test_post_createview(self):
    #    responce = self.client.post(
    #        reverse('post_new'),
     #       {
      #          'title': self.title,
       #         'body': self.body,
        #    }
        #)
        #self.assertEqual(responce.status_code, 302)
        #self.assertEqual(Post.objects.last().title,self.title)
        #self.assertEqual(Post.objects.last().body,self.body)
       