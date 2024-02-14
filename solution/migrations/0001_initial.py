# Generated by Django 5.0.2 on 2024-02-14 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_author', models.CharField(max_length=50)),
                ('quote_body', models.TextField()),
                ('context', models.CharField(blank=True, max_length=150)),
                ('source', models.CharField(blank=True, max_length=150)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
