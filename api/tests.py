from django.test import SimpleTestCase,Client,TestCase
from .views import *
from django.urls import reverse,resolve
from .models import *

class TestUrls(SimpleTestCase):
    def test_book_url_is_resolved(self):
        url = reverse('books')
        self.assertEqual(resolve(url).func,general_data)
    def test_add_url_is_resolved(self):
        url = reverse('add')
        self.assertEqual(resolve(url).func,book_api)
    def test_modify_url_is_resolved(self):
        url = reverse('modify',args=[1])
        self.assertEqual(resolve(url).func,book_api_patch)
        


class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
    def test_book_api_PATCH(self):
        tok = items.objects.create(
                name='Book1',
                isbn='633232',
                country='JAPAN',
                number_of_pages=50,
                publisher='test1',
                year = 2018,
                release_date='2018-01-10'
        )
        data = {
            "name":"Book123",
            "isbn":"633232",
            "country":"JAPAN",
            "number_of_pages":50,
            "publisher":"test1",
            "release_date":"2018-01-10"
        }
        response = self.client.patch('/api/v1/books/'+str(tok.id),data)
        self.assertEqual(response.status_code,200)
    def test_book_api_GET(self):
        response = self.client.get(reverse('add'))
        self.assertEqual(response.status_code,200)
    def test_book_api_POST(self):
        response = self.client.post('/api/v1/books',{
            'name':'Book1',
            'isbn':'633232',
            'country':'JAPAN',
            'number_of_pages':50,
            'publisher':'test1',
            'release_date':'2018-01-10'
        })
        self.assertEqual(response.status_code,200)
    def test_book_api_no_data_POST(self):
        response = self.client.post('/api/v1/books',{
        })
        self.assertEqual(response.status_code,404)
    def test_book_api_DELETE(self):
        items.objects.create(
                name='Book1',
                isbn='633232',
                country='JAPAN',
                number_of_pages=50,
                publisher='test1',
                year = 2018,
                release_date='2018-01-10'
        )
        response = self.client.delete('/api/v1/books/1',args=[1])
        self.assertEqual(response.status_code,200)
    def test_book_api_no_data_DELETE(self):
        response = self.client.delete('/api/v1/books/1',args=[1])
        self.assertEqual(response.status_code,404)
    def test_book_api_no_data_PATCH(self):
        response = self.client.patch('/api/v1/books/1',{
            'name':'Book123',
            'isbn':'633232',
            'country':'JAPAN',
            'number_of_pages':50,
            'publisher':'test1',
            'release_date':'2018-01-10'
        })
        self.assertEqual(response.status_code,404)
    def test_book_api_patch_GET(self):
        tok = items.objects.create(
                name='Book1',
                isbn='633232',
                country='JAPAN',
                number_of_pages=50,
                publisher='test1',
                year = 2018,
                release_date='2018-01-10'
        )
        response = self.client.get('/api/v1/books/'+str(tok.id))
        self.assertEqual(response.status_code,200)
    




    