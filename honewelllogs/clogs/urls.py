from django.urls import path
from .views import ClogsAPIView

urlpatterns = [
    path("generate-logs", ClogsAPIView.as_view(), name='call-logs-api'),
    path("api/call-logs", ClogsAPIView.as_view(), name='call-logs-api')
]
