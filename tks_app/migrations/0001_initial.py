# Generated by Django 3.0.7 on 2020-06-18 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Embed_Youtube_Code', models.CharField(max_length=150)),
            ],
        ),
    ]
