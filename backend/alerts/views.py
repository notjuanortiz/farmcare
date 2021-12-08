from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from alerts.models import Alert


class CreateEmailAlertView(APIView):

    def post(self, request):
        '''
        Creates a new email alert
        '''
        alert = Alert()
        recipient = request.data['recipient']
        message = request.data['message']

        if recipient is None:
            return Response("Failed to create alert. The 'recipient' field cannot be empty.", status=status.HTTP_400_BAD_REQUEST)

        alert.send(recipient, message)
        return Response("Successful", status=status.HTTP_201_CREATED)
