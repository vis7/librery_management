# Generated by Django 2.2.13 on 2021-06-18 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='book_pic'),
        ),
    ]