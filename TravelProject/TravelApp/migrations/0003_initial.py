# Generated by Django 4.2.3 on 2023-07-11 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TravelApp', '0002_delete_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Img', models.ImageField(upload_to='Pics')),
                ('Desc', models.TextField()),
            ],
        ),
    ]
