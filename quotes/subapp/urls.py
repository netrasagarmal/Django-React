from django.urls import path
from subapp.views import ReactView
  
urlpatterns = [
    path('wel/', ReactView.as_view(), name="something"),
]