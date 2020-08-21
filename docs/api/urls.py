from django.conf.urls import url


from .views import SpreadsheetAPIView, SpreadsheetLoginAPIView, SpreadsheetLogoutAPIView

urlpatterns = [
    url(r'spreadsheet/$', SpreadsheetAPIView.as_view(), name='spreadsheet-api'),
    url(r'login/$', SpreadsheetLoginAPIView.as_view(), name='spreadsheet-login-api'),
    url(r'logout/$', SpreadsheetLogoutAPIView.as_view(), name='spreadsheet-logout-api'),
]
