# Generated by Django 4.2.1 on 2023-08-08 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='products', to='products.tag'),
        ),
    ]
