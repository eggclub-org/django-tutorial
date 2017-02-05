from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list$', views.list_books, name='list_books'),
    url(r'^(?P<category>.*)/(?P<book_id>.*)$', views.book_detail, name='book_detail'),
]