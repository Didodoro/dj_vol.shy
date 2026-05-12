from django.test import TestCase
from django.urls import reverse
from .models import Post
from django.utils import timezone
from datetime import date

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.text = 'New text'
        cls.date =  date.today()
        cls.date2 =  date.today()
        cls.temperature = 15.0
        cls.pressure = 750.0
        cls.wind_speed = 5.0
        cls.precipitation_prob = 20.0
        cls.post = Post.objects.create(
            text="Перше вимірювання",
            date= cls.date,
            temperature=12.0,
            pressure=747.0,
            wind_speed=3.5,
            precipitation_prob=10.0
        )

    def test_model_content(self):
        self.assertEqual(self.post.text, "Перше вимірювання")
        self.assertEqual(self.post.date, self.date)
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

    def test_post_deleteview(self):
        response = self.client.post(
            reverse('post_delete', args=['1'])
        )
        self.assertEqual(response.status_code, 302)

    def test_post_createview(self):
        date3 =  date.today()
        text = '1234567890'
        responce = self.client.post(
            reverse('post_new'),
            {
                'text': text,
                'date': date3,
                'temperature': self.temperature,
                'pressure': self.pressure,
                'wind_speed': self.wind_speed,
                'precipitation_prob': self.precipitation_prob,
            }
        )
        self.assertEqual(responce.status_code, 302)
        self.assertEqual(Post.objects.last().text,text)
        self.assertEqual(Post.objects.last().date,date3)
        self.assertEqual(Post.objects.last().temperature,self.temperature)
        self.assertEqual(Post.objects.last().pressure,self.pressure)
        self.assertEqual(Post.objects.last().wind_speed,self.wind_speed)
        self.assertEqual(Post.objects.last().precipitation_prob,self.precipitation_prob)
        