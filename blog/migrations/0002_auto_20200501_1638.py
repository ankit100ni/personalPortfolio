# Generated by Django 3.0.5 on 2020-05-01 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogproject',
            old_name='desciption',
            new_name='blog_desciption',
        ),
        migrations.RenameField(
            model_name='blogproject',
            old_name='title',
            new_name='blog_title',
        ),
    ]