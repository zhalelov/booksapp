# Generated by Django 2.2.7 on 2019-12-16 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_info',
            name='author',
            field=models.ManyToManyField(related_name='books', to='booksapp.Author'),
        ),
        migrations.AlterField(
            model_name='author',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
