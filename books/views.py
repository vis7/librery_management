from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.core.mail import send_mail
from django.conf import settings

from .forms import BookForm
from .models import Book, User

# Create your views here.class DetailView(View):
#     def __init__(""):
# def index_view(request):
#     return HttpResponse("<h1>hello world</h1>")


def template_view(request):
    msg = 'welcome to journy'
    int_var = 123
    context = {
        'msg': msg,
        'int_var': int_var
    }
    return render(request, "books/template.html", context)


def book_list_view(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, "books/book_list.html", context)


def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book': book
    }
    return render(request, "books/book_detail.html", context)


def book_index_view(request):
    return render(request, "books/book_index.html")


def book_create_view(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = BookForm()
    context = {
        'form': form
    }
    return render(request, "books/book_create.html", context)


def book_update_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "books/book_update.html", context)


def book_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect(reverse('books:book_list_view'))

    context = {
        'book': book
    }
    return render(request, "books/book_delete.html", context)


def template_tag_demo(request):
    int_var = 10
    context = {
        'int_var': int_var
    }
    return render(request, "books/template_tag_demo.html", context)


def base_view(request):
    return render(request, "books/base.html")


def static_file_demo_view(request):
    return render(request, "books/static_file_demo.html")

# Main Views
# createview
# updateview
# deleteview
# detailview
# listview

# class DetailView(View):
#     def __init__(""):


class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Book, pk=pk)


class BookListView(ListView):
    template_name = "books/book_list.html"
    queryset = Book.objects.all()


class BookCreateView(CreateView):
    template_name = "books/book_create.html"
    form_class = BookForm

    def get_success_url(self):
        return reverse('books:book_list_view')


class BookUpdateView(UpdateView):
    template_name = "books/book_update.html"
    form_class = BookForm

    def get_success_url(self):
        return reverse('books:book_list_view')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Book, pk=pk)


class BookDeleteView(DeleteView):
    template_name = "books/book_delete.html"

    def get_success_url(self):
        return reverse('books:book_list_view')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Book, pk=pk)


def book_issue_view(request):
    if request.method == 'GET':
        book_list = Book.objects.all()
        user_list = User.objects.all()
        context = {
            'book_list': book_list,
            'user_list': user_list
        }
    else:
        book_pk = request.POST.get('book_pk')
        user_pk = request.POST.get('user_pk')
        book = Book.objects.get(pk=book_pk)
        user = User.objects.get(pk=user_pk)

        user.books.add(book)

        # send_mail
        subject = 'book issued from librery'
        msg = f'you have taken {book.name}'
        host_email = settings.EMAIL_HOST
        recipient_list = ['vishvajeet.vnurture@gmail.com']

        send_mail(subject, msg, host_email, recipient_list)
        return redirect(reverse('books:book_list_view'))
    return render(request, "books/book_issue.html", context)


def index_view(request):
    return render(request, "books/index.html")
