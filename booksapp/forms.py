from .models import *
from django import forms
from django.forms import ModelForm, TextInput
from django.core.exceptions import ValidationError


class BooksForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'book',
            'id': 'city',
            'placeholder':'Write a book'
        })}


class SearchForm(forms.Form):
    name = forms.CharField(max_length=50)

    def save(self):
        new_search = Book.objects.create(
            name=self.cleaned_data['name']
        )
        return new_search


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['title']

        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('create не может быть slug')
        if Author.objects.filter(slug__iexact=new_slug):
            raise ValidationError('"{}" уже есть в базе данных'.format(new_slug))
        return new_slug


class Book_infoForm(forms.ModelForm):
    class Meta:
        model = Book_info
        fields = [
            'title',
            'isbn',
            'author',
            'category',
            'publishing_house',
            'status',
            'rate',
            'descriptions'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'publishing_house': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'rate': forms.TextInput(attrs={'class': 'form-control'}),
            'descriptions': forms.TextInput(attrs={'class': 'form-control'})

        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('create не может быть slug')
        return new_slug
