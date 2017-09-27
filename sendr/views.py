import base64
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
    parser_classes = (parsers.MultiPartParser, parsers.FormParser, )

    def post(self, request, format=None):
        file_contents = self.request.data['image']
        mail_subject = self.request.data['subject']
        body = self.request.data['body']

        recipients = _get_recipients()

        mail = EmailMessage(
            subject=mail_subject,
            body=body,
            to=recipients,
        )
        filestream = base64.b64decode(file_contents[23:])
        mail.attach('image.jpg', filestream, 'image/jpg')

        try:
            mail.send(fail_silently=False)
        except AnymailRequestsAPIError as exc:  # noqa
            # TODO: setup logging
            raise
        except Exception as ex:  # noqa
            # TODO: setup logging
            raise
        return Response(status=200)
