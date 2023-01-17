from django.test import TestCase
from store.forms import RegistrationForm, ReviewForm


class TestRegistrationForm(TestCase):
    def test_registration_form_field_label(self):
        form = RegistrationForm()
        self.assertTrue(
            form.fields['name'].label is None or\
                form.fields['name'].label == 'name')

    def test_registation_form_with_incomplete_data(self):
        name = "Pita"
        email = "email@email.com"

        form = RegistrationForm(data={'name': name, 'email':email})
        self.assertFalse(form.is_valid())