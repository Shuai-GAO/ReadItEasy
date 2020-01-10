from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home_book),
    path('books/', views.show_books_list),
    path('books/<language>/<id_book>/', views.show_chapter),
    path('books/<language>/<id_book>/<int:reader_chapter>', views.show_chapter),
    path('books/<language>/<id_book>/statistics/', views.show_statistics),
    path('books/<language>/<id_book>/search/', views.show_search),
]