""" Test the store view"""

from django.test import TestCase
from store.models import Category, Writer, Book
from datetime import datetime


class TestCategory(TestCase):
    """test the Category class"""
    @classmethod
    def setUpTestData(cls) -> None:
        Category.objects.create(name="Motivation")

    def test_name_label(self):
        Category.objects.get(id=1)

        cat = Category.objects.get(id=1)
        field_label = cat._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_object_name_is_name(self):
        cat = Category.objects.get(id=1)
        expected_object_name = cat.name
        self.assertEqual(str(cat), expected_object_name)

    def test_name_max_length(self):
        cat = Category.objects.get(id=1)
        max_length = cat._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_created_at_data_type(self):
        cat = Category.objects.get(id=1)
        created_object_type = cat._meta.get_field('create_at')
        self.assertTrue(type(created_object_type), datetime)

    def test_updated_at_data_type(self):
        cat = Category.objects.get(id=1)
        updated_object_type = cat._meta.get_field('updated_at')
        self.assertTrue(type(updated_object_type), datetime)


class TestWriter(TestCase):
    """test the Writer class"""
    @classmethod
    def setUpTestData(cls) -> None:
        Writer.objects.create(name="Siatwambo", bio="Author of exams made easy")

    def test_name_label(self):
        Writer.objects.get(id=1)

        author = Writer.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_object_name_is_name(self):
        author = Writer.objects.get(id=1)
        expected_object_name = author.name
        self.assertEqual(str(author), expected_object_name)

    def test_writer_name_is_siatwambo(self):
        author = Writer.objects.get(id=1)
        self.assertEqual(str(author), "Siatwambo")

    def test_writer_bio(self):
        author = Writer.objects.get(id=1)
        expected_bio_text = author.bio
        self.assertEqual(str(author), expected_bio_text)

    def test_writer_bio(self):
        author = Writer.objects.get(id=1)
        self.assertEqual(str(author.bio), "Author of exams made easy")

    def test_name_max_length(self):
        author = Writer.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_created_at_data_type(self):
        author = Writer.objects.get(id=1)
        created_object_type = author._meta.get_field('create_at')
        self.assertTrue(type(created_object_type), datetime)

    def test_updated_at_data_type(self):
        author = Writer.objects.get(id=1)
        updated_object_type = author._meta.get_field('updated_at')
        self.assertTrue(type(updated_object_type), datetime)


class TestBook(TestCase):
    """ Test the Book class"""
    @classmethod
    def setUpTestData(cls) -> None:
        categ = Category.objects.create(name="Education")
        writer = Writer.objects.create(name="R Siatwambo")
        Book.objects.create(
            writer= writer,
            category=categ,
            name="Exams made easy",
            price=100,
            stock=1000,
            description="Help you in preparing for exams"
            )
    
    #Test field labels
    def test_object_writer_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('writer').verbose_name
        self.assertEqual(field_label, 'writer')

    def test_object_category_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_object_name_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        author = Book.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_object_price_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_object_stock_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('stock').verbose_name
        self.assertEqual(field_label, 'stock')

    def test_object_description_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    #Test object data
    def test_object_writer(self):
        book = Book.objects.get(id=1)
        expected_book_writer = book.writer
        self.assertEqual(str(expected_book_writer), "R Siatwambo")

    def test_object_category(self):
        book = Book.objects.get(id=1)
        expected_book_category = book.category
        self.assertEqual(str(expected_book_category), "Education")

    def test_object_name(self):
        book = Book.objects.get(id=1)
        expected_book_name = book.name
        self.assertEqual(str(book), expected_book_name)

    def test_object_price_is_price(self):
        book = Book.objects.get(id=1)
        expected_book_price = book.price
        self.assertEqual(expected_book_price, 100)

    def test_object_stock_is_stock(self):
        book = Book.objects.get(id=1)
        expected_books_in_stock = book.stock
        self.assertEqual(expected_books_in_stock, 1000)

    def test_object_description(self):
        book = Book.objects.get(id=1)
        expected_book_description = book.description
        self.assertEqual(
            expected_book_description, "Help you in preparing for exams")

    def test_object_default_values(self):
        book = Book.objects.get(id=1)
        expected_default_total_review = book.totalreview
        expected_default_total_rating = book.totalrating
        expected_default_status = book.status

        self.assertEqual(expected_default_total_review, 1)
        self.assertEqual(expected_default_total_rating, 5)
        self.assertEqual(expected_default_status, 0)
