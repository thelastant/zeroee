from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^info$", views.InfoView.as_view(), name="info"),
]
