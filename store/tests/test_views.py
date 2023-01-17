from django.test import TestCase, Client

from store.models import Writer, Category, Book, Slider
from django.urls import reverse

# Create your tests here.

class TestStore(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        categ = Category.objects.create(name="Education", icon="book.ico")
        writer = Writer.objects.create(name="R Siatwambo", pic="img.png")
        slider = Slider.objects.create(
            title="Exams made easy1",
            slideimg="book")
        Book.objects.create(
            writer= writer,
            category=categ,
            name="Exams made easy",
            coverpage="cover.png",
            bookpage="bookpage.png",
            price=100,
            stock=1000,
            description="Help you in preparing for exams"
            )

    # Test if view urls are accessible at the desired locations
    def test_index_view_url_at_desired_location(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_registration_view_url_desired_location(self):
        c = Client()
        response = c.get('/registration')
        self.assertEqual(response.status_code, 200)

    def test_login_view_url_at_desired_location(self):
        c = Client()
        response = c.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_get_books_view_url_at_desired_location(self):
        c = Client()
        response = c.get('/books')
        self.assertEqual(response.status_code, 200)

    def test_get_book_by_id_view_url_at_desired_location(self):
        c = Client()
        response = c.get('/book/1')
        self.assertEqual(response.status_code, 200)

    def test_get_writer_by_id_view_url_at_desired_location(self):
        c = Client()
        response = c.get('/writer/1')
        self.assertEqual(response.status_code, 200)

    def test_get_category_by_id_view_url_at_desired_location(self):
        c = Client()
        response = c.get('/category/1')
        self.assertEqual(response.status_code, 200)

    #Test if view urls are accessible by names
    def test_index_view_url_accessible_by_name(self):
        c = Client()
        response = c.get(reverse('store:index'))
        self.assertEqual(response.status_code, 200)

    def test_registration_view_url_accessible_by_name(self):
        c = Client()
        response = c.get(reverse('store:registration'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_url_accessible_by_name(self):
        c = Client()
        response = c.get(reverse('store:signin'))
        self.assertEqual(response.status_code, 200)

    def test_get_books_view_url_accessible_by_name(self):
        c = Client()
        response = c.get(reverse('store:books'))
        self.assertEqual(response.status_code, 200)

    def test_get_book_by_id_view_url_accessible_by_name(self):
        c = Client()
        response = c.get(reverse('store:book', kwargs={'id':1}))
        self.assertEqual(response.status_code, 200)

    def test_get_writer_by_id_view_url_accessible_by_name(self):
        c = Client()
        response = c.get(reverse('store:writer', kwargs={'id':1}))
        self.assertEqual(response.status_code, 200)

    def test_get_category_by_id_view_url_accessible_by_name(self):
        c = Client()
        response = c.get(reverse('store:category', kwargs={'id':1}))
        self.assertEqual(response.status_code, 200)

    # Test views use correct template
    def test_index_view_uses_correct_template(self):
        c = Client()
        response = c.get(reverse('store:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/index.html')

    def test_registration_view_uses_correct_template(self):
        c = Client()
        response = c.get(reverse('store:registration'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/signup.html')

    def test_login_view_uses_correct_template(self):
        c = Client()
        response = c.get(reverse('store:signin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/login.html')

    def test_get_books_view_uses_correct_template(self):
        c = Client()
        response = c.get(reverse('store:books'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/category.html')

    def test_get_book_by_id_view_uses_correct_template(self):
        c = Client()
        response = c.get(reverse('store:book', kwargs={'id':1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/book.html')

    def test_get_writer_by_id_view_uses_correct_template(self):
        c = Client()
        response = c.get(reverse('store:writer', kwargs={'id':1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/writer.html')

    def test_get_category_by_id_view_uses_correct_template(self):
        c = Client()
        response = c.get(reverse('store:category', kwargs={'id':1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/category.html')


    # test pagination
    # def test_get_book_pagination_is_four(self):
    #     c = Client()
    #     response = c.get(reverse('store:book', kwargs={'id':1}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'] == True)
    #     self.assertEqual(len(response.context['r_review']), 5)


    # def test_get_books_pagination_is_ten(self):
    #     c = Client()
    #     response = c.get(reverse('store:books'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'] == True)
    #     self.assertEqual(len(response.context['books_']), 10)

    # def test_get_category_by_id_pagination_is_ten(self):
    #     c = Client()
    #     response = c.get(reverse('store:category', kwargs={'id':1}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'] == True)
    #     self.assertEqual(len(response.context['book_']), 10)