# Generated by Django 2.0.6 on 2019-06-24 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=12)),
                ('fullname', models.CharField(max_length=50)),
            ],
        ),
    ]