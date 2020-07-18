from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from docs.api.permissions import IsAdminOrSuperUser
from script.spreadsheet import SpreadsheetBuilder


class SpreadsheetAPIView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = (IsAdminOrSuperUser,)

    def get(self, request, format=None):
        # TODO: Implement this
        return Response({"data": "success"})

    def post(self, request, format=None):
        json_data = request.data
        if "filename" not in json_data or "data" not in json_data:
            return Response({"status": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
        sb = SpreadsheetBuilder(filename=json_data["filename"], json_data=json_data["data"])
        if sb.valid():
            # TODO: sb.save(append=True)
            sb.append()
            return Response({"status": "created"}, status=status.HTTP_201_CREATED)
        return Response({"status": "Incorrect Input"}, status=status.HTTP_400_BAD_REQUEST)
