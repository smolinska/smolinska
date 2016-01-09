import json
import os
from unittest.mock import patch, mock_open

from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy
from photologue.models import Gallery
from with_asserts.case import AssertHTMLMixin

from apps.main.extra_logic import obfuscate_emails, deobfuscate_emails, parse_SCSS_variables
from apps.main.models import MenuItem


class ScssVarieblesTests(TestCase):
    def test(self):
        file = """
        $x:5;
          $y  :  5px;
        """
        with patch("builtins.open", mock_open(read_data=file)) as mocked_open:
            scss_vars = parse_SCSS_variables()
            path_to_vars = mocked_open.call_args[0][0]
            self.assertTrue(os.path.exists(path_to_vars), "\n{} can't be found,\n check path in {}.{}".format(
                path_to_vars, parse_SCSS_variables.__module__, parse_SCSS_variables.__name__))
            self.assertEquals(scss_vars, {'x': 5, 'y': 5})


class EmailObfuscationTests(TestCase):
    def test_ob(self):
        email = '<a href="mailto:biuro@merari.pl">biuro@merari.pl</a>'
        ob = obfuscate_emails(email)
        self.assertEquals(ob, '<span class="js-hidden-eml" data-user="oruib" data-website="lp.irarem"></span>')

    def test_identity(self):
        email = '<a href="mailto:biuro@merari.pl">biuro@merari.pl</a>'
        two = deobfuscate_emails(obfuscate_emails(email))
        self.assertEquals(email, two)


class MainViewTests(TestCase):
    def test_context(self):
        '''tab_types should contain choices for MenuItem.type'''
        response = self.client.get(reverse('main'))
        js_vars = response.context['js_vars']
        self.assertIn('GALLERY', json.loads(js_vars['TAB_TYPES']))
        self.assertEquals(len(json.loads(js_vars['TAB_URLS'])), len(MenuItem.TYPES) - 1,
                          'missing something in TAB_URLS')


class GalleryViewTests(TestCase, AssertHTMLMixin):
    def do_test(self, count, clas):
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')
        with self.assertHTML(response, 'div.gallery-item.' + clas) as elements:
            self.assertEqual(len(elements), count)

    def test_Galleries(self):
        """There should be `in_row` galleries in row, so we check row count"""
        expected_class = {
            1: 'col-md-12',
            2: 'col-md-6',
            3: 'col-md-4',
        }

        for count in range(1, 4):
            try:
                for i in range(count):
                    mommy.make(Gallery)
                self.do_test(count, expected_class[count])
                Gallery.objects.all().delete()
            except AssertionError:
                print('Test fail with {} galleries in base'.format(count))
                raise
