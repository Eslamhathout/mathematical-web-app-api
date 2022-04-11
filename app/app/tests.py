from django.test import TestCase


class CalcTests(TestCase):
    def test_add_numbers(self):
        '''Tests that two numbers are added'''
        self.assertEqual(3+3, 6)
