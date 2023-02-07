from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path("", views.UploadView.as_view(), name="upload"),
]
