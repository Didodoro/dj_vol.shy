from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.

class HomepageTest(SimpleTestCase):

    def test_url_exists_at_correct_location(self):
        responce = self.client.get("/")
        self.assertEqual(responce.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home")) # звернення до сторінки за її псевдонімом
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html") # тестуємо  наявність шаблону сторінки
    
    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Початкова сторінка</h1>") # перевіряємо наявність заголовку на сторінці

class AboutpageTest(SimpleTestCase):

    def test_url_exists_at_correct_location(self):
        responce = self.client.get("/about/")
        self.assertEqual(responce.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("about")) # звернення до сторінки за її псевдонімом
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html") # тестуємо  наявність шаблону сторінки
    
    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>Сторірінка about</h1>") # перевіряємо наявність заголовку на сторінці