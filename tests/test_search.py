############################

## commands to run before testing (setting up system)
## export DJANGO_SETTINGS_MODULE=hermes.settings
# pip3 install djangorestframework

## HOW TO RUN
## type the command below
## py.test
## for coverage report run
## py.test --cov=. --cov-report html


from api.search import Api
from django.test import TestCase

class test_search(TestCase):
    def setUp(self):
        self.api = Api()


    def test_upper(self):
        assert self.api.search("AAPL") != {}

    def test_lower(self):
        assert self.api.search("aapl") != {}

    def test_invalid(self):
        try:
            info = self.api.search("abcd")
        except Exception as e:
            assert str(e) == "The stock code you searched was invalid"
        else:
            assert 1 == 2
    