from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models




def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug+'-'+str(int(time()))

class Book(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book_info(models.Model):
    title = models.CharField(max_length=512, db_index=True)
    isbn = models.IntegerField(blank=True, null=True)
    author = models.ManyToManyField('Author', related_name='books')
    category = models.CharField(max_length=50,blank=True)
    publishing_house = models.CharField(max_length=50, db_index=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    owner = models.CharField(max_length=50,blank=True)
    status = models.CharField(max_length=20, blank=True)
    rate = models.IntegerField(blank=True, null=True)
    add_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    descriptions = models.TextField(blank=True, db_index=True)

    def get_absolute_url(self):
        return reverse('books_details_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('book_info_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('book_info_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-add_date']


class Author(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=150, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('author_details_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('author_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('author_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']




