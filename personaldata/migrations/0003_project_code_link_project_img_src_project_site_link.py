# Generated by Django 4.1.7 on 2023-02-27 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personaldata', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='code_link',
            field=models.URLField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='project',
            name='img_src',
            field=models.URLField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='project',
            name='site_link',
            field=models.URLField(default='', max_length=300),
        ),
    ]
