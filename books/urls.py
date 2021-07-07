from django.urls import path
from books.views import (
    book_create_view, book_index_view, book_list_view,
    book_detail_view, book_update_view, book_delete_view,
    template_tag_demo, base_view, static_file_demo_view,
    BookDetailView, BookListView,
    BookCreateView, BookUpdateView, BookDeleteView,
    book_issue_view
    )

app_name = 'books'

urlpatterns = [
    # path('custom_template/', custom_template_view),
    # path('create/', book_create_view),
    # path('', book_list_view, name='book_list_view'),
    path('book_index/', book_index_view, name="book_index_view"),
    # path('<int:pk>/', book_detail_view, name="book_detail_view"),
    # path('<int:pk>/update/', book_update_view, name="book_update_view"),
    # path('<int:pk>/delete/', book_delete_view, name="book_delete_view"),
    path('template_tag_demo/', template_tag_demo, name='template_tag_demo_view'),
    path('base/', base_view, name='base_view'),
    path('static_file_demo/', static_file_demo_view, name='static_file_demo_view'),

    # class based views
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail_view'),
    path("", BookListView.as_view(), name='book_list_view'),
    path("create/", BookCreateView.as_view(), name='book_create_view'),
    path("<int:pk>/update/", BookUpdateView.as_view(), name="book_update_view"),
    path("<int:pk>/delete/", BookDeleteView.as_view(), name='book_delete_view'),
    path('issue/', book_issue_view, name='book_issue_view')
]



# books/custom_template