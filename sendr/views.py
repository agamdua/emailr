import os

from anymail.exceptions import AnymailRequestsAPIError
from django.core.mail import EmailMessage
from rest_framework import parsers
from rest_framework.response import Response
from rest_framework.views import APIView


def _get_recipients():
    env_recipients = os.environ['RECIPIENTS']
    return env_recipients.split(',')


class SendMail(APIView):
    parser_classes = (parsers.MultiPartParser,)

    def post(self, request, format=None):
        file_contents = self.request.FILES['image']

        recipients = _get_recipients()

        mail = EmailMessage(
            subject='testing image',
            body='testing',
            to=recipients,
        )
        filestream = file_contents.read()
        mail.attach('image.jpg', filestream, 'image/jpg')

        try:
            mail.send(fail_silently=False)
        except AnymailRequestsAPIError as exc:  # noqa
            # TODO: setup logging
            raise
        return Response(status=200)
