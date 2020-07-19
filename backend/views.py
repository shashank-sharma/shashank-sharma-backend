from rest_framework.views import APIView
from rest_framework.response import Response


class HealthAPIView(APIView):
    def get(self, request, format=None):
        # TODO: Health show configs of available settings
        return Response({"status": "up"})
