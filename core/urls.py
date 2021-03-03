from django.urls import path
from .import views
from .views import home,delete_one,complete
urlpatterns = [
  path('', home , name="home"),
  path('delete/<int:pk>/' , delete_one ,name="delete_one"),
  path('complete/<int:pk>/' , complete , name="complete")
]
