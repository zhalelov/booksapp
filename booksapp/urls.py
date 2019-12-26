from django.urls import path
from .views import *
urlpatterns = [
    path('', crossbooking, name='crossbooking_url'),
    #path('search/', index, name='index_url'),
    path('createbook/', book_create.as_view(), name='book_create_url'),
    path('create_book_info/', Book_infoCreate.as_view(), name='book_info_create_url'),
    path('search/<id>/', book_details.as_view(), name='book_details_url'),
    path('authors/', author_list, name='author_list_url'),
    path('authors/create/', AuthorCreate.as_view(), name='author_create_url'),
    path('authors/<slug>/', AuthorDetails.as_view(), name='author_details_url'),
    path('authors/<slug>/update/', AuthorUpdate.as_view(), name='author_update_url'),
    path('authors/<slug>/delete/', AuthorDelete.as_view(), name='author_delete_url'),
    path('<slug>/', BooksDetail.as_view(), name='books_details_url'),
    path('<slug>/update/', Book_infoUpdate.as_view(), name='book_info_update_url'),
    path('<slug>/delete/', Book_infoDelete.as_view(), name='book_info_delete_url'),

]




