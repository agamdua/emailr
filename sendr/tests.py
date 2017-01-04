import unittest

from django.conf import settings
from django.test.utils import override_settings  # noqa
from rest_framework.test import APIClient, APITestCase as TestCase

from .views import _get_recipients


class TestSendMail(TestCase):
    def setUp(self):
        self.client = APIClient()

    # I am being lazy and leaving this in here in case I ever need to make an
    # actual test run:
    #
    # @override_settings(EMAIL_BACKEND="anymail.backends.mailgun.MailgunBackend")
    def test_upload_image(self):
        with open(settings.BASE_DIR + "/test_data/mrrobot.jpg", 'rb') as fp:
            response = self.client.post(
                "/",
                {'image': fp},
                format='multipart',
                HTTP_CONTENT_DISPOSITION="attachment; filename=upload.jpg",
            )
        self.assertEqual(response.status_code, 200)


class TestUtils(unittest.TestCase):
    def test__get_recipients(self):
        self.assertEqual(
            ["a@b.com", "c@d.com"],
            _get_recipients()
        )
