from rest_framework.views import APIView
from rest_framework.response import Response
from backend.settings import LATEST_UPDATED_AT


class HealthAPIView(APIView):
    permission_classes = []

    def get(self, request, format=None):
        # TODO: Health show configs of available settings
        return Response({"status": "up", "release": LATEST_UPDATED_AT})
