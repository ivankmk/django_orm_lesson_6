# Generated by Django 2.2.5 on 2020-11-06 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_comment_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comments',
            field=models.ManyToManyField(related_name='comments', to='blog.Post', verbose_name='Комментарии'),
        ),
    ]
