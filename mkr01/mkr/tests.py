from django.test import TestCase
from django.urls import reverse
from .models import Post
from django.utils import timezone

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(
            text="Перше вимірювання",
            data=timezone.now(),
            temperature=15.5,
            pressure=760.0,
            wind_speed=5.0,
            dosh=10.0
        )

    def test_model_content(self):
        self.assertEqual(self.post.text, "Перше вимірювання")
        self.assertEqual(self.post.temperature, 12.0)
        self.assertEqual(self.post.get_absolute_url(), ' ')

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Перше вимірювання")
        self.assertTemplateUsed(response, 'home.html')

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Перше вимірювання")
        self.assertContains(response, "15.5")
        self.assertContains(response, "760.0")
        self.assertContains(response, "5.0")
        self.assertContains(response, "10.0")

    def test_model_content(self):
        self.assertEqual(self.post.temperature, 15.5)
        self.assertEqual(self.post.pressure, 760.0)
        self.assertEqual(self.post.wind_speed, 5.0)
        self.assertEqual(self.post.dosh, 10.0)