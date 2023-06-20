from django.test import TestCase
from django.urls import reverse

from .models import Book

# Create your tests here.


class BookTests(TestCase):
    @classmethod
    def setUpTestdata(self):
        self.book = Book.objects.create(
            title='peace',
            subtitle='Way to become Happiear',
            author='Vishant',
            isbn='8745612598756'
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, 'peace')
        self.assertEqual(self.book.subtitle, 'Way to become Happiear')
        self.assertEqual(self.book.author, 'Vishant')
        self.assertEqual(self.book.isbn, '8745612598756')

    def test_book_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Way to become Happiear")
        self.assertTemplateUsed(response, 'books/book_list.html')
