# Generated by Django 3.2.6 on 2021-09-02 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scraper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
                ('url', models.TextField(null=True)),
                ('price', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(null=True)),
                ('image', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
