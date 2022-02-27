from urllib import response
from django.test import SimpleTestCase

from django.urls import reverse

# Create your tests here.
# Built in Django testing

class PokemonTests(SimpleTestCase):

  def test_home_page_status_code(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_home_base_template(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'home.html')
    self.assertTemplateUsed(response, 'base.html')

  def test_about_page_status_code(self):
    url = reverse('about')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_about_page_template(self):
    url = reverse('about')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'about.html')
    self.assertTemplateUsed(response, 'base.html')

  def test_info_page_status_code(self):
    url = reverse('info')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_info_page_template(self):
    url = reverse('info')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'info.html')
    self.assertTemplateUsed(response, 'base.html')

