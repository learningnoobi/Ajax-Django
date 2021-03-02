from django.urls import path
from .import views
from .views import home,delete_one
urlpatterns = [
  path('', home , name="home"),
  path('delete/<int:pk>/' , delete_one ,name="delete_one")
]
