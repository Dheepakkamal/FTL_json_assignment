from django.urls import path, include
from json_api import views
# from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
        path("", views.index, name = "index"),
]
