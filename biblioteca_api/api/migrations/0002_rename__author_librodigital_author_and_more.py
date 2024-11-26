# Generated by Django 5.1.3 on 2024-11-24 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='librodigital',
            old_name='_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='librodigital',
            old_name='_format',
            new_name='file_format',
        ),
        migrations.RenameField(
            model_name='librodigital',
            old_name='_published_date',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='librodigital',
            old_name='_size',
            new_name='size',
        ),
        migrations.RenameField(
            model_name='librodigital',
            old_name='_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='librofisico',
            old_name='_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='librofisico',
            old_name='_pages_amount',
            new_name='pages_amount',
        ),
        migrations.RenameField(
            model_name='librofisico',
            old_name='_published_date',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='librofisico',
            old_name='_title',
            new_name='title',
        ),
    ]
