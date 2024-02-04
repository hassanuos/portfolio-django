# Generated by Django 5.0.1 on 2024-02-04 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('authname', models.CharField(max_length=12)),
                ('img', models.ImageField(blank=True, null=True, upload_to='block')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
