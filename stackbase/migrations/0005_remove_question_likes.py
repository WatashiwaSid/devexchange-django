# Generated by Django 5.0.7 on 2024-07-24 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stackbase', '0004_question_likes_alter_comment_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='likes',
        ),
    ]
