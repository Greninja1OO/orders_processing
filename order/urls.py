from django.urls import path
from . import views
app_name = "order"

urlpatterns = [
    path("", views.makeorder, name="makeorder"),
    path("history/", views.orderhistory, name="history"),
]
