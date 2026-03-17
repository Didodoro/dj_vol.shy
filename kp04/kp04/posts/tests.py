from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

class HomepageTest(TestCase):

    text = "<h1> Домашня сторінка дошки оголошень</h1>"

    def test_url_exists_at_correct_location(self):
        responce = self.client.get("")
        self.assertEqual(responce.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home")) # звернення до сторінки за її псевдонімом
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html") # тестуємо  наявність шаблону сторінки
    
    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, HomepageTest.text) # перевіряємо наявність заголовку на сторінці
    
    def test_database_as_dict(self):
    # This returns a QuerySet of dictionaries
        data = Post.objects.values() 
        for row in data:
            print(row)