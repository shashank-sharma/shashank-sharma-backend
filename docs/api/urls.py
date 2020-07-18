from django.conf.urls import url


from .views import SpreadsheetAPIView


urlpatterns = [
    url(r'spreadsheet/$', SpreadsheetAPIView.as_view(), name='spreadsheet-api'),
]
