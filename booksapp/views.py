import pypyodbc
from django.views.generic import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q

from .forms import *
from .utils import *





def crossbooking(request):
    search_query = request.GET.get('search', '')
    if search_query:
        books = Book_info.objects.filter(Q(author__title__icontains=search_query) | Q(title__icontains=search_query)).distinct()
    else:
        books = Book_info.objects.all()
    pagination = Paginator(books, 2)
    page_number = request.GET.get('page', 1)
    page = pagination.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url
    }

    return render(request, 'books/crossbooking.html', context)

def index(request):

    books = Book.objects.all()
    all_books=[]
    mySQLServer = "LAPTOP-TT8V2S7B"
    mySQLDatabase = "Crossbooking"
    connection = pypyodbc.connect('Driver={SQL Server};'
                                  'Server=' + mySQLServer + ';'
                                  'Database=' + mySQLDatabase + ';')
    cursor = connection.cursor()

    mySQLQuery = """
                    select *
                    from all_books
                    where author  like '%'+ ? +'%'
                    """

    if (request.method == 'POST'):
        form = BooksForm(request.POST)
        form.save()
    form = BooksForm()

    for book in books:
        cursor.execute(mySQLQuery, [book.name])
        all_info = cursor.fetchall()
        for i in all_info:
            info = {'title': i[0], 'author': i[1], 'price': i[2], 'id': i[3]}
            all_books.append(info)

    context = {'all_info': all_books, 'form': form}
    cursor.close()
    connection.commit()
    connection.close()
    return render(request, 'books/index.html', context)

class book_details(View):
    def get(self, request, id):
        all_books = []
        mySQLServer = "LAPTOP-TT8V2S7B"
        mySQLDatabase = "Crossbooking"
        connection = pypyodbc.connect('Driver={SQL Server};'
                                      'Server=' + mySQLServer + ';'
                                      'Database=' + mySQLDatabase + ';')
        cursor = connection.cursor()

        mySQLQuery = """
                            select *
                            from all_books
                            where id  like  ?
                            """
        cursor.execute(mySQLQuery, [id])
        all_info = cursor.fetchall()
        for i in all_info:
            info = {'title': i[0], 'author': i[1], 'price': i[2], 'id': i[3]}
            all_books.append(info)

        context = {'all_info': all_books}
        cursor.close()
        connection.commit()
        connection.close()
        return render(request, 'books/book_details.html', context)


class book_create(LoginRequiredMixin, View):
        def get(self, request):
            form = SearchForm()
            return render(request, 'books/book_create.html', context={'form':form})

        def post (self, request):

            bound_form = SearchForm(request.POST)
            if bound_form.is_valid():
                bound_form.save()
                return redirect(index)
            return render(request, 'books/book_create.html', context={'form': bound_form})


class BooksDetail (objectDetailMixin, View):
    model = Book_info
    template = 'books/books_details.html'


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'books/author_list.html', context={'authors': authors})


class AuthorDetails(objectDetailMixin, View):
    model = Author
    template = 'books/author_details.html'


class AuthorCreate(LoginRequiredMixin, objectCreateMixin, View):
    form_model = AuthorForm
    template = 'books/author_create.html'


class Book_infoCreate(LoginRequiredMixin, objectCreateMixin, View):
    form_model = Book_infoForm
    template = 'books/book_info_create.html'


class Book_infoUpdate(LoginRequiredMixin, objectUpdateMixin, View):
    model = Book_info
    form_model = Book_infoForm
    template = 'books/book_info_update.html'


class AuthorUpdate(LoginRequiredMixin, objectUpdateMixin, View):
    model = Author
    form_model = AuthorForm
    template = 'books/author_update.html'


class AuthorDelete(LoginRequiredMixin, objectDeleteMixin, View):
    model = Author
    template = 'books/author_delete.html'
    redirect_url = 'author_list_url'


class Book_infoDelete(LoginRequiredMixin, objectDeleteMixin, View):
    model = Book_info
    template = 'books/book_info_delete.html'
    redirect_url = 'crossbooking_url'


