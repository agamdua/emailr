import os

from django.core.mail import EmailMessage
from rest_framework import parsers
from rest_framework.response import Response
from rest_framework.views import APIView


def _get_recipients():
    env_recipients = os.environ['RECIPIENTS']
    return env_recipients.split(',')


class SendMail(APIView):
    parser_classes = (parsers.FileUploadParser,)

    def post(self, request, format=None):
        file_contents = self.request.FILES['file']

        recipients = _get_recipients()

        mail = EmailMessage(
            subject='testing image',
            body='testing',
            to=recipients,
        )
        filestream = file_contents.read()[65:-22]
        mail.attach('image.jpg', filestream, 'image/jpg')

        mail.send(fail_silently=False)
        return Response(status=200)
