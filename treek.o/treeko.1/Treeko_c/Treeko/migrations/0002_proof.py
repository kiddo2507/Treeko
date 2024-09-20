# Generated by Django 3.1.6 on 2021-02-13 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Treeko', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='proof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('image1', models.ImageField(upload_to='pics')),
                ('image2', models.ImageField(upload_to='pics')),
                ('image3', models.ImageField(upload_to='pics')),
                ('image4', models.ImageField(upload_to='pics')),
            ],
        ),
    ]