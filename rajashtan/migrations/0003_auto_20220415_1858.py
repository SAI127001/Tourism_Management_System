# Generated by Django 3.0.5 on 2022-04-15 13:28

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('rajashtan', '0002_rajashtan_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rajashtan',
            name='desc',
            field=tinymce.models.HTMLField(),
        ),
    ]